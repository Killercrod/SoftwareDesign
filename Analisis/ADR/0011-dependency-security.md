# ADR 0011 — Política de dependencias y seguridad

Fecha: 2026-05-18

Estado: Propuesta

Contexto
- Mantener dependencias actualizadas y escaneos de seguridad reduce riesgo operativo.

Decisión
- Habilitar Dependabot para actualizaciones automáticas de dependencias y añadir scanner de seguridad en CI (por ejemplo, `npm audit` o `safety` para Python).

Pasos
- Configurar `dependabot.yml` para comprobar semanalmente.
- Añadir job en CI para ejecutar scanner de seguridad en PRs principales.

---
Estado: Aceptada

- Fecha de aceptación: 2026-02-11 22:34:40 -0600
- Aprobador: Cesar Augusto Rodriguez Te

Responsabilidades tras aceptación:
- Responsable: Cesar — habilitar Dependabot y revisar PRs de actualización.
- Verificación: Escaneos semanales y resolución de alertas críticas.
