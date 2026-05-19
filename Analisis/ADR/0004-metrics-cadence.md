# ADR 0004 — Cadencia y responsabilidad de métricas de repositorio

Fecha: 2026-05-18

 Estado: Aceptada

Contexto

Decisión

Responsables

---
Fecha de aceptación: 2026-02-11 22:34:40 -0600
Aprobador: Cesar Augusto Rodriguez Te

Responsabilidades tras aceptación:
- Responsable operativo: Cesar Augusto Rodriguez Te — coordinar la ejecución semanal y publicación de artefactos.
- Verificación: Publicación semanal del CSV y revisión en reuniones de seguimiento.

Pasos de implementación
1. Configurar un job recurrente (GitHub Actions `schedule`) que ejecute el script semanalmente (p. ej. lunes 02:00 UTC).
2. Añadir job para ejecutar métricas en PRs si el autor lo solicita (variable `RUN_METRICS_IN_PR=true`).
3. Publicar el CSV resultante como artefacto en las ejecuciones programadas.

Criterios de éxito
