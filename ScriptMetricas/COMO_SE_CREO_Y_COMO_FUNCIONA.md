# Como se creo el script y como entenderlo

## Objetivo del script

El script `python metricas.py` genera un CSV con metricas de colaboracion por persona, agrupadas por milestone semanal:

- Commits
- PRs fusionados
- Revisiones unicas por PR

El resultado final se guarda en `metricas_github.csv`.

## Problema que resuelve

Permite medir contribucion individual por semana de trabajo usando milestones de GitHub como marco temporal.

La semana se calcula asi:

- inicio = `due_on - 7 dias`
- fin = `due_on`

## Dependencias y requisitos

1. Python 3
2. PyGithub
3. Variable de entorno `GITHUB_TOKEN`
4. Repositorio con milestones que tengan `due_on`

## Diseno del script

### 1. Configuracion

Variables principales:

- `REPO_NAME`: repositorio en formato `owner/repo`
- `OUTPUT_CSV`: archivo de salida
- `INCLUDE_BOTS`: define si incluir cuentas bot
- `MILESTONE_NAME`: filtro opcional para una milestone especifica

### 2. Conexion a GitHub

Se usa autenticacion moderna de PyGithub:

```python
from github import Github, Auth
g = Github(auth=Auth.Token(TOKEN))
```

Esto evita el warning deprecado de `Github(TOKEN)`.

### 3. Funciones auxiliares

- `is_bot(user_name)`: detecta cuentas automatizadas comunes (`[bot]`, `dependabot`, `renovate`)
- `should_skip_user(user_name)`: aplica filtro de bots/nulos
- `get_user_login(user_obj, fallback_name=None)`: protege contra `None` y usa fallback cuando no hay usuario normalizado

### 4. Construccion de ventanas por milestone

Se recorren milestones y se arma un diccionario:

- `milestone_windows[titulo] = (inicio_semana, fin_semana)`

Si `MILESTONE_NAME` esta definido, solo se incluye esa milestone.

### 5. Conteo de commits

Por cada milestone semanal, consulta commits en el rango `since/until` y suma por autor.

### 6. Conteo de PRs y revisiones

Se recorren PRs cerrados una sola vez y se filtra:

- solo PRs fusionados
- solo PRs con milestone valida
- solo PRs cuya fecha `merged_at` cae dentro de la semana de su milestone

Para revisiones:

- se usa un `set` por PR
- cada reviewer cuenta maximo una vez por PR

### 7. Generacion del CSV

Columnas:

- Milestone
- Semana (inicio)
- Semana (fin)
- Autor
- Commits
- PRs fusionados
- Revisiones unicas por PR

## Decisiones tecnicas tomadas

1. Evitar doble consulta de PRs: PRs fusionados y revisiones se calculan en un mismo bucle.
2. Robustez ante nulos: se evita fallo cuando `user` no existe.
3. Filtro de bots configurable: misma regla para commits, PRs y reviews.
4. Filtro por milestone opcional: permite informes puntuales por sprint.

## Limites actuales

1. Si hay milestones con ventanas de fechas superpuestas, un commit podria contarse en mas de una milestone.
2. Si los PRs no tienen milestone o su `merged_at` cae fuera de ventana, no se contabilizan.

## Flujo de ejecucion recomendado

1. Activar entorno virtual
2. Instalar PyGithub
3. Exportar `GITHUB_TOKEN`
4. (Opcional) exportar `MILESTONE_NAME`
5. Ejecutar el script
6. Abrir `metricas_github.csv`

## Seguridad

- No pongas el token dentro del codigo.
- No ejecutes comandos con el token en texto plano en shell compartida.
- Si el token se expuso, debes revocarlo y generar uno nuevo.

## Ejemplo de ejecucion

```bash
cd /Users/cesrod/SoftwareDesign
source venv/bin/activate
export GITHUB_TOKEN="tu_token"
export MILESTONE_NAME="Weekly #3 Jueves 26"
cd ScriptMetricas
python "python metricas.py"
```

Para ejecutar todas las milestones:

```bash
unset MILESTONE_NAME
python "python metricas.py"
```
