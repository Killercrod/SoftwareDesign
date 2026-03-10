**Evaluacion de features de RNF** 

1. Seguridad RNF-S-01  

   Autenticación basada en tokens (JWT) con expiración tras 30 minutos de inactividad. 

   Análisis de rendimiento: cada solicitud requiere validar el token (firma y expiración), generando overhead (peso agregado entre la comunicación y sincronización entre procesos) de procesamiento.

   El sistema debe minimizar el overhead para alcanzar un alto nivel de rendimiento y escalabilidad 

   Análisis de seguridad: al expirar tras 30 minutos de inactividad, reduce la ventana de ataque por sesiones robadas

   Análisis de mantenimiento: será necesario gestionar sincronización de tiempo entre servidores, el impacto en mantenimiento requerirá monitoreo constante de desviaciones de tiempo

2. Rendimiento RNF-R-01 

   Cargas de archivos como comprobantes (hasta 10MB) con barra de progreso asíncrona 

   Análisis de rendimiento: habrá que tener consideración en que los archivos, aunque sean de 10MB consumen ancho de banda y memoria del servidor durante la subida de datos. La concurrencia puede saturar el servidor si varios usuarios suben archivos al mismo tiempo

   Análisis de seguridad: puede haber el riesgo de denegación de servicio por saturación de subidas masivas. Sera necesario validar tipo de contenido y antivirus para evitar malware o scripts malicioso

   Análisis de mantenimiento: requiere de gestión de almacenamiento temporal y definitivo para limpieza de archivos 

3. Disponibilidad RNF-D-01 

   Recuperación del módulo Mis Eventos en máximo 5 minutos (RTO).

   Análisis de rendimiento: los 5 minutos incluyen detección, conmutación y restauración de servicio, limitando estrategias más económicas, es decir, primero el sistema debe detectar automáticamente el fallo, luego, redirigir el trafico al entorno de respaldo (por ejemplo: DNS), y por último, cargar últimos datos, restablecer conexiones y verificar la integridad. Si se usan backups tradicionales (restaurar desde disco), solo la descarga del backup puede exceder los 5 minutos 

   Análisis de seguridad: los backups deben mantener el mismo nivel de cifrado y control de acceso. Puede haber riesgo de exponer datos en la recuperación si no se validan los mecanismos de conmutación 

   Análisis de mantenimiento: obliga a probar el plan de RTO periódicamente mediante simulacros para verificar que se cumpla en la medida de 5 minutos. Sera necesario monitorear continuamente la capacidad de recuperación 

4. Usabilidad (UX) RNF-U-01 

   Mensajes de error estructurados con causa y sugerencia

   Análisis de rendimiento: requiere procesamiento adicional para capturar el contexto, clasificar errores y generar sugerencias, podría aumentar latencia en respuestas de error, especialmente si las sugerencias requieren consultas a BD 

   Análisis de seguridad: las sugerencias deben clasificarse para no revelar estructura de la base de datos o lógica de negocio. Puede haber el riesgo de filtrar información sensible si la causa expone detalles internos

   Análisis de mantenimiento: requiere mantener actualizado el catálogo de errores cuando cambia la lógica de negocio

5. Mantenibilidad RNF-M-01 

   Arquitectura en capas (Controller–Service–Repository). 

   Análisis de rendimiento: cada petición atraviesa múltiples capas, añadiendo overhead por invocaciones de métodos y creación de objetos

   Análisis de seguridad: puede haber el riesgo de implementar controles en capa incorrecta, como una validación solo en controller y no en service. La arquitectura en capas mejora el aislamiento, por lo tanto, la lógica de negocio no accede directamente a datos

   Análisis de mantenimiento: tiene una alta cohesión al tener una separación de responsabilidades facilita modificar una capa sin afectar
