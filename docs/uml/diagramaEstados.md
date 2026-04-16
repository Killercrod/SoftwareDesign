# Diagrama de Estados - ECFCA

```mermaid
stateDiagram-v2
[*] --> Evento_Borrador
Evento_Borrador --> Evento_Publicado
Evento_Publicado --> Evento_Finalizado
Evento_Publicado --> Evento_Cancelado

Evento_Finalizado --> Solicitud_Pendiente
Evento_Cancelado --> Solicitud_Pendiente

Solicitud_Pendiente --> Solicitud_Aprobada
Solicitud_Pendiente --> Solicitud_Rechazada

Solicitud_Aprobada --> Lead_Nuevo
Solicitud_Rechazada --> Lead_Nuevo

Lead_Nuevo --> Lead_Contactado
Lead_Contactado --> Lead_Convertido

Lead_Convertido --> [*]
