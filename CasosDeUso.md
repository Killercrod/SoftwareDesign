# Módulo de Usuarios – Casos de Uso

## CU-MU-001: Consultar Usuarios

### Actor(es)
- Coordinación

### Descripción
La coordinación visualiza una lista de todos los usuarios registrados en el sistema, pudiendo buscar, filtrar y acceder a sus perfiles.

### Precondiciones
- La Coordinación ha iniciado sesión en el sistema.

### Flujo Básico (Camino Feliz)
1. La Coordinación accede al **Módulo de Usuarios**.
2. El sistema muestra una lista paginada de todos los usuarios registrados (Público General, Capacitadores, etc.), incluyendo nombre, correo electrónico y estado de la cuenta.
3. De forma opcional, la Coordinación utiliza filtros (rol, estado) o la barra de búsqueda (nombre, correo).
4. El sistema actualiza la lista según los criterios aplicados.
5. La Coordinación selecciona un usuario para ver su perfil detallado o realizar acciones.

---

## CU-MU-002: Validar Documentación de Usuario (General)

### Actor(es)
- Coordinación

### Descripción
La coordinación revisa y valida documentos subidos por los usuarios relacionados con la verificación de su perfil, roles o requisitos generales del sistema.

### Precondiciones
- La Coordinación ha iniciado sesión.
- Existen documentos cargados pendientes de validación.

### Flujo Básico (Camino Feliz)
1. La Coordinación accede a **Validación de Documentación** desde el Módulo de Usuarios.
2. El sistema muestra usuarios con documentos pendientes, indicando tipo de documento y usuario.
3. La Coordinación selecciona un documento y lo revisa.
4. La Coordinación verifica autenticidad y cumplimiento.
5. Marca el documento como **Validado** o **No Válido**, con comentario opcional.
6. El sistema actualiza el estado del documento.
7. El sistema notifica al usuario el resultado.

---

## CU-MU-003: Registrar Capacitador

### Actor(es)
- Coordinadora de Educación Continua

### Descripción
La Coordinadora de EC registra a un nuevo capacitador, capturando información personal y profesional.

### Precondiciones
- La Coordinadora de EC ha iniciado sesión.

### Flujo Básico (Camino Feliz)
1. La Coordinadora accede al **Módulo de Usuarios**.
2. Selecciona **Registrar Nuevo Capacitador**.
3. El sistema muestra un formulario con información básica y profesional.
4. La Coordinadora completa los campos requeridos y opcionales.
5. Guarda la información.
6. El sistema confirma el registro y agrega al capacitador al catálogo.

---

## CU-MU-004: Consultar Capacitadores

### Actor(es)
- Coordinación

### Descripción
La coordinación consulta la lista de capacitadores registrados, con opciones de búsqueda y filtrado.

### Precondiciones
- La Coordinación ha iniciado sesión.

### Flujo Básico (Camino Feliz)
1. La Coordinación accede al **Módulo de Usuarios**.
2. Selecciona **Consultar Capacitadores**.
3. El sistema muestra la lista con información clave (nombre, especialidad).
4. Opcionalmente, se aplican filtros o búsquedas.

---

## CU-MU-005: Modificar Información de Capacitador

### Actor(es)
- Coordinadora de Educación Continua
- Capacitador

### Descripción
La Coordinadora de EC o el Capacitador actualizan información personal o profesional del capacitador, excluyendo datos de pago y facturación.

### Precondiciones
- El actor ha iniciado sesión.
- El capacitador existe en el sistema.

### Flujo Básico (Camino Feliz)
1. El actor accede a **Editar Información de Capacitador**.
2. El sistema muestra un formulario con la información actual.
3. El actor realiza los cambios necesarios.
4. Guarda los cambios.
5. El sistema confirma la actualización.

---

## CU-MU-006: Archivar o Eliminar Capacitador

### Actor(es)
- Coordinadora de Educación Continua

### Descripción
La Coordinadora de EC archiva o elimina un capacitador del sistema.

### Precondiciones
- La Coordinadora de EC ha iniciado sesión.
- El capacitador existe.

### Flujo Básico (Camino Feliz)
1. La Coordinadora accede al **Módulo de Usuarios**.
2. Selecciona el capacitador a archivar o eliminar.
3. El sistema solicita confirmación.
4. La Coordinadora confirma la acción.
5. El sistema actualiza el estado o elimina el registro.

---

## CU-MU-007: Registrar o Actualizar Información de Pago y Facturación de Capacitador

### Actor(es)
- Coordinadora de Educación Continua

### Descripción
La Coordinadora de EC registra o actualiza la información financiera del capacitador, la cual debe ser validada por el propio capacitador.

### Precondiciones
- La Coordinadora de EC ha iniciado sesión.
- El capacitador está registrado.

### Flujo Básico (Camino Feliz)
1. La Coordinadora accede al perfil del capacitador.
2. Selecciona **Gestionar Información de Pago/Facturación**.
3. El sistema muestra el formulario de datos financieros.
4. La Coordinadora captura o actualiza la información.
5. Guarda los cambios.
6. El sistema marca la información como **Pendiente de Validación por Capacitador**.
7. El sistema notifica al capacitador.

---

## CU-MU-008: Validar Información de Pago y Facturación Propia

### Actor(es)
- Capacitador

### Descripción
El capacitador revisa y valida su información de pago y facturación registrada por la administración.

### Precondiciones
- El Capacitador ha iniciado sesión.
- Existe información pendiente de validación.

### Flujo Básico (Camino Feliz)
1. El Capacitador accede a su perfil o sección de datos financieros.
2. El sistema muestra la información pendiente.
3. El Capacitador revisa los datos.
4. Confirma la información como correcta.
5. El sistema cambia el estado a **Validada por Capacitador**.
6. El sistema notifica a la administración.

---

## CU-MU-009: Consultar Capacitaciones Asignadas

### Actor(es)
- Capacitador

### Descripción
El capacitador visualiza las capacitaciones a las que ha sido asignado.

### Precondiciones
- El Capacitador ha iniciado sesión.
- Existen capacitaciones asignadas.

### Flujo Básico (Camino Feliz)
1. El Capacitador accede a **Mis Capacitaciones**.
2. El sistema muestra la lista de capacitaciones asignadas con detalles relevantes.
3. De forma opcional, el Capacitador consulta el detalle de una capacitación.
