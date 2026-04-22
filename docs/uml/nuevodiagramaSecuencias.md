```mermaid
sequenceDiagram

actor Usuario
participant Sistema

Usuario->>Sistema: iniciarSesion()
Sistema-->>Usuario: acceso

Usuario->>Sistema: seleccionarEvento()
Sistema-->>Usuario: verificarCupo()

alt no hay cupo
    Sistema-->>Usuario: mostrarMensaje("No hay cupo")
else hay cupo
    Usuario->>Sistema: subirDocumentos()
    Sistema-->>Usuario: documentosRecibidos

    Usuario->>Sistema: enviarDatos()
    Sistema-->>Usuario: validarDatos()

    alt datos incorrectos
        Sistema-->>Usuario: mostrarError("Datos inválidos")
    else datos correctos
        Sistema-->>Usuario: registrarSolicitud()
        Sistema-->>Usuario: confirmacion()
    end
end
