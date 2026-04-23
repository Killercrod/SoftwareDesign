```mermaid
graph LR
    subgraph ACTORES
        U[Usuario]
        C[Capacitador]
        A[Administración]
    end

    subgraph CONTROLLER
        direction TB
        C1(consultar_info_evento)
        C2(subir_documentos)
        C3(realizar_pago)
        C4(consultar_evento_asignado)
        C5(imprimir_facturación)
        C6(gestionar_capacitadores)
        C7(crear_evento)
        C8(administrar_información)
    end

    subgraph SERVICE
        direction TB
        S1(obtenerDetallesEvento)
        S2(validarDisponibilidadCupo)
        S3(procesarRegistroInteresado)
        S4(confirmarPagoYActivacion)
        S5(calcularFacturacion)
        S6(asignarAgendaCapacitador)
        S7(verificarFechas)
    end

    subgraph REPOSITORY
        direction TB
        R1(buscar_eventos)
        R2(insertar_evento)
        R3(actualizar_cupo)
        R4(almacenar_docs)
        R5(getCapacitadorID)
        R6(guardarFacturacion)
    end

    DB[(MongoDB)]

    %% Conexiones Actores -> Controller
    U --> C1 & C2 & C3
    C --> C4 & C5
    A --> C6 & C7 & C8

    %% Conexiones Controller -> Service
    C1 --> S1
    C2 --> S2
    C3 --> S4
    C5 --> S5
    C6 --> S6
    C7 --> S7

    %% Conexiones Service -> Repository
    S1 --> R1
    S2 --> R1
    S3 --> R4 & R3
    S4 --> R3
    S5 --> R6
    S6 --> R5
    S7 --> R1
    R1 -.-> R2

    %% Persistencia
    REPOSITORY --> DB
