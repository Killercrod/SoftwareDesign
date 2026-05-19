# ADR 0007 — Política de revisión de Pull Requests

Fecha: 2026-05-18

Estado: Propuesta

Contexto
- Para garantizar calidad y trazabilidad, se define una política mínima de revisión de PRs.

Decisión
- Requerir al menos 1 approval para cambios de documentación y 2 approvals para cambios de código críticos.
- Requerir CI green (docs lint, métricas job) antes de permitir merge.

Reglas
- Añadir checklist en plantilla de PR: resumen, archivos afectados, tickets/issues relacionados.
- Si el PR toca la estructura del repo o renombre masivo, solicitar review de Cesar.

---
Estado: Aceptada

- Fecha de aceptación: 2026-02-11 22:34:40 -0600
- Aprobador: Cesar Augusto Rodriguez Te

Responsabilidades tras aceptación:
- Responsable: Cesar — asignar reviewers críticos y asegurar cumplimiento.
- Verificación: Revisiones y checks antes del merge.
