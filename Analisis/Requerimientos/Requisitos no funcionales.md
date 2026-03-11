
## Requisitos No Funcionales (RNF) – Propuesta Inicial

- **RNF-01:**  
  Autenticación basada en tokens (JWT) con expiración tras 30 minutos de inactividad.

- **RNF-02:**  
  Cargas de archivos (hasta 10MB)

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
  Comentarios en el código
Cada función principal del Módulo de Usuarios deberá incluir al menos un comentario que describa su propósito.

- **RNF-09:**
  Documentos asociados
El sistema deberá permitir almacenar al menos 3 documentos por usuario para procesos de validación.

   



