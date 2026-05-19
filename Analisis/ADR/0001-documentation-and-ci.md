
# ADR 0001 — Validación mínima de documentación y métricas en CI

Fecha: 2026-05-18

Estado: Propuesta (pendiente aprobación)

Propósito
Esta ADR documenta la decisión de introducir una validación mínima en CI orientada a la calidad documental y a la ejecución automatizada del script de métricas. El objetivo es detectar problemas de formato en la documentación y mantener métricas actualizadas que faciliten la revisión en PRs.

Contexto
- El repositorio contiene documentación extensa (RF, RNF, diagramas, bitácoras) y un script de métricas (`ScriptMetricas/python metricas.py`).
- Actualmente no existe un pipeline que valide automáticamente la calidad mínima de la documentación ni que ejecute las métricas en cada PR.

Decisión
- Implementar un workflow de GitHub Actions con dos responsabilidades principales:
  1) Linting y validación básica de Markdown (encontrar errores de formato, enlaces rotos simples y problemas de estilo).
 2) Ejecución condicional del script de métricas para regenerar/validar `metricas_github.csv` en PRs cuando el script y el token estén disponibles.

Responsables
- Propietario (owner) de la decisión: Cesar Augusto Rodriguez Te.
- Implementación técnica: equipo de documentación (Cesar + Ivan) con revisión por Braulio.

Fecha de revisión
- Revisar esta ADR el: 2026-06-01 (puede adelantarse si se integran cambios relevantes antes).

Pasos detallados de implementación
1. Añadir el workflow `.github/workflows/docs-ci.yml` con los siguientes jobs:
   - `lint-markdown`: usa `github/super-linter` para validar archivos Markdown. Debe fallar el job si hay errores de lint.
   - `run-metrics`: ejecuta el script de métricas (`ScriptMetricas/python metricas.py`) solo si el archivo existe. El job debe fallar solo en errores graves del script; si falta `GITHUB_TOKEN` o no aplica (repositorio público sin permisos), el job debe avisar pero no bloquear la PR.
2. Documentar en este ADR las variables de entorno requeridas: `GITHUB_TOKEN` (usado por Actions si se necesita mayor acceso) y `MILESTONE_NAME` (opcional) para ejecuciones de métricas enfocadas.
3. Añadir un archivo `CONTRIBUTING.md` (si no existe) con indicaciones de formato de Markdown y cómo ejecutar localmente `ScriptMetricas/python metricas.py`.
4. Hacer pruebas en la rama `bitacoras-individuales-prueba` y revisar que el workflow no introduzca falsos positivos.

Criterios de éxito (medibles)
- En la primera semana tras activar el workflow:
  - ≥95% de archivos Markdown deben pasar el linter sin errores bloqueantes en PRs.
  - El job de métricas genera `ScriptMetricas/metricas_github.csv` en ejecuciones donde el script y token están disponibles, o deja un aviso claro cuando no fue posible.
  - Los revisores documentan reducción de issues de formato en PRs recurrentes (feedback cualitativo aceptable).

Rollback / seguimiento
- Si el workflow causa falsos positivos o bloqueos injustificados, se revertirá temporalmente el workflow y se ajustarán reglas del linter (por ejemplo, permitir reglas menos estrictas) antes de reactivar.

Notas
- Esta ADR es intencionalmente ligera: recoge la decisión y los pasos inmediatos. Pueda derivarse ADRs adicionales para decisiones relacionadas (por ejemplo, políticas de normalización de nombres de archivo o validación de Mermaid) si se decide ampliar la validación.

Estado: generado y pendiente de revisión/aceptación por el equipo.

---
Estado: Aceptada

- Fecha de aceptación: 2026-02-11 22:34:40 -0600
- Aprobador: Cesar Augusto Rodriguez Te
- Implementación vinculada: branch `bitacoras-individuales-prueba` (workflow `.github/workflows/docs-ci.yml`, `CONTRIBUTING.md`, ADRs 0001–0012)

Responsabilidades tras aceptación:
- Responsable principal: Cesar Augusto Rodriguez Te — coordinar la puesta en marcha y seguimiento.
- Verificación: equipo de documentación (Cesar + Ivan) probarán y reportarán resultados en issues o PRs.
