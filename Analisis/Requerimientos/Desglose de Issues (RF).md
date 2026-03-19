# Desglose de Issues (Requerimientos Funcionales)
## RF-01 - Gestión de Perfil
- **Issue #001 (Backend)** : Endpoint unificado de autenticación

  Se deberá implementar un endpoint que permita gestionar el inicio de sesión del usuario mediante correo electrónico y contraseña.

  El sistema deberá recibir las credenciales del usuario y validar que el correo exista en la base de datos. En caso de ser válido, se deberá generar un código de acceso temporal que será   enviado al correo electrónico registrado.

  Posteriormente, el sistema deberá validar el código ingresado por el usuario, asegurando que coincida con el generado y que no haya expirado.
  Una vez validado correctamente, el sistema deberá generar un token de autenticación que permita acceder a los recursos protegidos.

  En caso de credenciales incorrectas, código inválido o expirado, el sistema deberá rechazar la autenticación.

- **Issue #002 (Backend)** : Obtención del perfil del usuario

  Se deberá implementar un endpoint que permita obtener la información del perfil del usuario autenticado.
  
  El sistema deberá validar el token de autenticación y extraer el identificador del usuario.
  Posteriormente, deberá consultar la base de datos y retornar los datos del perfil, incluyendo al menos correo electrónico, nombre y teléfono.
  
  Si el token no es válido o no está presente, el sistema deberá rechazar la solicitud.

- **Issue #003 (Frontend)** : Vista de perfil de usuario

  Se deberá desarrollar una vista que permita visualizar la información del perfil del usuario.
  
  La vista deberá consumir el endpoint correspondiente y mostrar de forma clara los datos del usuario, incluyendo correo electrónico, nombre y número telefónico.
  
  La información deberá presentarse en formato legible y organizado, sin permitir modificaciones directas en modo visualización.

- **Issue #004 (Frontend)** : Edición del perfil

  Se deberá implementar un modo de edición dentro de la vista de perfil.
  
  Al activar este modo, el sistema deberá mostrar un formulario precargado con la información actual del usuario.
  El usuario podrá modificar los campos disponibles y guardar los cambios.
  
  El sistema deberá validar que los datos ingresados cumplan con los formatos requeridos antes de enviarlos al backend.
  Una vez actualizados correctamente, se deberá reflejar la información actualizada en la vista y mostrar una confirmación al usuario.

## RF-02 – Solicitud de Inscripción
- **Issue #001 (Backend)**: Listado de eventos disponibles

  Se deberá implementar un endpoint que retorne todos los eventos disponibles para inscripción.
  
  El sistema deberá proporcionar, para cada evento, la siguiente información: identificador, nombre, fecha de inicio, fecha de finalización, descripción breve, precio y el estado de la solicitud del usuario respecto a dicho evento.
  
  En caso de que el usuario no tenga una solicitud asociada, el estado deberá indicarse como no existente o equivalente.
- **Issue #002 (Backend)**: Detalle de evento

  Se deberá implementar un endpoint que permita obtener la información completa de un evento específico.
  
  El sistema deberá recibir el identificador del evento y validar su existencia.
  En caso de ser válido, deberá retornar toda la información relevante del evento, incluyendo descripción completa, fechas, costo y cualquier dato adicional necesario para la inscripción.
- **Issue #003 (Backend)**: Generación de formulario de inscripción

  Se deberá implementar la lógica necesaria para proporcionar los campos requeridos para el registro a un evento.
  
  El sistema deberá definir los datos necesarios para completar la inscripción, los cuales podrán variar dependiendo del evento.
  Estos campos deberán ser retornados al frontend para su renderización dinámica.
- **Issue #004 (Frontend)**: Sección de eventos disponibles

  Se deberá implementar una sección denominada “Eventos Disponibles”.
  
  Esta vista deberá consumir el endpoint de listado de eventos y mostrar la información de forma estructurada, permitiendo al usuario identificar rápidamente las opciones disponibles.
  
  Cada evento deberá incluir una opción para visualizar más detalles.
- **Issue #005 (Frontend)**: Vista de detalle de evento

  Se deberá implementar una vista que muestre la información completa de un evento seleccionado.
  
  Esta vista deberá consumir el endpoint correspondiente y presentar todos los datos relevantes, incluyendo descripción, fechas, costo y estado de inscripción del usuario.
- **Issue #006 (Frontend)**: Acción de inscripción

  Se deberá implementar la funcionalidad que permita al usuario iniciar el proceso de inscripción a un evento.
  
  Esta acción deberá estar disponible tanto desde la lista como desde la vista de detalle del evento.
  Al activarse, el sistema deberá mostrar el formulario de inscripción correspondiente.

## RF-03 - Carga de Documentación
- **Issue #001 (Backend)**: Obtención de documentos requeridos

  Se deberá implementar un endpoint que permita obtener la lista de documentos requeridos para una solicitud específica.
  
  El sistema deberá validar que la solicitud exista y que pertenezca al usuario autenticado.
  En caso de ser válida, deberá retornar el listado de documentos obligatorios.
- **Issue #002 (Backend)**: Carga de documentos

  Se deberá implementar un endpoint que permita subir archivos asociados a una solicitud.
  
  El sistema deberá validar: Existencia de la solicitud y que pertenezca al usuario autenticado.
  
  Una vez validado, deberá almacenar el archivo y asociarlo correctamente a la solicitud correspondiente.
- **Issue #003 (Backend)**: Validación de documentos completos

  Se deberá implementar una funcionalidad que permita verificar si una solicitud cuenta con todos los documentos requeridos.
  
  El sistema deberá comparar la lista de documentos obligatorios del evento con los documentos cargados por el usuario y determinar si la documentación está completa.
- **Issue #004 (Backend)**: Manejo de formatos no permitidos

  Se deberá implementar una validación que restrinja los tipos de archivo permitidos.
  
  En caso de que el usuario intente subir un archivo con un formato no permitido, el sistema deberá rechazar la operación y retornar un mensaje de error claro.
- **Issue #005 (Frontend)**: Componente de carga de documentos

  Se deberá desarrollar un componente reutilizable denominado “CargarDocumento”.
  
  Este componente deberá incluir un campo de selección de archivo y validar en el cliente: Tipo de archivo permitido y tamaño máximo permitido.
  
  El componente deberá ser reutilizable en distintas partes del sistema.
- **Issue #006 (Frontend)**: Notificación de carga exitosa

  Una vez que un documento sea cargado correctamente, el sistema deberá mostrar una notificación temporal indicando que la operación fue exitosa.
  
  El mensaje deberá ser claro y visible para el usuario.
- **Issue #007 (Frontend)**: Cancelación de carga

  Se deberá implementar una opción que permita cancelar la carga de un archivo en proceso.
  
  Al cancelar, el sistema deberá detener la operación, descartar cualquier dato temporal y regresar al estado previo sin realizar cambios en la solicitud.
## RF-04 – Consulta de Estatus
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


## RF-05 – Reenvío de Solicitudes
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

## RF-06 – Acceso a Contenido
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

