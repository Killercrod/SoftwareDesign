# Reporte Final Mensual - Marzo 2026

## Base de este reporte
- Fuente principal: `ScriptMetricas/metricas_github.csv` generado al volver a ejecutar `python metricas.py` despues de actualizar `main`.
- Se uso el mismo criterio del script para mantener objetividad y comparabilidad:
  - Ventanas semanales por milestone con `due_on`.
  - Conteo por autor de `Commits`, `PRs fusionados`, `Revisiones unicas por PR`.
- Validacion posterior al cierre de la ultima milestone:
  - `Weekly#4` ya tiene `due_on` y ahora si entra al calculo del script.

## Resultado cuantitativo final (script actualizado)
- Filas de datos: 19 (autores por milestone)
- Milestones evaluadas: 4
  - `Weekly #1 Jueves 12` (2026-03-05 a 2026-03-12)
  - `Weekly  #2 Jueves 19` (2026-03-12 a 2026-03-19)
  - `Weekly #3 Jueves 26` (2026-03-19 a 2026-03-26)
  - `Weekly#4` (2026-03-24 a 2026-03-31)
- Totales del periodo cubierto por milestones:
  - Commits: 120
  - PRs fusionados: 0
  - Revisiones unicas por PR: 0

## Desglose por milestone
- Weekly #3 Jueves 26: 59 commits, 0 PRs fusionados, 0 revisiones
- Weekly #1 Jueves 12: 32 commits, 0 PRs fusionados, 0 revisiones
- Weekly  #2 Jueves 19: 16 commits, 0 PRs fusionados, 0 revisiones
- Weekly#4: 13 commits, 0 PRs fusionados, 0 revisiones

## Desglose por autor
- Killercrod: 76 commits, 0 PRs fusionados, 0 revisiones
- KERMITH79: 14 commits, 0 PRs fusionados, 0 revisiones
- IvanChiPolanco: 12 commits, 0 PRs fusionados, 0 revisiones
- JonEsp87: 8 commits, 0 PRs fusionados, 0 revisiones
- BraulioTelloMancilla: 6 commits, 0 PRs fusionados, 0 revisiones
- jsrangel666: 4 commits, 0 PRs fusionados, 0 revisiones

## Analisis semana a semana (a fondo)

### Semana 1 - Weekly #1 Jueves 12 (2026-03-05 a 2026-03-12)
- Metricas del script:
  - 32 commits
  - Distribucion por autor: Killercrod (15), KERMITH79 (9), JonEsp87 (7), BraulioTelloMancilla (1)
  - PRs y revisiones: 0
- Evidencia en repositorio:
  - Predominan cambios de base en RNF, glosario, estructura inicial y limpieza/reorganizacion de documentos.
  - Se observan merges de PR que consolidan aportes de varios integrantes en una misma ventana.
  - Archivos frecuentes en esta semana: documentos de RNF, glosario, bitacora de Omar, e imagenes de apoyo en `images/`.
- Lectura objetiva:
  - Semana de construccion y estabilizacion de artefactos base del analisis.

### Semana 2 - Weekly  #2 Jueves 19 (2026-03-12 a 2026-03-19)
- Metricas del script:
  - 16 commits
  - Distribucion por autor: Killercrod (12), BraulioTelloMancilla (1), IvanChiPolanco (1), KERMITH79 (1), jsrangel666 (1)
  - PRs y revisiones: 0
- Evidencia en repositorio:
  - Fuerte reestructuracion de la carpeta `Analisis/Requerimientos` (movimientos, renombres y normalizacion Funcionales/No funcionales).
  - Ajustes sobre el diagrama de procesos en Mermaid y consolidacion de README/bitacoras.
  - Archivos mas tocados incluyen `Analisis/Requerimientos/Funcionales/Bussines process diagram.mermaid`, `README.md` y documentos RF/RNF movidos.
- Lectura objetiva:
  - Semana de ordenamiento y estandarizacion documental, con menor volumen que Semana 1 pero alta intensidad de reorganizacion.

### Semana 3 - Weekly #3 Jueves 26 (2026-03-19 a 2026-03-26)
- Metricas del script:
  - 59 commits
  - Distribucion por autor: Killercrod (42), IvanChiPolanco (10), BraulioTelloMancilla (3), KERMITH79 (3), JonEsp87 (1)
  - PRs y revisiones: 0
- Evidencia en repositorio:
  - Pico de actividad del mes.
  - Incorporacion del paquete de metricas (`ScriptMetricas/python metricas.py`, `INSTRUCCIONES.md`, `COMO_SE_CREO_Y_COMO_FUNCIONA.md`).
  - Avances de mantenibilidad/modificabilidad y ajustes adicionales de documentacion y bitacoras.
- Lectura objetiva:
  - Semana de mayor productividad, enfocada en instrumentacion de medicion y consolidacion de calidad documental.

### Semana 4 - Weekly#4 (2026-03-24 a 2026-03-31)
- Metricas del script:
  - 13 commits
  - Distribucion por autor: Killercrod (7), jsrangel666 (3), BraulioTelloMancilla (1), IvanChiPolanco (1), KERMITH79 (1)
  - PRs y revisiones: 0
- Evidencia en repositorio:
  - Integraciones finales por PR.
  - Inclusion de `Estrategia BD.md`.
  - Movimiento de `Guia_Mantenibilidad.md` a `Analisis/Requerimientos/No funcionales/Guia_Mantenibilidad.md`.
  - Ajustes y normalizacion de diagramas/artefactos funcionales y actualizaciones de bitacoras.
- Lectura objetiva:
  - Cierre de mes con integracion y refinamiento final de entregables, ahora si reflejado por la milestone `Weekly#4`.

## Analisis del estado del repositorio (cualitativo)
- El repositorio esta orientado a analisis y documentacion de requisitos del proyecto ECFCA, con enfasis en el modulo de gestion de usuarios.
- En `README.md` se consolida la estructura documental del proyecto, incluyendo bitacoras, RF y RNF.
- Se incorporaron/actualizaron documentos clave de calidad y arquitectura:
  - `Analisis/Requerimientos/No funcionales/Guia_Mantenibilidad.md`
  - `Estrategia BD.md`
  Estos artefactos refuerzan modificabilidad, mantenibilidad y estrategia de cambios en base de datos.
- Las bitacoras muestran trazabilidad de trabajo por integrante y aportan evidencia de evolucion semanal.

## Interpretacion objetiva
- El script confirma que la actividad medida en sus ventanas semanales se concentra en la milestone que cierra el 26 de marzo.
- En esta corrida no aparecen PRs fusionados ni revisiones contabilizadas por el script (todas en 0), por lo que el indicador dominante es commits.
- Tras asignar `due_on` a `Weekly#4`, el script incorporo esa ventana y aumento los totales de commits del reporte.

## Limites del reporte
- Este reporte no representa todo el mes calendario completo, solo el rango cubierto por milestones con `due_on`.
- Si hay PRs sin milestone, fuera de ventana, o merges fuera de ese rango, no se veran reflejados en el CSV.
- Si una milestone esta cerrada pero no tiene `due_on`, tampoco se refleja en el CSV.

## Cierre
Este documento es el resumen final consolidado del mes, construido con la salida actualizada del script y complementado con lectura del estado documental del repositorio para dar contexto tecnico y organizacional.
