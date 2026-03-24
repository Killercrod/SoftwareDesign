import os
import csv
from github import Github
from collections import defaultdict

# ===== CONFIGURACIÓN =====
REPO_NAME = "usuario/repositorio"   # Cambia por tu repositorio
OUTPUT_CSV = "metricas_github.csv"

# Lee el token desde variable de entorno (más seguro)
TOKEN = os.getenv("GITHUB_TOKEN")   # o "MI_TOKEN" si usas otro nombre

if not TOKEN:
    raise ValueError("No se encontró el token. Configura la variable de entorno GITHUB_TOKEN")

# ===== CONEXIÓN =====
g = Github(TOKEN)
repo = g.get_repo(REPO_NAME)

# Diccionarios para acumular métricas
commits_count = defaultdict(int)
prs_merged_count = defaultdict(int)
reviews_count = defaultdict(int)

# ===== 1. OBTENER COMMITS =====
print("Obteniendo commits...")
# PyGithub maneja la paginación automáticamente. Para repositorios muy grandes,
# podrías limitar con un slice (ej: get_commits()[:1000]) o usar since/until.
for commit in repo.get_commits():
    if commit.author:
        author = commit.author.login
    else:
        # Si el autor no es un usuario registrado (ej. commit por email)
        author = commit.commit.author.name

    # Opcional: ignorar bots (dependabot, etc.)
    if author and ("[bot]" in author or "dependabot" in author):
        continue

    commits_count[author] += 1

# ===== 2. OBTENER PULL REQUESTS FUSIONADOS =====
print("Obteniendo Pull Requests fusionados...")
for pr in repo.get_pulls(state='closed'):
    if pr.merged:
        author = pr.user.login
        prs_merged_count[author] += 1

# ===== 3. OBTENER REVISIONES REALIZADAS =====
print("Obteniendo revisiones de PRs...")
for pr in repo.get_pulls(state='closed'):
    for review in pr.get_reviews():
        reviewer = review.user.login
        reviews_count[reviewer] += 1

# ===== UNIR AUTORES =====
all_authors = set(commits_count.keys()) | set(prs_merged_count.keys()) | set(reviews_count.keys())

# ===== 4. GENERAR CSV =====
with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Autor', 'Commits', 'PRs fusionados', 'Revisiones'])

    for author in sorted(all_authors):
        writer.writerow([
            author,
            commits_count.get(author, 0),
            prs_merged_count.get(author, 0),
            reviews_count.get(author, 0)
        ])

print(f"Reporte generado: {OUTPUT_CSV}")
