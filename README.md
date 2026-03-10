# **Requisitos funcionales**

Se documentará el proceso de la revisión de los requisitos funcionales en el proyecto (enfocado en el módulo de usuarios.)

Definir como se identifica un Req. Funcional
Un requerimiento funcional especifica comportamientos observables, procesos a llevar a cabo y políticas que se deben enforzar que el software debe proveer.

Ejemplo: En un software de banco, debería cumplir que “una cuenta debe tener al menos un cliente como propietario” y “el dinero en una cuenta no puede ser negativo”, ambos son comportamientos que describen el programa bancario.

Una herramienta útil para separar a los funcionales de los no funcionales es el Perfect Technology Filter, donde plantea que un RF es aquel que necesita ser definido incluso si existiese una computadora con velocidad infinita, memoria ilimitada y sin errores, de lo contrario, sería un RNF.

Cada requerimiento debe ser:
* Interpretable de una sola manera, no debe haber ambigüedades en el requerimiento.
* Testeable, debe demostrarse su cumplimiento en el programa.

Definir cómo se crea el issue
Un issue es un problema, una tarea a realizar a base de algún reporte o mejora solicitada, mientras que un RF se define de manera que no deje ambigüedades, a la hora de codificar, no puede ser lo suficientemente claro para el programador, por lo que se descompone en múltiples issues que faciliten el trabajo a la hora de programar el requisito.
De la descripción del requerimiento funcional, se va descomponiendo en estas tareas cortas.

Ejemplo. RF-01: Gestión del Carrito de Compras
El sistema debe permitir a los usuarios registrados añadir productos a un carrito de compras, visualizar el contenido del carrito con los precios actualizados y eliminar productos del mismo. El carrito debe persistir entre sesiones.
A partir del requisito, se descompone en distintos issues:

Issue #101
Backend: Crear endpoint para añadir producto al carrito. Debe recibir producto_id y usuario_id y devolver el carrito actualizado.
"Añadir productos a un carrito de compras"

Issue #102
Frontend: Implementar botón "Añadir al carrito" en la página de producto. Al hacer clic, debe llamar al endpoint del Issue #101 y mostrar una notificación de éxito.
"Añadir productos a un carrito de compras"

Issue #103
Backend: Crear endpoint para obtener el contenido del carrito. Debe recibir usuario_id y devolver la lista de productos con sus precios.
"visualizar el contenido del carrito con los precios actualizados"

Issue #104
Frontend: Crear la vista del carrito. Debe mostrar la información del endpoint (Issue #103), el precio total, y un botón para eliminar.
"visualizar el contenido del carrito... y eliminar productos"

Issue #105
Backend: Crear endpoint para eliminar producto del carrito. Debe recibir producto_id y usuario_id.
"eliminar productos del mismo"

Issue #106
Base de Datos/Durabilidad: Guardar el carrito en la base de datos. Asegurar que los cambios en el carrito se guarden y al volver a iniciar sesión, el carrito se recupere.
"El carrito debe persistir entre sesiones"




Definir cómo se asigna
hola braulio tello mancilla 
Definir proceso de revisión

