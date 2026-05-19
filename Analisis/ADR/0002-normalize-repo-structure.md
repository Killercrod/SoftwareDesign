# ADR 0002 — Normalizar estructura y nombres de archivos del repositorio

Fecha: 2026-05-18

Estado: Propuesta

Contexto
- El repositorio contiene archivos y carpetas con nombres que incluyen espacios, acentos y formatos inconsistentes (por ejemplo, `Bitácoras/`, nombres con espacios y mayúsculas variables). Esto dificulta scripting, búsquedas y automatización.

Decisión
- Establecer una convención de estructura y nombres:
  - Nombres de carpetas y archivos en kebab-case (minúsculas, guiones) o snake_case según preferencia del equipo; propuesto: kebab-case.
  - Evitar espacios y caracteres acentuados en nombres de archivos y carpetas.
  - Mantener secciones principales en la raíz: `analisis/`, `bitacoras/`, `script-metricas/`, `docs/`, `images/`, `README.md`.

Responsables
- Propietario: Cesar Augusto Rodriguez Te.
- Implementación: Ivan (normalización) y revisión por todo el equipo.

Fecha de revisión
- Revisar el estado y aceptación el: 2026-06-08.

Pasos de implementación
1. Crear una rama `refactor/normalize-structure` y mapear nombres actuales → nombres normalizados.
2. Aplicar renombrados atómicos con commits claros (evitar grandes commits que mezclen contenido y renombrados).
3. Actualizar referencias internas (links en Markdown) y scripts que dependan de rutas.
4. Comunicar a todo el equipo antes de la fusión y dar tiempo para adaptaciones.

Criterios de éxito
- Todos los archivos y carpetas principales renombrados y referenciados correctamente.
- Ningún script o link roto en la rama de integración (pasar validación de CI antes de merge).

Notas

---
Estado: Aceptada

- Fecha de aceptación: 2026-02-11 22:34:40 -0600
- Aprobador: Cesar Augusto Rodriguez Te

Responsabilidades tras aceptación:
- Responsable principal: Cesar Augusto Rodriguez Te — coordinar la normalización y seguimiento.
- Verificación: Ivan realizará los renombrados atómicos y el equipo verificará links y scripts.
- Los renombrados pueden generar muchos cambios en Git; seguir la práctica de commits atómicos y PRs revisables.
