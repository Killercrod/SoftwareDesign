
# Diagrama de Secuencia - Flujo de Inscripción

```mermaid
sequenceDiagram

actor Usuario
participant UI
participant EventoService
participant InscripcionService
participant CRMService
participant Repo

Usuario->>UI: ver eventos
UI->>EventoService: obtenerEventos()
EventoService->>Repo: fetch eventos
Repo-->>EventoService: lista
EventoService-->>UI: eventos

Usuario->>UI: inscribirse
UI->>InscripcionService: crearInscripcion(datos)

InscripcionService->>EventoService: validarCupo()
EventoService-->>InscripcionService: ok / no

alt cupo disponible
    InscripcionService->>Repo: guardarInscripcion()
    Repo-->>InscripcionService: ok

    InscripcionService->>CRMService: crearLead(usuario)
    CRMService->>Repo: guardarLead()

    InscripcionService-->>UI: confirmación
    UI-->>Usuario: inscripción exitosa
else sin cupo
    InscripcionService-->>UI: error
    UI-->>Usuario: no disponible
end
