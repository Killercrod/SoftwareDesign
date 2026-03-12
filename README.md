# Requisitos funcionales

Se documentará el proceso de la revisión de los requisitos funcionales en el proyecto (enfocado en el módulo de usuarios.)
## Definir como se identifica un Req. Funcional
Un requerimiento funcional especifica comportamientos observables, procesos a llevar a cabo y políticas que se deben enforzar que el software debe proveer.

**Ejemplo**: En un software de banco, debería cumplir que “una cuenta debe tener al menos un cliente como propietario” y “el dinero en una cuenta no puede ser negativo”, ambos son comportamientos que describen el programa bancario.

Una herramienta útil para separar a los funcionales de los no funcionales es el Perfect Technology Filter, donde plantea que un RF es aquel que necesita ser definido incluso si existiese una computadora con velocidad infinita, memoria ilimitada y sin errores, de lo contrario, sería un RNF.

*Cada requerimiento debe ser*:
* **Interpretable** de una sola manera, no debe haber ambigüedades en el requerimiento.
* **Testeable**, debe demostrarse su cumplimiento en el programa.

## Definir cómo se crea el issue
Un issue es un problema, una tarea a realizar a base de algún reporte o mejora solicitada, mientras que un RF se define de manera que no deje ambigüedades, a la hora de codificar, no puede ser lo suficientemente claro para el programador, por lo que se descompone en múltiples issues que faciliten el trabajo a la hora de programar el requisito.
De la descripción del requerimiento funcional, se va descomponiendo en estas tareas cortas.

**Ejemplo. RF-01**: Gestión del Carrito de Compras
El sistema debe permitir a los usuarios registrados añadir productos a un carrito de compras, visualizar el contenido del carrito con los precios actualizados y eliminar productos del mismo. El carrito debe persistir entre sesiones.

A partir del requisito, se descompone en distintos issues:
- **Issue #101	Backend**: Crear endpoint para añadir producto al carrito. Debe recibir producto_id y usuario_id y devolver el carrito actualizado.	"Añadir productos a un carrito de compras"
- **Issue #102	Frontend:** Implementar botón "Añadir al carrito" en la página de producto. Al hacer clic, debe llamar al endpoint del Issue #101 y mostrar una notificación de éxito.	"Añadir productos a un carrito de compras"
- **Issue #103	Backend**: Crear endpoint para obtener el contenido del carrito. Debe recibir usuario_id y devolver la lista de productos con sus precios.	"visualizar el contenido del carrito con los precios actualizados"
- **Issue #104	Frontend**: Crear la vista del carrito. Debe mostrar la información del endpoint (Issue #103), el precio total, y un botón para eliminar.	"visualizar el contenido del carrito... y eliminar productos"
- **Issue #105	Backend**: Crear endpoint para eliminar producto del carrito. Debe recibir producto_id y usuario_id.	"eliminar productos del mismo"
- **Issue #106	Base de Datos/Durabilidad:** Guardar el carrito en la base de datos. Asegurar que los cambios en el carrito se guarden y al volver a iniciar sesión, el carrito se recupere.	"El carrito debe persistir entre sesiones"

## Definir cómo se asigna
Durante las sesiones de refinamiento, el equipo analiza los issues derivados de los requisitos funcionales, verificando que tengan criterios de aceptación claros y estimando su complejidad técnica, se refina quien se hará cargo de cierto issue complementando con sub-equipos o parejas si la tarea lo requiere, se validan mediante el acuerdo de todos los integrantes para poder continuar con la asignación.

## Definir proceso de revisión

El proceso de revisión garantiza que el código cumple con los criterios de aceptación del issue y con los estándares de calidad del proyecto. El flujo es el siguiente:

1. **Desarrollo local:** El integrante crea una rama (branch) desde la rama principal (main/develop) y realiza los cambios necesarios para resolver el issue.

2. **Apertura de Pull Request (PR):** Al finalizar, abre un Pull Request hacia la rama principal. En la descripción del PR debe:
   - Vincular el issue correspondiente (ej. "Closes #101").
   - Describir brevemente la solución implementada.
   - Incluir evidencia de pruebas (si aplica).

3. **Revisión por pares:** Los miembros del equipo (diferente al autor). La revisión verifica:
   - Cumplimiento del issue y RF asociado.

4. **Retroalimentación:**
   - Si hay observaciones, se comentan en el PR y se notifica al autor para corrección.
   - Si no hay observaciones (o ya se solventaron), se **aprueba** el PR.

5. **Integración (Merge):** Con al menos una aprobación, el autor (o el revisor) procede a hacer **merge** del PR a la rama principal.

6. **Cierre del ciclo:** Una vez mergeado, se actualiza el issue en el tablero de proyectos marcándolo como **"Hecho"** (Done/Closed), asegurando la trazabilidad desde el RF original hasta la entrega.

## Requisitos Funcionales
**RF-01 (Gestión de Perfil):**
El sistema permitirá al usuario iniciar sesión y gestionar sus datos personales.

Issue #001: (Backend): Crear endpoint unificado de registro/login, recibe email y contraseña.

Issue #002: (Backend): Crear endpoint para obtener perfil del usuario autenticado, requiere token válido. 

Issue #003: (Frontend): Crear vista de perfil de usuario que muestre: email, nombre, teléfono.

Issue #004: (Frontend): Implementar modo edición en vista de perfil con formulario para editar los datos del usuario.

**RF-02 (Solicitud de Inscripción):**
El sistema permitirá al usuario seleccionar un evento en la sección de “Eventos Disponibles”, mostrar información clave (nombre, fechas, breve descripción, precio, estado de solicitud, etc.) y enviar una solicitud de inscripción (CU-PG-004).

Issue #001: (Backend): Listar los eventos disponibles con su campo requerido (id, nombre, fecha_inicio, fecha_fin, descripción_breve, precio, estado_solicitud_usuario).

Issue #002: (Backend): Obtener el detalle específico de un evento seleccionado, recibe evento_id y devuelve información completa del evento.

Issue #003: (Backend):  Generar un formulario de inscripción para el usuario con los datos necesarios.

Issue #004 (Frontend): Crear sección "Eventos Disponibles".

Issue #005 (Frontend): Vista de detalle de evento.

Issue #006 (Frontend): Acción "Inscribirse" desde lista o detalle.

**RF-03 (Carga de Documentación):**
El sistema permitirá subir archivos digitalizados asociados a una solicitud como parte del proceso de solicitud o cuando un administrativo solicita información adicional para una solicitud existente (CU-PG-006).

Issue #001: (Backend): Crear endpoint para obtener documentos requeridos de una solicitud, Validar que la solicitud existe y pertenece al usuario autenticado.

Issue #002: (Backend): Crear endpoint para subir documento, Validar solicitud existe y pertenece al usuario.

Issue #003: (Backend): Crear endpoint para verificar documentos completos de una solicitud, comparar documentos obligatorios del evento contra los ya subidos.

Issue #003: (Backend): Implementar manejo de excepción para formato de archivo no permitido. 

Issue #004: (Frontend): Crear componente reutilizable "CargarDocumento" que incluya: input file con validación en cliente de formato y tamaño.

Issue #005: (Frontend): Implementar notificación de carga exitosa mediante toast o mensaje temporal: "Documento cargado exitosamente".

Issue #006: (Frontend): Implementar cancelación de carga con botón "Cancelar" que interrumpa la subida, no guarde nada y retorne al estado anterior sin cambios.


 
**RF-04 (Consulta de Estatus):**
El sistema mostrará una lista consolidada con el estado de solicitudes y pagos del usuario autenticado (CU-PG-007).

Issue #001 (Backend): Crear endpoint para listar las solicitudes del usuario autenticado con su estado actual (pendiente, aprobada, rechazada, en revisión).

Issue #002 (Backend): Crear endpoint para obtener el detalle de una solicitud específica, incluyendo estado de documentos y estado de pago.

Issue #003 (Frontend): Crear vista de "Mis Solicitudes" que muestre una lista de las solicitudes del usuario con su estado y evento asociado.

Issue #004 (Frontend): Crear vista de detalle de solicitud donde se muestre información completa (evento, estado de solicitud, documentos requeridos, documentos cargados y estado de pago).

**RF-05 (Reenvío de Solicitudes):**
El sistema permitirá editar y reenviar solicitudes rechazadas o con información incompleta (CU-PG-008).

Issue #001 (Backend): Crear endpoint para actualizar una solicitud existente cuando su estado sea "rechazada" o "información incompleta".

Issue #002 (Backend): Validar que la solicitud a editar pertenezca al usuario autenticado y que su estado permita modificaciones.

Issue #003 (Frontend): Implementar opción "Editar solicitud" en solicitudes rechazadas o incompletas desde la vista de detalle.

Issue #004 (Frontend): Implementar formulario de edición que permita modificar los campos necesarios y reenviar la solicitud.

Issue #005 (Frontend): Mostrar notificación de confirmación cuando la solicitud sea reenviada exitosamente.
 
**RF-06 (Acceso a Contenido):**
El sistema permitirá visualizar los detalles y recursos de los eventos confirmados (CU-PG-009).

Issue #001 (Backend): Crear endpoint para obtener los recursos y detalles de un evento al que el usuario esté inscrito y aprobado.

Issue #002 (Backend): Validar que el usuario tenga una solicitud aprobada para el evento antes de permitir el acceso a su contenido.

Issue #003 (Frontend): Crear sección "Mis Eventos" que liste los eventos confirmados del usuario.

Issue #004 (Frontend): Crear vista de detalle del evento que muestre información, recursos disponibles y materiales asociados

