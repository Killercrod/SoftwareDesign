
## Requisitos No Funcionales (RNF) – Propuesta Inicial

- **RNF-01:**  
  Autenticación basada en tokens (JWT) con expiración tras 30 minutos de inactividad.

- **RNF-02:**  
  Cargas de archivos (hasta 5MB)
  sistema deberá permitir subir documentos con un tamaño máximo de 5 MB por archivo.

- **RNF-03:**  
  Recuperación del módulo *Mis Eventos* en máximo 5 minutos (RTO).

- **RNF-04:**  
  Arquitectura en capas (Controller–Service–Repository).

 - **RNF-05:**
 Consistencia de interfaz
Todas las pantallas del Módulo de Usuarios deberán utilizar el mismo menú principal y el mismo diseño de botones para las acciones Crear, Guardar, Cancelar y Eliminar.

 - **RNF-06:**
   Validación de formularios
Los formularios de registro y edición deberán verificar que los campos obligatorios no estén vacíos antes de guardar la información.

 - **RNF-07:**
   Tiempo de procesamiento de acciones
El sistema deberá registrar, actualizar o eliminar información de usuarios en un tiempo menor o igual a 3 segundos.

- **RNF-08:**
Formato de correo electrónico (institucional)
El sistema deberá verificar que los correos electrónicos ingresados contengan el carácter “@” y un dominio antes de guardar el registro.

- **RNF-09**
  Identificador de usuario
El sistema deberá asignar un identificador único numérico a cada usuario registrado.
   



