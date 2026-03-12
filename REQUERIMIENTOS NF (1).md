**REQUISITOS NO FUNCIONALES**

Sistema ECFCA — Educación Continua FCA-UADY

# 1\. PROCESO DE GESTIÓN DE REQUISITOS NO FUNCIONALES

Los Requisitos No Funcionales (RNF) especifican los estándares y cualidades que debe cumplir un sistema para funcionar de manera eficaz, centrándose en cómo opera el sistema y no en qué hace. En el contexto del Sistema ECFCA, donde se gestionan datos personales sensibles de participantes, capacitadores y personal administrativo, los RNF son críticos para garantizar seguridad.

## 1.1 Descripción General

Este proceso establece la metodología para identificar, definir, documentar, implementar y revisar los RNF del Módulo de Gestión de Usuarios (MU), iniciando con CU-MU-001: Consultar Usuarios. El módulo administra el ciclo de vida completo de todos los actores del sistema: Público General, Capacitadores, Staff, Coordinación y Personal de Contabilidad.

## 1.2 Objetivo

Asegurar que los RNF se implementen correctamente, garantizando que el sistema ECFCA opere con los niveles de rendimiento, seguridad, disponibilidad y calidad requeridos para una plataforma de la UADY.

## 1.3 Identificación de RNF

A partir del caso de uso CU-MU-001 al CU-MU-009 y considerando que el sistema maneja información personal sensible bajo las restricciones del aviso de privacidad obligatorio, se identificaron los siguientes RNF:

|     |     |     |     |
| --- | --- | --- | --- |
| **ID RNF** | **Categoría** | **Descripción** | **Vinculado a RF** |
| RNF-01 | Rendimiento | La consulta de usuarios debe retornar resultados en un “tiempo promedio” para el volumen de registros esperado en ECFCA. |     |
| RNF-02 | Seguridad | Solo usuarios autenticados con rol autorizado (Staff, Coordinación) pueden ejecutar CU-MU-001. Los datos personales deben protegerse según el aviso de privacidad del sistema. |     |
| RNF-03 | Disponibilidad | El módulo de consulta debe estar disponible el 99% del tiempo en horario operativo institucional. |     |
| RNF-04 | Usabilidad | La interfaz de consulta debe ser operable en menos de 3 pasos desde el menú principal, adaptada al perfil del personal administrativo de la FCA. |     |
| RNF-05 | Mantenibilidad | El módulo debe seguir patrones de arquitectura documentados para facilitar su evolución conforme el sistema ECFCA crezca. |     |
| RNF-06 | Escalabilidad | El sistema debe soportar el crecimiento proyectado de usuarios del sistema ECFCA sin degradación visible del servicio. |     |

## 1.4 Criterios de Calidad

Los criterios de calidad definen las métricas medibles que determinan si un RNF se ha cumplido satisfactoriamente en el contexto del sistema ECFCA:

|     |     |     |     |
| --- | --- | --- | --- |
| **RNF ID** | **Criterio** | **Métrica** | **Umbral Aceptable** |
| RNF-01 | Tiempo de respuesta | Respuesta medida bajo carga normal de operación | FALTA RELLENAR |
| RNF-02 | Control de acceso | Porcentaje de intentos no autorizados bloqueados | 80% de bloqueo |
| RNF-03 | Disponibilidad | Tiempo activo dividido entre tiempo total operativo | ≥ 99% |
| RNF-04 | Pasos de navegación | Número de clics para llegar a la función de consulta | ≤ 3 pasos |
| RNF-05 | Cobertura documental | Porcentaje de módulos con documentación actualizada | ≥ 95% |
| RNF-06 | Usuarios concurrentes | Usuarios simultáneos sin tasa de error > 5% | FALTA RELLENAR |

## 1.5 Proceso de Evaluación

El proceso de evaluación de RNF sigue un flujo estructurado en cinco etapas:

- Etapa 1 — Definición: El equipo identifica los RNF durante la fase de análisis de cada caso de uso.
- Etapa 2 — Implementación: El desarrollador responsable integra los RNF en el diseño técnico.
- Etapa 3 — Prueba: Se ejecutan pruebas de rendimiento, seguridad y carga según las métricas definidas.
- Etapa 4 — Validación: Un integrante diferente al implementador verifica que los criterios se cumplan.
- Etapa 5 — Cierre: Se documenta el resultado en el registro de RNF y se actualiza el estado del issue.

## 1.6 Proceso de Revisión

|     |     |     |
| --- | --- | --- |
| **Fase de Revisión** | **Responsable** | **Frecuencia** |
| Revisión inicial | Lead del equipo | Al definir cada caso de uso |
| Revisión de implementación | Integrante diferente al implementador | Antes de merge a rama principal |
| Revisión periódica | Todo el equipo/Profesor | Sprint review / semanal (Jueves) |