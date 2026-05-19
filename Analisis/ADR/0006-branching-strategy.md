# ADR 0006 — Estrategia de branches (branching)

Fecha: 2026-05-18

Estado: Propuesta

Contexto
- El repo ha tenido actividad en `main` y ramas de trabajo (`bitacoras-individuales-prueba`). Es necesario definir una estrategia clara para features, releases y hotfixes.

Decisión
- Adoptar un modelo trunk-based con ramas de característica (`feature/...`) y ramas de trabajo temporales para documentación (`docs/...`).

Reglas principales
- `main`: rama protegida, código/documentación estable.
- `feature/<name>`: ramas para desarrollo; PRs hacia `main` con revisión y CI-green.
- `docs/<topic>` o `bitacoras-<user>`: ramas para documentación y bitácoras, también pasan por PR.

Responsables
- Propietario: Cesar.

Pasos
- Añadir reglas de protección en `main` (revisión obligatoria, CI success required).
- Documentar en `CONTRIBUTING.md` el flujo recomendado.

---
Estado: Aceptada

- Fecha de aceptación: 2026-02-11 22:34:40 -0600
- Aprobador: Cesar Augusto Rodriguez Te

Responsabilidades tras aceptación:
- Responsable: Cesar Augusto Rodriguez Te — configurar reglas y guiar adopción.
- Verificación: PRs y políticas de protección aplicadas en `main`.
