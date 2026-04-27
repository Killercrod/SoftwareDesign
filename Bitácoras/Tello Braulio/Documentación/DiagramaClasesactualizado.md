classDiagram
    namespace Controllers {
        class UsuarioController {
            +consultarInfoEvento()
            +subirDocumentos()
            +inscribirse(idEvento)
            +accederMisEventos()
        }
        class CapacitadorController {
            +consultarEventoAsignado()
            +imprimirFacturacion()
        }
        class AdminController {
            +gestionarCapacitadores()
            +crearEvento()
            +administrarInformacion()
        }
    }
    namespace Services {
        class EventoService {
            +obtenerDetallesEvento()
            +validarDisponibilidadCupo()
            +verificarFechas()
        }
        class InscripcionService {
            +procesarRegistroInteresado()
            +confirmarPagoYActivacion()
        }
        class FacturacionService {
            +calcularFacturacion()
        }
        class CapacitadorService {
            +asignarAgendaCapacitador()
        }
    }
    namespace Repositories {
        class EventoRepository {
            +buscarEventos()
            +insertarEvento()
        }
        class InscripcionRepository {
            +actualizarCupo()
        }
        class DocumentoRepository {
            +almacenarDocs()
        }
        class CapacitadorRepository {
            +getCapacitadorID()
        }
        class FacturacionRepository {
            +guardarFacturacion()
        }
    }
    namespace Models {
        class Usuario {
            int idUsuario
            string nombre
            string email
            string etapa
        }
        class Rol {
            int idRol
            string nombre //Admin | capacitador | usuario
        }
        class Evento {
            int idEvento
            string nombre
            date fechaInicio
            date fechaFin
            string descripcion
            int cupo
        }
        class Inscripcion {
            int idInscripcion
            int idUsuario
            int idEvento
            string estado
        }
        class Solicitud {
            int idSolicitud
            int idInscripcion
            string estado
        }
        class Documento {
            int idDocumento
            int idSolicitud
            string nombre
            string tipo
            string estado
        }
        class Pago {
            int idPago
          
        }
        class Capacitador {
            int idCapacitador
            int idUsuario
            string informacionFiscal
        }
    }
    UsuarioController --> EventoService
    UsuarioController --> InscripcionService
    CapacitadorController --> CapacitadorService
    CapacitadorController --> FacturacionService
    AdminController --> CapacitadorService
    AdminController --> EventoService
    EventoService --> EventoRepository
    InscripcionService --> InscripcionRepository
    InscripcionService --> DocumentoRepository
    InscripcionService --> EventoRepository
    FacturacionService --> FacturacionRepository
    CapacitadorService --> CapacitadorRepository
    EventoRepository ..> Evento
    InscripcionRepository ..> Inscripcion
    DocumentoRepository ..> Documento
    DocumentoRepository ..> Solicitud
    CapacitadorRepository ..> Capacitador
    FacturacionRepository ..> Pago
    Usuario -->  Rol
    Usuario  -->  Inscripcion
    Evento  -->  Inscripcion
    Inscripcion  -->  Solicitud
    Solicitud  -->  Documento
    Capacitador  -->  Usuario
```
