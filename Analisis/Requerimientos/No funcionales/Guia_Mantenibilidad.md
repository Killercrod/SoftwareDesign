# Guía de Mantenibilidad y Modificabilidad 

Este documento establece los estándares y reglas de diseño para asegurar que cualquier desarrollador del equipo pueda realizar cambios en el proyecto de forma segura, minimizando el riesgo de errores en funcionalidades existentes.

## 1. Conceptos Fundamentales

Para este proyecto, definimos :

* **Mantenibilidad (General):** La facilidad con la que el sistema se modifica para corregir errores o adaptarse a nuevos requisitos.
* **Modificabilidad (Específica):** La capacidad de alterar la estructura o funcionalidad sin generar errores en otras partes del código. 

Diferencia con una analogía:

* **Mantenibilidad (General):** es como tener una casa bien organizada y limpia.
* **Modificabilidad (Específica):** es cuando quieres derribar una pared para hacer un cuarto más grande, no se te caiga el techo

---
En cuanto la documentación, se seleccionó el  RNF-04, ya que es el que tiene un rol más importante en la Mantenibilidad del proyecto:
## 2. Arquitectura en Capas (RNF-04)

Para mantener nuestra mantenibilidad separamos responsabilidades mediante una arquitectura de tres capas:

| Capa | Responsabilidad Principal |
| :--- | :--- |
| **Controller** | Maneja solicitudes HTTP e invoca métodos del Service. |
| **Service** | Contiene la lógica de negocio y procesa operaciones. |
| **Repository** | Gestiona la lectura y escritura en la base de datos. |

### Principios de Diseño
* **Alta Cohesión:** Cada capa tiene una única tarea clara.
* **Bajo Acoplamiento:** Modificar una capa (ej. cambiar el motor de BD) no obliga a modificar las demás.
* **KISS:** Código simple y directo; evitar complejidad innecesaria.
* **Sin dependencias cíclicas:** Las capas no se llaman entre sí de forma circular.

---

## 3. Estándares de Codificación

Para mantener el orden arquitectónico, se deben seguir estas reglas:

1.  **Organización de Archivos:** El código debe residir en sus carpetas correspondientes: `/controllers`, `/services`, `/repositories`, `/models`, `/schemas`.
2.  **Validación de Datos:** Es obligatorio usar **Pydantic** para validar esquemas en cada modificación.
3.  **Documentación:** Todo cambio debe incluir documentación básica (docstrings) explicando su propósito.
4.  **Lógica Pura:** Ninguna capa debe contener lógica que corresponda a otra (ej. no escribir queries de BD en el Controller).

---

## 4. Gestión de Cambios

### Cambios en Base de Datos (MongoDB)
*Nota: Se profundizara y se aceptaran los cambios en el Issue #54. (ÁUN EN PROGRESO)*
* La adición de campos nuevos no debe romper documentos existentes.
* Todo cambio de esquema se refleja primero en `/models` y `/schemas` antes de tocar el Repository.
* Los cambios deben probarse en el entorno de desarrollo obligatoriamente.

### Flujo para Cambios Multicapa
Cuando una modificación afecte a más de una capa, seguir este orden ascendente:
1.  **Identificar** las capas afectadas.
2.  **Actualizar Repository** (Capa de datos).
3.  **Actualizar Pydantic Schemas** (Validación).
4.  **Actualizar Service** (Lógica de negocio).
5.  **Actualizar Controller** (Interfaz de entrada/salida).
6.  **Verificar** la respuesta final del endpoint.

---

## 5. Ejemplo Práctico: Agregar campo a "Usuario"

Para agregar un nuevo campo de forma segura, el flujo es:
1.  Modificar el modelo en `/app/models`.
2.  Actualizar el schema de validación en `/app/schemas` con Pydantic.
3.  Ajustar las funciones del Repository en `/app/repositories`.
4.  Ajustar el Service si el nuevo campo requiere lógica adicional.
5.  Verificar que el Controller responda correctamente.
6.  **Validación cruzada:** Asegurar que se sigan cumpliendo **RNF-06** (formularios) y **RNF-09** (ID único).

---

## 6. Métricas de Calidad

Todo cambio será evaluado bajo las siguientes métricas:
* **Modularidad:** Responsabilidades claramente separadas.
* **Mensajes de Error:** Deben ser descriptivos y amigables (RNF-06).
* **Persistencia de Identidad:** El ID único del capacitador debe ser estable (RNF-09).
* **Documentación:** Presencia de comentarios en cambios realizados.
