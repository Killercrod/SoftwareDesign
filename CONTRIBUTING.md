# Contributing

Gracias por contribuir. Este archivo resume pasos rápidos para colaborar en el repo.

1) Preparar entorno local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt || true
pip install PyGithub || true
```

2) Ejecutar el script de métricas (opcional)

```bash
cd ScriptMetricas
python "python metricas.py"
```

3) Política de commits
- Usa mensajes predecibles: `<type>(scope?): descripción breve` donde `type` ∈ {feat, fix, docs, style, refactor, chore, ci}.
- Ejemplo: `docs(adr): add ADR for docs CI`

4) Pull Requests
- Crea PRs pequeños y revisables. Incluye descripción, archivos cambiados y issues relacionados.
- Para cambios en estructura (renombrados masivos), solicita revisión de `Cesar Augusto Rodriguez Te`.

5) Bitácoras
- Actualiza tu bitácora en `Bitácoras/<TuNombre>/` semanalmente o al cierre de milestone.

6) ADRs
- Las decisiones de diseño se guardan en `Analisis/ADR/`.
