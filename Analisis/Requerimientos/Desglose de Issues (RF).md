## RF-04 – Consulta de Estatus (Issues en prosa)
- **Issue #001 (Backend)** : Listado de solicitudes del usuario, se deberá implementar un endpoint que permita obtener todas las solicitudes asociadas al usuario autenticado.

  El sistema deberá validar el token de autenticación proporcionado en la petición y extraer el identificador del usuario.

  Una vez validado, el sistema consultará la base de datos para recuperar todas las solicitudes que pertenezcan a dicho usuario, ordenadas por fecha de creación en orden descendente.

  Cada solicitud deberá incluir, como mínimo, el identificador, el nombre del evento asociado, la fecha de registro y el estado actual.

  Los estados deberán manejarse bajo un catálogo controlado: pendiente, en revisión, aprobada y rechazada.

  En caso de que el token sea inválido o no se proporcione, el sistema deberá rechazar la petición con un error de autenticación.


- **Issue #002 (Backend)** : Consulta de detalle de solicitud

  Se deberá implementar un endpoint que permita obtener el detalle completo de una solicitud específica.
  
  El sistema deberá validar que la solicitud solicitada exista y que pertenezca al usuario autenticado. En caso contrario, deberá retornar un error de autorización o de recurso no encontrado, según corresponda.
  
  El detalle deberá incluir:
  
    • 	Información del evento asociado
    
    • 	Estado actual de la solicitud
    
    • 	Listado de documentos requeridos
    
    • 	Indicador de documentos cargados por el usuario
    
    • 	Estado del pago asociado
    
  La información deberá entregarse de forma estructurada, permitiendo al frontend identificar claramente qué elementos están completos y cuáles pendientes.

- **Issue #003 (Frontend)** : Vista de listado de solicitudes

  Se deberá desarrollar una interfaz denominada “Mis Solicitudes”, en la cual se mostrará un listado de todas las solicitudes del usuario.

  La vista deberá consumir el endpoint correspondiente y presentar la información en un formato claro (tabla o tarjetas), mostrando al menos el nombre del evento, la fecha y el estado de cada solicitud.

  Cada elemento de la lista deberá ser interactivo, permitiendo al usuario acceder al detalle de la solicitud seleccionada.


- **Issue #004 (Frontend)** : Vista de detalle de solicitud

  Se deberá implementar una vista que muestre la información completa de una solicitud.

  Esta vista deberá consumir el endpoint de detalle y presentar:

  •	Información general del evento

  •	Estado de la solicitud

  •	Estado de cada documento requerido (cargado o pendiente)

  •	Estado del pago

  La interfaz deberá permitir al usuario identificar fácilmente el progreso de su solicitud.


## RF-05 – Reenvío de Solicitudes (Issues en prosa)
- Issue #001 (Backend): Actualización de solicitudes

  Se deberá implementar un endpoint que permita actualizar una solicitud existente.
  
  El sistema deberá validar que:
  
  1.	La solicitud pertenezca al usuario autenticado
  
  2.	El estado actual de la solicitud permita modificaciones
  
  Únicamente se permitirá la edición de solicitudes en estado rechazada o información incompleta.
  
  Una vez validado, el sistema actualizará los datos proporcionados y cambiará automáticamente el estado de la solicitud a en revisión.
  

- Issue #002 (Backend): Validación de reglas de edición

  Se deberá implementar una validación estricta que impida la modificación de solicitudes que no cumplan con las condiciones establecidas, si la solicitud no pertenece al usuario o su estado no es editable, el sistema deberá rechazar la operación con un error de autorización.
  Esta validación deberá ejecutarse antes de cualquier modificación en la base de datos.

- Issue #003 (Frontend): Opción de edición de solicitud

  En la vista de detalle de la solicitud, se deberá mostrar la opción “Editar solicitud” únicamente cuando el estado de la misma sea rechazada o información incompleta.
  
  Esta opción deberá redirigir al usuario a una vista de edición.

- Issue #004 (Frontend): Formulario de edición

  Se deberá implementar un formulario que permita al usuario modificar los datos previamente registrados en la solicitud.
  
  El formulario deberá cargarse con la información existente y validar que:
  
  •	Los campos obligatorios no estén vacíos
  
  •	Los documentos requeridos sean proporcionados
  
  Al enviar el formulario, se deberá realizar una petición al backend para actualizar la solicitud.
  

- Issue #005 (Frontend): Notificación de confirmación

  Una vez que la solicitud sea actualizada correctamente, el sistema deberá mostrar una notificación clara indicando que la solicitud fue reenviada exitosamente.
  
  En caso de error, se deberá mostrar un mensaje informativo con la causa del fallo.

## RF-06 – Acceso a Contenido (Issues en prosa)
- Issue #001 (Backend): Obtención de eventos aprobados

  Se deberá implementar un endpoint que retorne la lista de eventos a los que el usuario tiene acceso.
  
  El sistema deberá validar el token y recuperar únicamente aquellos eventos para los cuales el usuario tenga una solicitud en estado aprobada.
  
  Cada evento deberá incluir información básica como identificador y nombre.

- Issue #002 (Backend): Validación de acceso a contenido
  Se deberá implementar una validación que garantice que únicamente los usuarios con solicitudes aprobadas puedan acceder al contenido de un evento.
  
  Si un usuario intenta acceder a un evento sin contar con aprobación, el sistema deberá denegar el acceso y retornar un error de autorización.
  

- Issue #003 (Frontend): Vista de eventos del usuario
  Se deberá desarrollar una sección denominada “Mis Eventos”, en la cual se listarán todos los eventos confirmados del usuario.

  La vista deberá consumir el endpoint correspondiente y permitir la navegación hacia el detalle de cada evento.

- Issue #004 (Frontend): Vista de detalle del evento

  Se deberá implementar una vista que muestre la información completa del evento seleccionado.
  
  Esta vista deberá incluir:
  
  •	Información general del evento
  
  •	Recursos disponibles (archivos, enlaces, materiales)
  
  El acceso a esta vista deberá estar restringido únicamente a usuarios autorizados.

