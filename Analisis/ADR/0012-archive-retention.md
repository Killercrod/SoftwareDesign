# ADR 0012 — Retención y archivado de artefactos y métricas

Fecha: 2026-05-18

Estado: Propuesta

Contexto
- El sistema generará artefactos (CSV de métricas, snapshots de documentación) que pueden necesitar retención para auditoría.

Decisión
- Publicar métricas como artefactos en ejecuciones programadas y conservarlas por 90 días en el repository actions artifacts.

Pasos
- Configurar job programado que ejecute métricas y suba `metricas_github.csv` como artefacto con retención de 90 días.

---
Estado: Aceptada

- Fecha de aceptación: 2026-02-11 22:34:40 -0600
- Aprobador: Cesar Augusto Rodriguez Te

Responsabilidades tras aceptación:
- Responsable: Cesar — supervisar retención y publicación de artefactos.
- Verificación: Artefactos publicados con retención 90 días.
