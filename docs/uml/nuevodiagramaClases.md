```mermaid
classDiagram

class Usuario {
  int id
  string email
  string password
  string estado
  +iniciarSesion()
}

class Perfil {
  string nombre
  string telefono
}

class Rol {
  string nombre
}

class Evento {
  int id
  string nombre
  date fecha_inicio
  date fecha_fin
  string descripcion
  float precio
  +hayCupo()
}

class Categoria {
  string nombre
}

class Inscripcion {
  int id
  string estado
  date fecha
  +crear()
}

class Solicitud {
  int id
  string estado
  +validarDatos()
  +registrar()
}

class Documento {
  string nombre
  string tipo
  +subir()
}

class Lead {
  int id
  string nombre
  string email
  string estado
  +crear()
}

class Interaccion {
  int id
  date fecha
  string tipo
}

class Comunicacion {
  string medio
  string mensaje
}

Usuario "1" --> "1" Perfil
Usuario "*" --> "*" Rol
Usuario "1" --> "*" Inscripcion

Evento "*" --> "1" Categoria
Evento "1" --> "*" Inscripcion

Inscripcion "1" --> "1" Solicitud
Solicitud "1" --> "*" Documento

Lead "1" --> "*" Interaccion
Interaccion "1" --> "1" Comunicacion
