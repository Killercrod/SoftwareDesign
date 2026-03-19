## Requerimientos Funcionales y Casos de Uso

**RF-01 (Gestión de Perfil):** El sistema permitirá al usuario iniciar sesión y gestionar sus datos personales.

CU-001: Iniciar Sesión y Gestionar Datos
Actores: Usuario
Descripción: El usuario deberá registrarse con su correo y contraseña además de poder entrar a la configuración de su perfil, ver y gestionar sus datos personales.
Pre-Condiciones: El usuario ya debe tener una cuenta creada.
Flujo básico:
1. El usuario accede a la página de inicio de sesión del sistema.  
2. El sistema muestra una interfaz solicitando el correo electrónico del usuario.
3. El sistema valida que la dirección de correo electrónico existe en la base de datos de usuarios.
4. El sistema genera un código de acceso temporal al correo del usuario.
5. El sistema solicita el código de acceso.
6. El usuario ingresa el código que recibió en su correo.
7. El sistema valida que el código coincida con el enviado y no haya expirado.
8. El sistema debe tener un botón para poder consultar el perfil del usuario con sus datos personales.
9. El usuario podrá modificar alguno de los datos en que caso de que lo desee.

Flujo de Excepciones:
1. Correo electrónico no válido.
2. Código de acceso temporal incorrecto.
3. Código de acceso expirado.

- Issue #001: (Backend): Crear endpoint unificado de registro/login, recibe email y contraseña.

- Issue #002: (Backend): Crear endpoint para obtener perfil del usuario autenticado, requiere token válido. 

- Issue #003: (Frontend): Crear vista de perfil de usuario que muestre: email, nombre, teléfono.

- Issue #004: (Frontend): Implementar modo edición en vista de perfil con formulario para editar los datos del usuario.


**RF-02 (Solicitud de Inscripción):** El sistema permitirá al usuario seleccionar un evento en la sección de “Eventos Disponibles”, mostrar información clave (nombre, fechas, breve descripción, precio, estado de solicitud, etc.) y enviar una solicitud de inscripción (CU-PG-004).

CU-02: Seleccionar Evento y Enviar Solicitud de Inscripción.
Actores: Usuario
Descripción: El usuario podrá navegar entre los distintos eventos que oferta la plataforma, revisar detalles sobre los eventos de su interés y enviar una solicitud de inscripción al evento seleccionado.
Pre-Condiciones: El usuario debe haberse registrado en el sistema con su correo y contraseña para acceder a la plataforma.
Flujo básico:
1. El usuario entra a la sección de Eventos Disponibles
2. El sistema muestra la lista de los distintos eventos
3. El usuario podrá navegar entre la lista de eventos disponibles
4. El usuario podrá acceder a información como nombre, fechas, descripción, precio.
5. El usuario podrá enviar una solicitud de inscripción a través del botón inscribirse.
6. El usuario rellenará los datos del formulario.
7. El sistema valida los datos.
8. El sistema muestra mensaje de confirmación de recibida la solicitud.

Flujo de Excepciones:
1. No hay cupo en el evento.
2. El usuario ya está inscrito.
3. Datos inválidos en el formulario.
4. Formulario de inscripción incompleto.

- Issue #001: (Backend): Listar los eventos disponibles con su campo requerido (id, nombre, fecha_inicio, fecha_fin, descripción_breve, precio, estado_solicitud_usuario).

- Issue #002: (Backend): Obtener el detalle específico de un evento seleccionado, recibe evento_id y devuelve información completa del evento.

- Issue #003: (Backend):  Generar un formulario de inscripción para el usuario con los datos necesarios.

- Issue #004 (Frontend): Crear sección "Eventos Disponibles".

- Issue #005 (Frontend): Vista de detalle de evento.

- Issue #006 (Frontend): Acción "Inscribirse" desde lista o detalle.

**RF-03 (Carga de Documentación)**: El sistema permitirá subir archivos digitalizados asociados a una solicitud como parte del proceso de solicitud o cuando un administrativo solicita información adicional para una solicitud existente (CU-PG-006).

CU-03: Carga de Documentación.
Actores: Usuario.
Pre-Condiciones: El usuario debe haberse inscrito al evento de su interés.
Flujo Básico:
1. El sistema despliega un listado de documentos necesarios que el usuario debe subir.
2. El usuario debe seleccionar debe seleccionar el botón de Cargar Documento.
3. El usuario debe seleccionar el archivo correspondiente en su explorador de archivos confirmando la subida.
4. El sistema envía el archivo al backend, verificando su autenticidad y que sea formato correcto.
5. El sistema despliega el mensaje de Subido Correctamente.

Flujo de Excepciones:
1. Tipo de archivo no permitido.
2. El tamaño del archivo es excedido.
3. Cancelación de la subida por parte del usuario.

- Issue #001: (Backend): Crear endpoint para obtener documentos requeridos de una solicitud, Validar que la solicitud existe y pertenece al usuario autenticado.

- Issue #002: (Backend): Crear endpoint para subir documento, Validar solicitud existe y pertenece al usuario.

- Issue #003: (Backend): Crear endpoint para verificar documentos completos de una solicitud, comparar documentos obligatorios del evento contra los ya subidos.

- Issue #003: (Backend): Implementar manejo de excepción para formato de archivo no permitido. 

- Issue #004: (Frontend): Crear componente reutilizable "CargarDocumento" que incluya: input file con validación en cliente de formato y tamaño.

- Issue #005: (Frontend): Implementar notificación de carga exitosa mediante toast o mensaje temporal: "Documento cargado exitosamente".

- Issue #006: (Frontend): Implementar cancelación de carga con botón "Cancelar" que interrumpa la subida, no guarde nada y retorne al estado anterior sin cambios.


 
RF-04 (Consulta de Estatus):
El sistema mostrará una lista consolidada con el estado de solicitudes y pagos del usuario autenticado.
CU-PG-007: Consultar Estatus de Solicitudes
Actores: Usuario
Descripción: El usuario podrá visualizar una lista de sus solicitudes que incluya en ella: su estado actual, detalles descriptivos de cada una, documentos y estado de pago
Pre-Condiciones: El usuario debe haber iniciado sesión y contar con al menos una solicitud registrada.

Flujo básico:
1.	El usuario accede a la sección "Mis Solicitudes".
2.	El sistema muestra una lista de solicitudes del usuario.
3.	Cada solicitud incluye su estado (pendiente, aprobada, rechazada, en revisión).
4.	El usuario selecciona una solicitud específica.
5.	El sistema muestra el detalle completo de la solicitud (el detalle incluye información del evento asociado)
6.	El sistema muestra el estado de los documentos requeridos y cargados.
7.	El sistema muestra el estado de pago de la solicitud.

Flujo de Excepciones:
1.	No existen solicitudes registradas para el usuario.
2.	Error al obtener la información de las solicitudes.
3.	Solicitud no encontrada.

Issues:

•	Issue #001 (Backend): Crear endpoint para listar las solicitudes del usuario autenticado con su estado actual (pendiente, aprobada, rechazada, en revisión).

•	Issue #002 (Backend): Crear endpoint para obtener el detalle de una solicitud específica, incluyendo estado de documentos y estado de pago.

•	Issue #003 (Frontend): Crear vista de "Mis Solicitudes" que muestre una lista de las solicitudes del usuario con su estado y evento asociado.

•	Issue #004 (Frontend): Crear vista de detalle de solicitud donde se muestre información completa (evento, estado de solicitud, documentos requeridos, documentos cargados y estado de pago).



RF-05 (Reenvío de Solicitudes):
El sistema permitirá editar y reenviar solicitudes rechazadas o con información incompleta.
CU-PG-008: Reenviar Solicitud
Actores: Usuario
Descripción: El usuario podrá editar una solicitud previamente rechazada o incompleta y reenviarla para su validación.
Pre-Condiciones: El usuario debe haber iniciado sesión y contar con una solicitud en estado "rechazada" o "información incompleta".

Flujo básico:
1.	El usuario accede a la sección "Mis Solicitudes".
2.	El sistema muestra la lista de solicitudes.
3.	El usuario selecciona una solicitud con estado editable.
4.	El sistema muestra el detalle de la solicitud.
5.	El usuario selecciona la opción "Editar solicitud".
6.	El sistema despliega un formulario con los datos actuales.
7.	El usuario modifica los campos necesarios.
8.	El usuario envía la solicitud actualizada.
9.	El sistema valida la información ingresada.
10.	El sistema actualiza la solicitud y cambia su estado a "en revisión".
    
Flujo de Excepciones:
1.	La solicitud no se encuentra en un estado editable.
2.	Error en la validación de datos.
3.	Error al actualizar la solicitud.
   
Issues:

•	Issue #001 (Backend): Crear endpoint para actualizar una solicitud existente cuando su estado sea "rechazada" o "información incompleta".

•	Issue #002 (Backend): Validar que la solicitud a editar pertenezca al usuario autenticado y que su estado permita modificaciones.

•	Issue #003 (Frontend): Implementar opción "Editar solicitud" en solicitudes rechazadas o incompletas desde la vista de detalle.

•	Issue #004 (Frontend): Implementar formulario de edición que permita modificar los campos necesarios y reenviar la solicitud.

•	Issue #005 (Frontend): Mostrar notificación de confirmación cuando la solicitud sea reenviada exitosamente.



RF-06 (Acceso a Contenido):
El sistema permitirá visualizar los detalles y recursos de los eventos confirmados.
CU-PG-009: Acceder a Contenido de Eventos
Actores: Usuario
Descripción: El usuario podrá acceder a los eventos en los que ha sido aprobado, visualizando sus detalles y recursos disponibles.
Pre-Condiciones: El usuario debe haber iniciado sesión y contar con una solicitud aprobada para al menos un evento.

Flujo básico:
1.	El usuario accede a la sección "Mis Eventos".
2.	El sistema muestra la lista de eventos confirmados del usuario.
3.	El usuario selecciona un evento.
4.	El sistema valida que el usuario tenga acceso al evento.
5.	El sistema muestra el detalle del evento.
6.	El sistema muestra los recursos disponibles del evento.
7.	El sistema muestra materiales asociados al evento.
   
Flujo de Excepciones:
1.	El usuario no tiene eventos confirmados.
2.	El usuario intenta acceder a un evento sin aprobación.
3.	Error al cargar los recursos del evento.
   
Issues:

•	Issue #001 (Backend): Crear endpoint para obtener los recursos y detalles de un evento al que el usuario esté inscrito y aprobado.

•	Issue #002 (Backend): Validar que el usuario tenga una solicitud aprobada para el evento antes de permitir el acceso a su contenido.

•	Issue #003 (Frontend): Crear sección "Mis Eventos" que liste los eventos confirmados del usuario.

•	Issue #004 (Frontend): Crear vista de detalle del evento que muestre información, recursos disponibles y materiales asociados.

