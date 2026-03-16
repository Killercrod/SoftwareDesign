

**RF-01 (Gestión de Perfil):** El sistema permitirá al usuario iniciar sesión y gestionar sus datos personales.

- Issue #001: (Backend): Crear endpoint unificado de registro/login, recibe email y contraseña.

- Issue #002: (Backend): Crear endpoint para obtener perfil del usuario autenticado, requiere token válido. 

- Issue #003: (Frontend): Crear vista de perfil de usuario que muestre: email, nombre, teléfono.

- Issue #004: (Frontend): Implementar modo edición en vista de perfil con formulario para editar los datos del usuario.


**RF-02 (Solicitud de Inscripción):** El sistema permitirá al usuario seleccionar un evento en la sección de “Eventos Disponibles”, mostrar información clave (nombre, fechas, breve descripción, precio, estado de solicitud, etc.) y enviar una solicitud de inscripción (CU-PG-004).

- Issue #001: (Backend): Listar los eventos disponibles con su campo requerido (id, nombre, fecha_inicio, fecha_fin, descripción_breve, precio, estado_solicitud_usuario).

- Issue #002: (Backend): Obtener el detalle específico de un evento seleccionado, recibe evento_id y devuelve información completa del evento.

- Issue #003: (Backend):  Generar un formulario de inscripción para el usuario con los datos necesarios.

- Issue #004 (Frontend): Crear sección "Eventos Disponibles".

- Issue #005 (Frontend): Vista de detalle de evento.

- Issue #006 (Frontend): Acción "Inscribirse" desde lista o detalle.

**RF-03 (Carga de Documentación)**: El sistema permitirá subir archivos digitalizados asociados a una solicitud como parte del proceso de solicitud o cuando un administrativo solicita información adicional para una solicitud existente (CU-PG-006).


- Issue #001: (Backend): Crear endpoint para obtener documentos requeridos de una solicitud, Validar que la solicitud existe y pertenece al usuario autenticado.

- Issue #002: (Backend): Crear endpoint para subir documento, Validar solicitud existe y pertenece al usuario.

- Issue #003: (Backend): Crear endpoint para verificar documentos completos de una solicitud, comparar documentos obligatorios del evento contra los ya subidos.

- Issue #003: (Backend): Implementar manejo de excepción para formato de archivo no permitido. 

- Issue #004: (Frontend): Crear componente reutilizable "CargarDocumento" que incluya: input file con validación en cliente de formato y tamaño.

- Issue #005: (Frontend): Implementar notificación de carga exitosa mediante toast o mensaje temporal: "Documento cargado exitosamente".

- Issue #006: (Frontend): Implementar cancelación de carga con botón "Cancelar" que interrumpa la subida, no guarde nada y retorne al estado anterior sin cambios.


 
**RF-04 (Consulta de Estatus)**: El sistema mostrará una lista consolidada con el estado de solicitudes y pagos del usuario autenticado (CU-PG-007).

- Issue #001 (Backend): Crear endpoint para listar las solicitudes del usuario autenticado con estado actual (pendiente, aprobada, rechazada, en revisión).

- Issue #002 (Backend): Crear endpoint para obtener el detalle de una solicitud específica, incluyendo estado de documentos y estado de pago.

- Issue #003 (Frontend): Crear vista de "Mis Solicitudes" que muestre una lista de las solicitudes del usuario con su estado y evento asociado.

- Issue #004 (Frontend): Crear vista de detalle de solicitud donde se muestre información completa (evento, estado de solicitud, documentos requeridos, documentos cargados y estado de pago).

**RF-05 (Reenvío de Solicitudes)**: El sistema permitirá editar y reenviar solicitudes rechazadas o con información incompleta (CU-PG-008).

- Issue #001 (Backend): Crear endpoint para actualizar una solicitud existente cuando su estado sea "rechazada" o "información incompleta".

- Issue #002 (Backend): Validar que la solicitud a editar pertenezca al usuario autenticado y que su estado permita modificaciones.

- Issue #003 (Frontend): Implementar opción "Editar solicitud" en solicitudes rechazadas o incompletas desde la vista de detalle.

- Issue #004 (Frontend): Implementar formulario de edición que permita modificar los campos necesarios y reenviar la solicitud.

- Issue #005 (Frontend): Mostrar notificación de confirmación cuando la solicitud sea reenviada exitosamente.

 **RF-06 (Acceso a Contenido)**: El sistema permitirá visualizar los detalles y recursos de los eventos confirmados (CU-PG-009).
- Issue #001 (Backend): Crear endpoint para obtener los recursos y detalles de un evento al que el usuario esté inscrito y aprobado.
- Issue #002 (Backend): Validar que el usuario tenga una solicitud aprobada para el evento antes de permitir el acceso a su contenido.
- Issue #003 (Frontend): Crear sección "Mis Eventos" que liste los eventos confirmados del usuario.
- Issue #004 (Frontend): Crear vista de detalle del evento que muestre información, recursos disponibles y materiales asociados
