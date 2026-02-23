# Descripción General del Sistema

El sistema es una **plataforma integral de gestión académica y comercial**, cuyo objetivo principal es **automatizar todo el ciclo de vida de un evento educativo**, incluyendo cursos, diplomados y capacitaciones.

## Pilares del Sistema

El sistema se divide en **tres grandes pilares funcionales**:

### 1. Gestión de Ventas
Capta interesados (*leads*) desde **Meta Ads** y los convierte en clientes a través de un **embudo comercial estructurado**.

### 2. Gestión de Eventos
Administra la creación de cursos, capacitaciones y diplomados, así como la **generación de constancias**.

### 3. Público General
Es la **cara del sistema hacia el cliente final**. En este módulo los interesados pueden:
- Registrarse
- Subir documentación
- Realizar pagos
- Consultar el estado de sus solicitudes
- Acceder a sus eventos inscritos

---

## Casos de Uso Relacionados (Módulo Público General)

- **CU-PG-004:** Solicitar Inscripción a Evento  
- **CU-PG-005:** Realizar Pago de Solicitud Aprobada  
- **CU-PG-006:** Cargar Documentos (por el usuario)  
- **CU-PG-007:** Consultar Estado de mis Solicitudes / Inscripciones  
- **CU-PG-008:** Volver a Enviar Solicitud  
- **CU-PG-009:** Consultar Mis Eventos  

---

## Requisitos Funcionales (RF) 

- **RF-01 (Gestión de Perfil):**  
  El sistema permitirá al usuario iniciar sesión y gestionar sus datos personales.

- **RF-02 (Solicitud de Inscripción):**  
  El sistema permitirá al usuario seleccionar un evento y enviar una solicitud de inscripción (CU-PG-004).

- **RF-03 (Carga de Documentación):**  
  El sistema permitirá subir archivos digitalizados asociados a una solicitud (CU-PG-006).

- **RF-04 (Pasarela de Pagos):**  
  El sistema integrará un módulo de pago electrónico para solicitudes aprobadas (CU-PG-005).

- **RF-05 (Consulta de Estatus):**  
  El sistema mostrará una lista consolidada con el estado de solicitudes y pagos (CU-PG-007).

- **RF-06 (Reenvío de Solicitudes):**  
  El sistema permitirá editar y reenviar solicitudes rechazadas o con información incompleta (CU-PG-008).

- **RF-07 (Acceso a Contenido):**  
  El sistema permitirá visualizar los detalles y recursos de los eventos confirmados (CU-PG-009).

---

## Requisitos No Funcionales (RNF) – Propuesta Inicial

### 1. Seguridad (Prioridad Alta)

- **RNF-S-01:**  
  Autenticación basada en tokens (JWT) con expiración tras 30 minutos de inactividad.

- **RNF-S-02:**  
  Comunicación cifrada mediante **TLS 1.2 o superior** para datos personales y financieros.

- **RNF-S-03:**  
  Los documentos cargados no deben almacenarse en directorios públicos; el acceso será mediante URLs firmadas o servicios protegidos.

### 2. Rendimiento y Escalabilidad

- **RNF-R-01:**  
  Cargas de archivos (hasta 10MB) con barra de progreso asíncrona.

- **RNF-R-02:**  
  Timeout controlado en pasarela de pagos (≤ 5 segundos).

- **RNF-E-01:**  
  Soporte para 300 peticiones concurrentes con P95 ≤ 2.5 segundos.

### 3. Disponibilidad y Tolerancia a Fallos

- **RNF-D-01:**  
  Recuperación del módulo *Mis Eventos* en máximo 5 minutos (RTO).

- **RNF-D-02:**  
  Uso de transacciones ACID para evitar pagos sin solicitud asociada.

### 4. Usabilidad (UX)

- **RNF-U-01:**  
  Mensajes de error estructurados con causa y sugerencia.

- **RNF-U-02:**  
  Precarga de datos en reenvío de solicitudes (CU-PG-008).

### 5. Mantenibilidad y Arquitectura

- **RNF-M-01:**  
  Arquitectura en capas (Controller–Service–Repository).

- **RNF-M-02:**  
  Registro de auditoría con usuario, timestamp e IP por cambio de estado.

---




