**RNF-04 — Arquitectura en capas (Módulo  de BD “Mis Eventos”)** 

1. **Descripción** 

El sistema implementará una arquitectura en capas basada en Controller, Service y Repository, extendida a presentación, lógica de negocio, acceso a datos e infraestructura. 

El módulo “Mis Eventos” será diseñado bajo esta estructura para garantizar mantenibilidad, escalabilidad y bajo acoplamiento.![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.001.png)

2. **Definición de capas** 
1. **Capa de Presentación (Controller)** 

Responsable de manejar las solicitudes del usuario. **Responsabilidades:** 

- Recibir solicitudes HTTP (GET, POST, PUT, DELETE)  
- Validar datos básicos  
- Invocar la capa Service  
- Retornar respuestas  ![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.002.png)
2. **Capa de Lógica de Negocio (Service)** Contiene las reglas del sistema. **Responsabilidades:** 
- Validaciones de negocio  
- Procesamiento de datos ![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.003.png)
3. **Capa de Acceso a Datos (Repository)** Gestiona la interacción con la base de datos. **Responsabilidades:** 
- Operaciones CRUD![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.004.png)
4. **Capa de Infraestructura** 

Incluye la configuración técnica del sistema. **Responsabilidades:** 

- Conexión a base de datos  
- ORM   ![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.005.png)
3. **Flujos del sistema** 

**Consulta de eventos:** 

Controller → Service → Repository → Base de datos → Respuesta 

**Creación de evento:** 

Controller → Service → Repository → Base de datos → Respuesta 

**Actualización de evento:** 

Controller → Service → Repository → Base de datos ![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.006.png)

4. **Diagrama de capas** 

Presentación ↓ 

Service 

↓ 

Repository 

↓ 

Base de Datos 

**Regla:** Cada capa solo puede comunicarse con la capa inferior inmediata.![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.007.png)

5. **Persistencia de datos Estrategia:** Uso de ORM  **Patrones:** 
- Repository: desacopla acceso a datos ![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.008.png)
6. **Lineamientos para nuevas funcionalidades Reglas:** 
- No acceder a la base de datos desde Controller 
- No incluir lógica de negocio en Repository  
- No mezclar responsabilidades 

**Flujo:** 

1. Controller  
1. Service  
1. Repository  ![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.009.png)
7. **Convenciones de base de datos Tablas:** 
- eventos  
- usuarios  
- eventos\_usuarios  

**Columnas:** 

- snake\_case (ej. fecha\_inicio)  

**IDs:** 

- Enteros  ![](Aspose.Words.9ab29137-7834-40a8-aaf8-05660c534e56.010.png)
8. **Beneficios** 
- Separación de responsabilidades 
- Mantenibilidad  
- Escalabilidad  
- Facilidad de pruebas  
- Reducción de deuda técnica 
