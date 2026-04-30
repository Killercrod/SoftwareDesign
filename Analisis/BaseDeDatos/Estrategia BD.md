> ESTRATEGIA DE GESTION DE BASE DE DATOS
>
> **1.** **Objetivo**
>
> Establecer una estrategia robusta para gestionar los cambios en la
> base de datos del sistema, permitiendo la evolución del esquema de
> manera**incremental,** **reversible** **y** **automatizada**, alineada
> con la arquitectura en capas definida (Controller → Service →
> Repository → Base de datos) .
>
> Esta estrategia asegura el cumplimiento del requisito no funcional de
> **modificabilidad**, permitiendo adaptar la base de datos a nuevos
> requerimientos sin afectar otras capas del sistema.
>
> **2.** **Enfoque** **de** **Migraciones**
>
> Se adopta un enfoque de **migraciones** **basadas** **en** **código**,
> utilizando scripts versionados en Python para gestionar los cambios en
> MongoDB.
>
> Dado que MongoDB esuna base de datos NoSQL con esquema flexible, se
> implementa un sistema de migracionescontrolado que permite mantener
> trazabilidad, control yconsistencia en los cambios estructurales.
>
> **3.** **Integración** **con** **la** **Arquitectura** **en**
> **Capas**
>
> La estrategia de migraciones respeta la arquitectura en capas del
> sistema:
>
> • **Capa** **de** **Presentación** **(Controller):**No interactúa con
> la base de datos ni con migraciones
>
> • **Capa** **de** **Lógica** **de** **Negocio** **(Service):**Define
> reglas de negocio sin gestionar cambios estructurales
>
> • **Capa** **de** **Acceso** **a** **Datos** **(Repository):**Refleja
> los cambios en la estructura de la base de datos
>
> • **Capa** **de** **Infraestructura:**Responsable de la ejecución,
> configuración y gestión de migraciones
>
> Se mantiene la regla de que cada capa solo puede comunicarse con su
> capa inferior inmediata, evitando acoplamiento y mejorando la
> mantenibilidad .
>
> **4.** **Estrategia** **de** **Versionado**
>
> Las migraciones se gestionan mediante archivos versionados de forma
> secuencial.
>
> Cada migración representa un cambio específico en la base de datos y
> se identifica mediante:
>
> • Un número de versión incremental
>
> • Una descripción clara del cambio
>
> Esto permite:
>
> • Mantener un historial completo de modificaciones
>
> • Facilitar el trabajo colaborativo
>
> • Controlarla evolución del esquema
>
> **5.** **Convenciones** **de** **Migración**
>
> Se establecen las siguientes reglas:
>
> • Las migraciones son **inmutables**una vez aplicadas
>
> • Se adopta un enfoque de migraciones**solo** **hacia** **adelante**
>
> • Cada migración debe ser reversible mediante un mecanismo controlado
>
> • No se deben modificarmigraciones ya ejecutadas en ningún entorno
>
> • Los cambios deben ser pequeños, claros y específicos
>
> Estas convenciones garantizan estabilidad, trazabilidad ycontrol de
> versiones.
>
> **6.** **Ejecución** **de** **Migraciones**
>
> Las migraciones se ejecutan mediante un proceso automatizado que:
>
> • Detecta cambios pendientes
>
> • Aplica migraciones en orden secuencial
>
> • Registra el estado actual de la base de datos
>
> El sistema también permite revertir cambios en caso de errores,
> asegurando la integridad de la información.
>
> **7.** **Integración** **en** **CI/CD**
>
> Las migraciones se integran dentro del pipeline de integración y
> despliegue continuo.
>
> Durante el proceso de despliegue:
>
> 1\. Se construye el sistema
>
> 2\. Se ejecutan pruebas automatizadas
>
> 3\. Se aplican las migraciones pendientes
>
> 4\. Se despliega la aplicación
>
> Esto asegura que la base de datos esté sincronizada con la versión del
> sistema en todo momento.
>
> **8.** **Manejo** **de** **Entornos**
>
> Se contemplan múltiples entornos de ejecución:
>
> • Desarrollo (dev)
>
> • Pruebas (staging)
>
> Cada entorno cuenta con:
>
> • Configuración específica
>
> • Control de versiones de migraciones
>
> **9.** **Proceso** **de** **Trabajo** **del** **Equipo**
>
> El flujo de trabajo para la gestión de migraciones es:
>
> 1\. Crear una nueva migración con una descripción clara
>
> 2\. Implementar los cambios necesarios
>
> 3\. Probar en entorno de desarrollo
>
> 4\. Validar en entorno de staging
>
> 5\. Integrar al repositorio principal
>
> Este proceso reduce errores y asegura consistencia entre entornos.
>
> **10.** **Validación** **de** **Migraciones**
>
> Antes de aplicar una migración en producción, se debe verificar:
>
> • Correcta aplicación del cambio
>
> • Integridad de los datos existentes
>
> • Compatibilidad con la lógica del sistema
>
> • Posibilidad de reversión sin pérdida de información
