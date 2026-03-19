# Atributos de Calidad del Sistema

Este documento define los atributos de calidad del sistema, los cuales forman parte de los Requisitos No Funcionales (RNF).

Los atributos de calidad describen cómo debe comportarse el sistema y se basan en el modelo de calidad definido por el estándar ISO/IEC 25010.

---

## 1. Rendimiento (Performance)

**Descripción**

El sistema debe responder a las solicitudes de los usuarios en un tiempo adecuado para garantizar una buena experiencia.

**Escenario de calidad**

| Campo | Descripción |
|-------|-------------|
| Fuente | Usuario |
| Estímulo | Solicitud de una acción dentro del sistema |
| Ambiente | Uso normal del sistema |
| Artefacto | Servidor o aplicación |
| Respuesta | El sistema procesa la solicitud |
| Medida | Tiempo de respuesta menor a 2 segundos |

### RNF-02: Carga de archivos
**Descripción**

El sistema debe gestionar la carga de archivos estableciendo límites de tamaño para evitar sobrecargas en el servidor.

**Criterios de aceptación**

- Límite de tamaño configurado en 5 MB
- Validación del tamaño ocurre antes de iniciar la transferencia completa
- El servidor no consume recursos excesivos con archivos grandes

### RNF-07: Tiempo de procesamiento de acciones
**Descripción**

El sistema debe garantizar tiempos de respuesta aceptables para las operaciones principales (registro, actualización, eliminación) bajo condiciones normales de carga.

**Criterios de aceptación**

- Tiempo de respuesta promedio menor a 2 segundos para el 95% de las peticiones
- Pruebas de carga realizadas con usuarios simulados
- Sin tiempos de espera excesivos (spinners infinitos)

---

## 2. Seguridad

**Descripción**

El sistema debe proteger la información de los usuarios y evitar accesos no autorizados.

**Escenario de calidad**

| Campo | Descripción |
|-------|-------------|
| Fuente | Usuario o posible atacante |
| Estímulo | Intento de acceso al sistema |
| Ambiente | Sistema en producción |
| Artefacto | Sistema de autenticación |
| Respuesta | Validar credenciales del usuario |
| Medida | Acceso permitido únicamente con credenciales válidas |

### RNF-01: Autenticación basada en tokens
**Descripción**

El sistema debe proteger las credenciales de los usuarios mediante mecanismos de seguridad como tokens JWT.

**Criterios de aceptación**

- Los tokens JWT tienen una fecha de expiración definida
- El sistema rechaza solicitudes con tokens manipulados o caducados
- Las sesiones se invalidan correctamente al cerrar sesión

### RNF-06: Validación de formularios
**Descripción**

La validación en cliente y servidor protege la integridad de los datos almacenados, evitando la entrada de información corrupta o malformada.

**Criterios de aceptación**

- Validación en tiempo real en el cliente
- Validación obligatoria en el servidor
- Mensajes de error descriptivos y amigables

### RNF-08: Validación del formato de correo electrónico
**Descripción**

Previene el almacenamiento de datos con formato incorrecto protegiendo la integridad de la información de contacto.

**Criterios de aceptación**

- Validación de sintaxis en el campo de correo
- Mensaje de error específico indicando el formato correcto
- Prevención de inyección de datos maliciosos vía correo

### RNF-09: Identificador único de capacitador
**Descripción**

Asegura la identificación correcta y única de cada usuario dentro del sistema y en la base de datos.

**Criterios de aceptación**

- Clave primaria única en la tabla de usuarios
- Validación de unicidad antes de insertar registros
- Trazabilidad completa de acciones por ID único

---

## 3. Usabilidad

**Descripción**

El sistema debe ser fácil de utilizar para los usuarios.

**Escenario de calidad**

| Campo | Descripción |
|-------|-------------|
| Fuente | Usuario nuevo |
| Estímulo | Uso del sistema por primera vez |
| Ambiente | Interfaz del sistema |
| Artefacto | Interfaz gráfica |
| Respuesta | El usuario puede navegar sin dificultad |
| Medida | El usuario puede realizar tareas básicas sin ayuda externa |

### RNF-05: Consistencia de interfaz
**Descripción**

La interfaz del sistema debe mantener un diseño uniforme para que los usuarios identifiquen acciones de forma consistente.

**Criterios de aceptación**

- Uso de una librería de componentes unificada
- Mismos patrones de navegación en todas las vistas
- Reducción de errores de usuario por confusión de interfaz

### RNF-06: Validación de formularios
**Descripción**

Evita el registro de datos incompletos manteniendo errores manejables para el usuario.

**Criterios de aceptación**

- Validación en tiempo real en el cliente
- Validación obligatoria en el servidor
- Mensajes de error descriptivos y amigables

### RNF-08: Validación del formato de correo electrónico
**Descripción**

Mejora la experiencia del usuario al mostrar mensajes claros sobre errores de formato antes de guardar.

**Criterios de aceptación**

- Validación de sintaxis en el campo de correo
- Mensaje de error específico indicando el formato correcto
- Facilita la corrección inmediata

---

## 4. Disponibilidad

**Descripción**

El sistema debe estar disponible para los usuarios la mayor parte del tiempo.

**Escenario de calidad**

| Campo | Descripción |
|-------|-------------|
| Fuente | Usuario |
| Estímulo | Intento de acceso al sistema |
| Ambiente | Sistema en producción |
| Artefacto | Servidor del sistema |
| Respuesta | El sistema responde correctamente |
| Medida | Disponibilidad del sistema del 99% |

### RNF-03: Recuperación del módulo Mis Eventos
**Descripción**

El sistema debe mantenerse disponible para los usuarios durante la mayor parte del tiempo y recuperarse rápidamente tras una falla.

**Criterios de aceptación**

- El sistema debe estar accesible
- Manejo adecuado de errores
- Tiempo de recuperación (RTO) menor a 2 minutos tras un fallo crítico

---

## 5. Mantenibilidad

**Descripción**

El sistema debe permitir modificaciones y mejoras sin afectar otras partes del software.

**Escenario de calidad**

| Campo | Descripción |
|-------|-------------|
| Fuente | Desarrollador |
| Estímulo | Necesidad de modificar el sistema |
| Ambiente | Desarrollo del proyecto |
| Artefacto | Código fuente |
| Respuesta | Se puede modificar el sistema sin romper otras funcionalidades |
| Medida | Cambios aislados en módulos específicos |

### RNF-04: Arquitectura en capas
**Descripción**

El código del sistema debe estar organizado para facilitar futuras modificaciones mediante separación de capas (Controller, Service, Repository).

**Criterios de aceptación**

- Código modular
- Separación clara de responsabilidades
- Documentación básica del código
- Las capas no tienen dependencias cíclicas

---

## Resumen de Mapeo RNF a Atributos

| RNF | Atributo(s) de Calidad |
|-----|------------------------|
| RNF-01 | Seguridad |
| RNF-02 | Rendimiento |
| RNF-03 | Disponibilidad |
| RNF-04 | Mantenibilidad |
| RNF-05 | Usabilidad |
| RNF-06 | Usabilidad, Seguridad |
| RNF-07 | Rendimiento |
| RNF-08 | Seguridad, Usabilidad |
| RNF-09 | Seguridad |
