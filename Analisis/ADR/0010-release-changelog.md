# ADR 0010 — Releases y generación de changelog

Fecha: 2026-05-18

Estado: Propuesta

Contexto
- No hay política clara de releases ni generación de changelog automatizado.

Decisión
- Adoptar releases semánticos y generar changelog automático desde commits que sigan la convención (Conventional Commits) usando una herramienta (p. ej. `github-changelog-generator` o `auto`).

Pasos
- Comenzar por documentar en `CONTRIBUTING.md` el uso de Conventional Commits.
- Configurar job opcional que genere un borrador de changelog en releases.

---
Estado: Aceptada

- Fecha de aceptación: 2026-02-11 22:34:40 -0600
- Aprobador: Cesar Augusto Rodriguez Te

Responsabilidades tras aceptación:
- Responsable: Cesar — supervisar la generación de changelogs y releases.
- Verificación: Revisión de borradores de changelog en releases.
