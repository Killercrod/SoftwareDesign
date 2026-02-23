
# Introducción al Proyecto ECFCA

El **Sistema de Educación Continua para la FCA-UADY (ECFCA)** es una plataforma integral de gestión académica y comercial desarrollada en colaboración entre la Facultad de Matemáticas (FMAT) y la Facultad de Contaduría y Administración (FCA) de la Universidad Autónoma de Yucatán.

El sistema tiene como objetivo automatizar y optimizar todo el ciclo de vida de los eventos educativos ofrecidos por la unidad de Educación Continua, incluyendo cursos, diplomados y capacitaciones. La plataforma se estructura en tres pilares fundamentales:

1. **Gestión de Ventas (CRM)**: Captación de leads desde fuentes externas (Meta Ads, bolsa de trabajo UADY) y seguimiento de oportunidades comerciales.
2. **Gestión de Eventos**: Administración de programas académicos, generación de constancias y reportes.
3. **Gestión de Usuarios**: Manejo integral de participantes, capacitadores y personal administrativo.


---
## Índice de Documentos

- [Análisis de Usuarios](https://github.com/Killercrod/SoftwareDesign/blob/main/Analisis%20de%20Usuarios.pdf)
- [Casos de Uso](https://github.com/Killercrod/SoftwareDesign/blob/main/CasosDeUso.md)
- [Consideraciones para el Sistema](https://github.com/Killercrod/SoftwareDesign/blob/main/ConsideracionesParaElSistema.md)
- [Descripción General del Sistema](https://github.com/Killercrod/SoftwareDesign/blob/main/DescripciónGeneral.md)
# Introducción al Proyecto ECFCA
---

# Módulo de Gestión de Usuarios

El **Módulo de Gestión de Usuarios** constituye el núcleo del sistema en lo que respecta a la administración de personas que interactúan con la plataforma. Abarca desde el registro y autenticación del público general, pasando por la gestión de participantes inscritos en eventos, hasta la administración especializada de capacitadores y los procesos de validación documental realizados por el personal administrativo.

Este módulo facilita todo el ciclo de vida del usuario dentro del sistema:
- **Para el público general**: registro, solicitud de inscripción, carga de documentos, consulta de estatus y acceso a eventos.
- **Para capacitadores**: gestión de su perfil, información fiscal y consulta de eventos asignados.
- **Para el staff y coordinación**: validación de documentos, administración de perfiles y gestión de capacitadores.

---
Hemos seleccionado el **Módulo de Gestión de Usuarios** como punto de partida para nuestro análisis y desarrollo por las siguientes razones:

1. **Es el módulo más práctico y mejor delimitado**: Sus fronteras funcionales están claramente definidas, lo que facilita un análisis profundo y acotado sin depender críticamente de los otros módulos para su operación básica.

2. **Constituye la base del sistema**: Todos los demás módulos (Eventos y Ventas) dependen de la existencia de usuarios bien gestionados. Sin una sólida administración de participantes y capacitadores, los módulos de eventos y ventas carecerían de sentido.

3. **Interacción temprana con actores clave**: Permite validar requisitos con todos los tipos de usuario (público general, staff, capacitadores) desde etapas tempranas, asegurando que las necesidades fundamentales están cubiertas.

4. **Alta cohesión y bajo acoplamiento**: Aunque se integra con otros módulos, sus funcionalidades centrales (registro, autenticación, gestión de perfiles) pueden desarrollarse de manera independiente, reduciendo riesgos de interdependencias complejas al inicio del proyecto.

5. **Documentación existente**: Contamos con una base sólida de casos de uso y requisitos definidos en el repositorio original, así como un avance documentado por nuestro equipo, lo que nos permite progresar de manera ordenada y consistente.

Esta elección estratégica nos permitirá entregar valor tangible en un plazo razonable, establecer una arquitectura robusta y escalable, y generar aprendizajes que faciliten el abordaje posterior de los módulos restantes.
