# Introducción  
# Objetivo
--- 
# Flujo de trabajo
- Archivos de flujo  
- Bitácoras  
- Problemática  
- Requisitos  
  - Funcionales  
  - No funcionales  
- Atributos del Sistema  
  - Actividades  
  - Secuencias  
  - Clases  
  - Arquitectura  
  - Base de datos  
  - Explicación del trabajo / metodología / reuniones / bitácoras  
--- 
# Problemática  
## Requisitos  
### Funcionales  
  - Casos de Uso [DiagramaCU]  
### No funcionales  
  - Refinamiento y Desglose  
  - Atributos de calidad del sistema  
## Atributos del sistema   
### Flujo de Actividades [Diagrama de Actividades]
![Diagrama UML](./images/flujohappypath.png)
### Flujo de Secuencias [Diagramas de Secuencias]
secuencias lo abarca
### Interesados [Diagrama Inscripción]  
secuencias lo abarca
### Participantes [Diagrama "Mis Eventos"]  
### Flujo de Clases [Diagrama de clases]  

```mermaid
classDiagram

class Usuario {
  int idUsuario
  string nombre
  string email
  string etapa   // Interesado | Participante
  +iniciarSesion()
  +registrarse()
}

class Rol {
  int idRol
  string nombre  // Admin | Capacitador | Usuario
}

class Evento {
  int idEvento
  string nombre
  date fechaInicio
  date fechaFin
  string descripcion
  int cupo
  +verificarCupo()
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
  +validarDatos()
  +registrarSolicitud()
}

class Documento {
  int idDocumento
  int idSolicitud
  string nombre
  string tipo
  string estado
  +subirDocumento()
}

class Pago {
  int idPago
  +imprimirComprobante()
}

class Capacitador {
  int idCapacitador
  int idUsuario
  string informacionFiscal
  +consultarEventos()
}

Usuario --> Rol
Usuario --> Inscripcion

Evento --> Inscripcion
Inscripcion --> Solicitud
Solicitud --> Documento
Inscripcion --> Pago

Evento --> Capacitador
```

### Componentes y Dependencias (RNF.md)  
### Arquitectura  
  - Diagrama de Arquitectura  
  - Diagrama de despliegue
### Base de Datos  
