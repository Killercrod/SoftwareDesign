**Refinamiento y desglose de RNF** 

**RNF-01 — Autenticación basada en tokens**

**Descripción** 

El sistema deberá utilizar autenticación mediante **tokens JWT** para validar las sesiones de los usuarios.

**Propósito** 

Controlar el acceso al sistema mediante sesiones verificables y limitar el tiempo de uso cuando no existe actividad.

**Criterios de cumplimiento** 

- El sistema generará un **token JWT** después de que el usuario inicie sesión correctamente. 
- El token deberá expirar después de **30 minutos sin actividad del usuario**. 
- Cuando el token expire, el sistema deberá redirigir al usuario a la pantalla de inicio de sesión. 
- El token deberá enviarse en cada solicitud al servidor para validar la sesión.

**Impacto en el sistema** 

- Requiere implementar un **mecanismo de generación y validación de tokens**. 
- Reduce el uso de sesiones almacenadas en el servidor.

**RNF-02 — Carga de archivos** 

**Descripción** 

El sistema deberá permitir subir documentos asociados a los usuarios.

**Propósito** 

Permitir que los usuarios carguen documentos necesarios para validación o registro dentro del sistema. 

**Criterios de cumplimiento** 

- El sistema deberá aceptar archivos con un tamaño **menor o igual a 5 MB**. 
- Si el archivo supera el límite de 5 MB, el sistema deberá rechazar la carga y mostrar un mensaje de error.
- El sistema deberá completar la carga del archivo en un tiempo máximo de **10 segundos** en condiciones de red normales.

**Impacto en el sistema** 

- Requiere configurar límites de tamaño en el servidor o backend.
- Se debe implementar validación del tamaño del archivo antes de guardarlo.
- Se requiere espacio de almacenamiento para los documentos.

**RNF-03 — Recuperación del módulo Mis Eventos** 

**Descripción** 

El sistema deberá permitir restablecer la funcionalidad del módulo **Mis Eventos** después de una falla. 

**Propósito** 

Reducir el tiempo durante el cual el módulo no está disponible.

**Criterios de cumplimiento** 

- El módulo **Mis Eventos** deberá volver a estar disponible en un tiempo máximo de **5 minutos** después de una falla del sistema o reinicio del servidor.
- Después de la recuperación, el módulo deberá permitir nuevamente:
- consulta de eventos 
- visualización de información de eventos

**Impacto en el sistema** 

- Requiere que el sistema pueda reiniciarse sin configuraciones manuales complejas. 
- Se debe mantener la configuración del sistema almacenada para permitir reinicio rápido. 

**RNF-04 — Arquitectura en capas** 

**Descripción** 

El sistema deberá implementar una arquitectura en capas compuesta por **Controller, Service y Repository**. 

**Propósito** 

Separar la lógica de presentación, la lógica de negocio y el acceso a datos.

**Criterios de cumplimiento** 

El sistema deberá cumplir las siguientes reglas de estructura:

- **Controller** 
- Manejar solicitudes HTTP del usuario. 
- Invocar métodos del Service. 
- **Service** 
- Contener la lógica de negocio del sistema.
- Procesar las operaciones antes de acceder a los datos.
- **Repository** 
- Gestionar las operaciones de lectura y escritura en la base de datos.

**Impacto en el sistema** 

- Facilita el mantenimiento del código.
- Permite modificar la lógica de negocio sin cambiar la capa de acceso a datos.
- Requiere organizar el proyecto en carpetas o módulos separados.

**RNF-05 — Consistencia de interfaz** 

**Descripción** 

Las pantallas del Módulo de Usuarios deberán mantener un diseño uniforme.

**Propósito** 

Permitir que los usuarios identifiquen las acciones del sistema de forma consistente.

**Criterios de cumplimiento** 

- Todas las pantallas del Módulo de Usuarios deberán incluir el **mismo menú principal**. 


- Los botones de acciones deberán utilizar las mismas etiquetas en todas las pantallas: 
- Crear 
- Guardar 
- Cancelar 
- Eliminar 

**Impacto en el sistema** 

- Requiere definir una **plantilla o componente reutilizable de interfaz**. 
- Reduce cambios de diseño entre pantallas.

**RNF-06 — Validación de formularios** 

**Descripción** 

Los formularios de registro y edición deberán validar la información antes de almacenarla. 

**Propósito** 

Evitar el registro de datos incompletos en el sistema.

**Criterios de cumplimiento** 

- El sistema deberá verificar que los **campos obligatorios no estén vacíos**. 
- Si un campo obligatorio está vacío, el sistema deberá mostrar un mensaje indicando el campo que requiere información.
- El sistema no deberá guardar el registro hasta que todos los campos obligatorios estén completos.

**Impacto en el sistema** 

- Requiere validaciones tanto en el **cliente** como en el **servidor**. 
- Reduce errores en los datos almacenados.

**RNF-07 — Tiempo de procesamiento de acciones**

**Descripción** 

El sistema deberá ejecutar las operaciones principales dentro de un tiempo definido.

**Propósito** 

Garantizar tiempos de respuesta aceptables para los usuarios.

**Criterios de cumplimiento** 

Las siguientes acciones deberán completarse en **3 segundos o menos**: 

- registrar usuario 
- actualizar información de usuario
- eliminar usuario 
- archivar usuario 

La medición se realizará desde el momento en que el usuario envía el formulario hasta que el sistema muestra el mensaje de confirmación.

**Impacto en el sistema** 

- Requiere consultas optimizadas a la base de datos.

**RNF-08 — Validación del formato de correo electrónico (institucional)** 

**Descripción** 

El sistema deberá verificar el formato del correo electrónico antes de guardar un registro. 

**Propósito** 

Evitar el almacenamiento de correos electrónicos con formato incorrecto.

**Criterios de cumplimiento** 

El sistema deberá verificar que el correo electrónico:

- contenga el carácter **@** 
- contenga un **dominio después del símbolo @**

Si el correo no cumple estas condiciones, el sistema deberá mostrar un mensaje indicando formato inválido. 

**Impacto en el sistema** 


- Requiere validación en el formulario de registro y edición.
- Reduce errores en datos de contacto.

**RNF-09 — Identificador único de usuario** 

**Descripción** 

El sistema deberá asignar un identificador numérico único a cada usuario registrado.

**Propósito** 

Permitir la identificación de cada usuario dentro del sistema y en la base de datos.

**Criterios de cumplimiento** 

- El identificador deberá ser un **valor numérico entero**. 
- El identificador no deberá repetirse entre usuarios.
- El identificador deberá generarse automáticamente al crear un nuevo usuario.

**Impacto en el sistema** 

- Requiere un campo de identificador en la base de datos.
- El identificador deberá utilizarse para realizar operaciones de consulta, actualización o eliminación de usuarios.
