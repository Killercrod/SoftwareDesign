# Guia Paso a Paso para Ejecutar python metricas.py

## Que necesitas tener

1. Python 3 instalado.
2. Acceso al repositorio en GitHub.
3. Un token personal de GitHub con permisos de lectura de repositorio y PRs.
4. Milestones en GitHub con fecha due_on configurada.

## Paso 1: Ir al proyecto

```bash
cd /Users/cesrod/SoftwareDesign
```

## Paso 2: Crear y activar entorno virtual (recomendado)

```bash
/opt/homebrew/bin/python3 -m venv venv
source venv/bin/activate
```

Nota: Si ya existe venv, solo activa con source venv/bin/activate.

## Paso 3: Instalar dependencias

```bash
pip install PyGithub
```

## Paso 4: Configurar el token de GitHub

```bash
export GITHUB_TOKEN="tu_token_aqui"
```

## Paso 5: Verificar el repositorio en el script

Archivo: python metricas.py

Debe tener esta forma:

```python
REPO_NAME = "usuario/repositorio"
```

Ejemplo real:

```python
REPO_NAME = "Killercrod/SoftwareDesign"
```

## Paso 6: Elegir si quieres todas las milestones o solo una

Opcion A: todas las milestones

```bash
unset MILESTONE_NAME
```

Opcion B: una milestone especifica

```bash
export MILESTONE_NAME="Weekly #3 Jueves 26"
```

## Paso 7: Ejecutar el script

```bash
cd /Users/cesrod/SoftwareDesign/ScriptMetricas
/Users/cesrod/SoftwareDesign/venv/bin/python "python metricas.py"
```

## Paso 8: Revisar el resultado

El archivo generado es:

metricas_github.csv

Ver rapido en terminal:

```bash
cd /Users/cesrod/SoftwareDesign/ScriptMetricas
column -t -s',' metricas_github.csv | head -30
```

## Como interpreta el script las semanas

Para cada milestone con due_on:

- Semana inicio = due_on - 7 dias
- Semana fin = due_on

Todo se agrupa por esa ventana semanal.

## Que columnas genera el CSV

- Milestone
- Semana (inicio)
- Semana (fin)
- Autor
- Commits
- PRs fusionados
- Revisiones unicas por PR

## Configuracion opcional de bots

Por defecto, los bots vienen excluidos.

Para incluir bots en una corrida puntual:

```bash
export INCLUDE_BOTS="true"
```

Para excluir bots explicitamente:

```bash
export INCLUDE_BOTS="false"
```

Valores aceptados como verdadero: 1, true, yes, y, si.

## Errores comunes y solucion

Error: No module named github

- Activa el venv correcto y ejecuta pip install PyGithub.

Error: No se encontro el token

- Ejecuta export GITHUB_TOKEN="..." antes de correr.

Error: No se encontraron milestones con due_on

- Agrega fecha due_on en al menos una milestone en GitHub.

CSV con PRs y revisiones en 0

- Revisa que los PRs esten fusionados.
- Revisa que tengan milestone asignada.
- Revisa que merged_at caiga dentro de la ventana semanal de la milestone.
