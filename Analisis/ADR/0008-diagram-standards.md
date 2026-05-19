# ADR 0008 — Estándares para diagramas y formatos

Fecha: 2026-05-18

Estado: Propuesta

Contexto
- Hay múltiples diagramas en formatos distintos (Mermaid en Markdown, PNG, drawio). Conviene unificar los estándares para facilitar mantenimiento y versionado.

Decisión
- Preferir diagrams as code cuando sea posible (Mermaid) y almacenar los archivos fuente en `Analisis/Diagramas/`.
- Para imágenes exportadas (PNG/PDF), guardar en `images/` con nombre derivado del fuente y fecha.

Reglas
- Nombre: `analisis-diagrama-<tipo>-<nombre>.md` o `.mmd` para Mermaid.
- Incluir bloque de metadatos en el archivo con autor y fecha.

---
Estado: Aceptada

- Fecha de aceptación: 2026-02-11 22:34:40 -0600
- Aprobador: Cesar Augusto Rodriguez Te

Responsabilidades tras aceptación:
- Responsable: Equipo de análisis — estandarizar fuentes en `Analisis/Diagramas/`.
- Verificación: Revisión de diagramas nuevos y migración progresiva de fuentes.
