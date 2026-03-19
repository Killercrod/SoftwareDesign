# Asignación de Criterios de Calidad a Requisitos No Funcionales (ECFCA)

## RNF-01: Autenticación basada en tokens

| Campo | Descripción |
| :--- | :--- |
| **Criterio de Calidad Asignado** | **Seguridad** |
| **Justificación** | Este requisito protege la integridad y confidencialidad de las sesiones de usuario mediante tokens JWT. Garantiza que la información sensible no sea accesible por personas no autorizadas y limita el tiempo de uso cuando no hay actividad, cumpliendo directamente con la definición de seguridad del glosario como medidas para proteger datos y usuarios. |

## RNF-02: Carga de archivos

| Campo | Descripción |
| :--- | :--- |
| **Criterio de Calidad Asignado** | **Rendimiento** |
| **Justificación** | Establece límites de tamaño de archivo (5 MB) para asegurar una experiencia fluida durante operaciones pesadas. Minimiza el consumo innecesario de recursos computacionales y evita sobrecargas en el servidor, alineándose con la definición de rendimiento que incluye el uso eficiente de recursos y la minimización de su consumo innecesario. |

## RNF-03: Recuperación del módulo Mis Eventos

| Campo | Descripción |
| :--- | :--- |
| **Criterio de Calidad Asignado** | **Disponibilidad y Tolerancia a fallos** |
| **Justificación** | Busca reducir el tiempo durante el cual el módulo no está disponible y permite que el sistema continúe funcionando o se recupere rápidamente tras una falla. Esto corresponde directamente con las definiciones de disponibilidad (tiempo operativo) y tolerancia a fallos (capacidad de recuperación ante errores internos o interrupciones). |

## RNF-04: Arquitectura en capas

| Campo | Descripción |
| :--- | :--- |
| **Criterio de Calidad Asignado** | **Mantenibilidad y Arquitectura** |
| **Justificación** | La separación de capas (Controller, Service, Repository) facilita el mantenimiento del código y permite modificar la lógica de negocio sin afectar otras partes del sistema. Cumple con la definición de arquitectura como estructura fundamental y de mantenibilidad como la facilidad para modificar el sistema para corregir errores o adaptarse a nuevos requisitos. |

## RNF-05: Consistencia de interfaz

| Campo | Descripción |
| :--- | :--- |
| **Criterio de Calidad Asignado** | **Usabilidad** |
| **Justificación** | Mantiene un diseño uniforme que permite a los usuarios identificar acciones de forma consistente y adapta el sistema al flujo de trabajo del usuario. Esto se alinea con la definición de usabilidad como la facilidad para aprender y utilizar el sistema efectivamente, manteniendo errores manejables. |

## RNF-06: Validación de formularios

| Campo | Descripción |
| :--- | :--- |
| **Criterio de Calidad Asignado** | **Usabilidad y Seguridad** |
| **Justificación** | Evita el registro de datos incompletos manteniendo errores manejables para el usuario (Usabilidad). Simultáneamente, la validación en cliente y servidor protege la integridad de los datos almacenados, evitando la entrada de información corrupta o malformada (Seguridad/Integridad). |

## RNF-07: Tiempo de procesamiento de acciones

| Campo | Descripción |
| :--- | :--- |
| **Criterio de Calidad Asignado** | **Rendimiento** |
| **Justificación** | Garantiza tiempos de respuesta aceptables para las operaciones principales (registro, actualización, eliminación) bajo condiciones normales de carga. Esto corresponde directamente con la definición de rendimiento referida a la capacidad del sistema para responder dentro de un tiempo aceptable. |

## RNF-08: Validación del formato de correo electrónico

| Campo | Descripción |
| :--- | :--- |
| **Criterio de Calidad Asignado** | **Seguridad y Usabilidad** |
| **Justificación** | Previene el almacenamiento de datos con formato incorrecto protegiendo la integridad de la información de contacto (Seguridad). También mejora la experiencia del usuario al mostrar mensajes claros sobre errores de formato antes de guardar, facilitando la corrección inmediata (Usabilidad). |

## RNF-09: Identificador único de capacitador

| Campo | Descripción |
| :--- | :--- |
| **Criterio de Calidad Asignado** | **Seguridad e Integridad de datos** |
| **Justificación** | Asegura la identificación correcta y única de cada usuario dentro del sistema y en la base de datos. La unicidad del identificador garantiza la integridad de los datos, previniendo duplicaciones que podrían comprometer la confidencialidad o la trazabilidad de la información, elementos clave de la seguridad. |
