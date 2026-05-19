# ADR 0003 — Política de commits y formato de mensajes

Fecha: 2026-05-18

Estado: Propuesta

Contexto
- La base de commits actual contiene mensajes con formatos variados y numerosas cargas directas de archivos. Una política consistente facilita búsqueda, trazabilidad y automatizaciones (por ejemplo, generación de changelogs).

Decisión
- Adoptar una política sencilla basada en convenciones de prefijos (inspirada en Conventional Commits) y en PRs revisables:
  - Mensaje de commit: `<type>(scope?): descripción breve` donde `type` ∈ {feat, fix, docs, style, refactor, chore, ci}.
  - Cuerpo opcional: explicar el motivo y referenciar issues/PRs si aplica.
  - No subir archivos grandes por upload directo sin PR (usar PR con descripción y revisión).

Responsables
- Propietario: Cesar + líderes de equipo.

Fecha de revisión
- Revisar el cumplimiento y ajustes el: 2026-06-01.

Pasos de implementación
1. Añadir `CONTRIBUTING.md` con ejemplos de mensajes y reglas mínimas.
2. Añadir un `commit-msg` hook opcional (en `tools/`) y plantilla para `prepare-commit-msg` si el equipo lo desea.
3. Configurar una plantilla de Pull Request que solicite descripción, issues relacionados y checklist de revisión.
4. Comunicar la política y dejar una ventana de adaptación de 1 semana.

Criterios de éxito
- 80% de los commits de la rama principal y PRs activos usando el formato en las dos semanas posteriores.

---
Estado: Aceptada

- Fecha de aceptación: 2026-02-11 22:34:40 -0600
- Aprobador: Cesar Augusto Rodriguez Te

Responsabilidades tras aceptación:
- Responsable principal: Cesar Augusto Rodriguez Te — supervisar adopción del formato de commits.
- Verificación: Revisiones de PRs y muestreo semanal de commits.
