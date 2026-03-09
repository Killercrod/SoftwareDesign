# Atributos de Calidad del Sistema

Este documento define los **atributos de calidad del sistema**, los cuales forman parte de los **Requisitos No Funcionales (RNF)**.  

Los atributos de calidad describen **cómo debe comportarse el sistema** y se basan en el modelo de calidad definido por el estándar ISO/IEC 25010.

---

# 1. Rendimiento (Performance)

## Descripción
El sistema debe responder a las solicitudes de los usuarios en un tiempo adecuado para garantizar una buena experiencia.

## Escenario de calidad

Fuente: Usuario  
Estímulo: Solicitud de una acción dentro del sistema  
Ambiente: Uso normal del sistema  
Artefacto: Servidor o aplicación  
Respuesta: El sistema procesa la solicitud  
Medida: Tiempo de respuesta menor a 2 segundos

## Issue sugerido

**RNF-01 Mejorar rendimiento del sistema**

### Descripción
El sistema debe responder a las solicitudes de los usuarios en menos de 2 segundos bajo condiciones normales de uso.

### Criterios de aceptación

- Tiempo de respuesta promedio menor a 2 segundos
- Pruebas realizadas con múltiples usuarios
- No saturación del servidor en uso normal

---

# 2. Seguridad

## Descripción
El sistema debe proteger la información de los usuarios y evitar accesos no autorizados.

## Escenario de calidad

Fuente: Usuario o posible atacante  
Estímulo: Intento de acceso al sistema  
Ambiente: Sistema en producción  
Artefacto: Sistema de autenticación  
Respuesta: Validar credenciales del usuario  
Medida: Acceso permitido únicamente con credenciales válidas

## Issue sugerido

**RNF-02 Implementar seguridad en autenticación**

### Descripción
El sistema debe proteger las credenciales de los usuarios mediante mecanismos de seguridad.

### Criterios de aceptación

- Contraseñas cifradas
- Validación segura del login
- Manejo adecuado de sesiones de usuario

---

# 3. Usabilidad

## Descripción
El sistema debe ser fácil de utilizar para los usuarios.

## Escenario de calidad

Fuente: Usuario nuevo  
Estímulo: Uso del sistema por primera vez  
Ambiente: Interfaz del sistema  
Artefacto: Interfaz gráfica  
Respuesta: El usuario puede navegar sin dificultad  
Medida: El usuario puede realizar tareas básicas sin ayuda externa

## Issue sugerido

**RNF-03 Mejorar usabilidad de la interfaz**

### Descripción
La interfaz del sistema debe ser clara e intuitiva para facilitar su uso.

### Criterios de aceptación

- Navegación clara
- Botones visibles y comprensibles
- Formularios simples de completar

---

# 4. Disponibilidad

## Descripción
El sistema debe estar disponible para los usuarios la mayor parte del tiempo.

## Escenario de calidad

Fuente: Usuario  
Estímulo: Intento de acceso al sistema  
Ambiente: Sistema en producción  
Artefacto: Servidor del sistema  
Respuesta: El sistema responde correctamente  
Medida: Disponibilidad del sistema del 99%

## Issue sugerido

**RNF-04 Garantizar disponibilidad del sistema**

### Descripción
El sistema debe mantenerse disponible para los usuarios durante la mayor parte del tiempo.

### Criterios de aceptación

- El sistema debe estar accesible
- Manejo adecuado de errores
- Recuperación ante fallos simples

---

# 5. Mantenibilidad

## Descripción
El sistema debe permitir modificaciones y mejoras sin afectar otras partes del software.

## Escenario de calidad

Fuente: Desarrollador  
Estímulo: Necesidad de modificar el sistema  
Ambiente: Desarrollo del proyecto  
Artefacto: Código fuente  
Respuesta: Se puede modificar el sistema sin romper otras funcionalidades  
Medida: Cambios aislados en módulos específicos

## Issue sugerido

**RNF-05 Mejorar mantenibilidad del código**

### Descripción
El código del sistema debe estar organizado para facilitar futuras modificaciones.

### Criterios de aceptación

- Código modular
- Separación clara de responsabilidades
- Documentación básica del código

---

# Plantilla para nuevos RNF

Se recomienda usar el siguiente formato para crear nuevos requisitos no funcionales.

```
RNF-XX Nombre del atributo

Descripción
Explicación del requisito no funcional.

Escenario de calidad
Fuente:
Estímulo:
Ambiente:
Artefacto:
Respuesta:
Medida:

Criterios de aceptación
- criterio 1
- criterio 2
- criterio 3
```

---

# Relación con el Proyecto

Cada **feature del sistema** debe indicar qué atributos de calidad afecta.  
Esto permite evaluar el impacto técnico de cada funcionalidad antes de su implementación.

Ejemplo:

Feature: Sistema de login

Atributos de calidad relacionados:

- Seguridad
- Rendimiento
- Disponibilidad
