import os
import csv
from datetime import timedelta
from github import Github, Auth
from collections import defaultdict

# ===== CONFIGURACIÓN =====
REPO_NAME = "Killercrod/SoftwareDesign"   # Cambia por tu repositorio
OUTPUT_CSV = "metricas_github.csv"
INCLUDE_BOTS = os.getenv("INCLUDE_BOTS", "false").strip().lower() in {"1", "true", "yes", "y", "si"}
MILESTONE_NAME = os.getenv("MILESTONE_NAME", "").strip()  # Ej: "Weekly #3 Jueves 26"

# Lee el token desde variable de entorno (más seguro)
TOKEN = os.getenv("GITHUB_TOKEN")   # o "MI_TOKEN" si usas otro nombre

if not TOKEN:
    raise ValueError("No se encontró el token. Configura la variable de entorno GITHUB_TOKEN")

# ===== CONEXIÓN =====
# Evita pasar el token por linea de comando; usa siempre variable de entorno.
g = Github(auth=Auth.Token(TOKEN))
repo = g.get_repo(REPO_NAME)

def is_bot(user_name):
    if not user_name:
        return False
    lower_name = user_name.lower()
    return "[bot]" in lower_name or "dependabot" in lower_name or "renovate" in lower_name


def should_skip_user(user_name):
    return (not user_name) or (not INCLUDE_BOTS and is_bot(user_name))


def get_user_login(user_obj, fallback_name=None):
    if user_obj and getattr(user_obj, "login", None):
        return user_obj.login
    return fallback_name


# Estructura: metrics[milestone_title][author] = {commits, prs_merged, reviews}
metrics = defaultdict(lambda: defaultdict(lambda: {
    "commits": 0,
    "prs_merged": 0,
    "reviews": 0,
}))

# milestone_windows[title] = (start_week, end_week)
milestone_windows = {}

print("Obteniendo milestones...")
for milestone in repo.get_milestones(state="all"):
    # Se asume una semana fija por milestone: [due_on - 7 dias, due_on]
    if MILESTONE_NAME and milestone.title != MILESTONE_NAME:
        continue

    if not milestone.due_on:
        continue

    end_week = milestone.due_on
    start_week = end_week - timedelta(days=7)
    milestone_windows[milestone.title] = (start_week, end_week)

if not milestone_windows:
    if MILESTONE_NAME:
        raise ValueError(
            f"No se encontro la milestone '{MILESTONE_NAME}' con due_on configurado."
        )
    raise ValueError(
        "No se encontraron milestones con due_on. Configura fechas en milestones para calcular semanas."
    )

if MILESTONE_NAME:
    print(f"Filtrando por milestone: {MILESTONE_NAME}")

# ===== 1. OBTENER COMMITS POR MILESTONE-SEMANAL =====
print("Obteniendo commits por semana de milestone...")
for milestone_title, (start_week, end_week) in milestone_windows.items():
    for commit in repo.get_commits(since=start_week, until=end_week):
        author = get_user_login(commit.author, commit.commit.author.name)
        if should_skip_user(author):
            continue
        metrics[milestone_title][author]["commits"] += 1

# ===== 2 y 3. OBTENER PRs FUSIONADOS + REVISIONES (1 SOLA PASADA) =====
print("Obteniendo PRs fusionados y revisiones unicas por PR...")
for pr in repo.get_pulls(state="closed"):
    if not pr.merged:
        continue

    if not pr.milestone or pr.milestone.title not in milestone_windows:
        continue

    milestone_title = pr.milestone.title
    start_week, end_week = milestone_windows[milestone_title]

    # Se cuenta el PR en la semana de su milestone si su merge cae en la ventana semanal
    if not pr.merged_at or not (start_week <= pr.merged_at <= end_week):
        continue

    pr_author = get_user_login(pr.user)
    if not should_skip_user(pr_author):
        metrics[milestone_title][pr_author]["prs_merged"] += 1

    # Revisiones unicas por PR: un reviewer cuenta maximo 1 vez por PR
    unique_reviewers = set()
    for review in pr.get_reviews():
        reviewer = get_user_login(review.user)
        if should_skip_user(reviewer):
            continue
        unique_reviewers.add(reviewer)

    for reviewer in unique_reviewers:
        metrics[milestone_title][reviewer]["reviews"] += 1

# ===== 4. GENERAR CSV =====
with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Milestone',
        'Semana (inicio)',
        'Semana (fin)',
        'Autor',
        'Commits',
        'PRs fusionados',
        'Revisiones unicas por PR',
    ])

    for milestone_title in sorted(metrics.keys()):
        start_week, end_week = milestone_windows[milestone_title]
        authors = sorted(metrics[milestone_title].keys())

        for author in authors:
            writer.writerow([
                milestone_title,
                start_week.strftime('%Y-%m-%d'),
                end_week.strftime('%Y-%m-%d'),
                author,
                metrics[milestone_title][author]['commits'],
                metrics[milestone_title][author]['prs_merged'],
                metrics[milestone_title][author]['reviews'],
            ])

print(f"Reporte generado: {OUTPUT_CSV}")
