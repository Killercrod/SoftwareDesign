**Componentes o dependencias a considerar siguiendo los RNF** 

1. **Backend (API en Python):** 

Usar FastAPI o flask  

Se relaciona con los RNF (01, 04, 06 y 07) 

2. **Autenticación (RNF-01)** 

**Librerías para JWT:** 

- PyJWT 
- Python-Jose 

**Sirven para:** 

- Generar tokens 
- Validar tokens 
- Configurar la expiración (30 mins) 
3. **Base de Datos (MongoDB)** 

**Conector en Python:** 

PyMongo 

4. **Manejo de archivos (RNF-02)** 

**Módulo nativo de Python:** os, shutil **Manejo de uploads en:** 

FastAPI → UploadFile 

Flask → request.files 

Se relaciona con la validación de tamaño (<= 5 MB) y guardado en servidor o carpeta local 

5. **Validación de datos (RNF-06, RNF-08)** 
- Pydantic  

Expresiones regulares (re de Python) **Para qué sirve:** 

- Validar campos obligatorios 
- Validar formato de correo 
6. **Arquitectura en capas (RNF-04)** 

**Organización del proyecto  Estructura:** 

/app 

`  `/controllers   /services 

`  `/repositories   /models 

`  `/schemas 

7. **Manejo de sesiones y rendimiento (RNF-07)** 
- Uvicorn  

**Para qué sirve:** 

- Ejecutar el servidor 
- Mejorar tiempos de respuesta
8. **Identificadores únicos (RNF-09)** 

` `**Opciones en MongoDB:** 

- \_id automático de MongoDB 

Glosario de librerías y dependencias: FastAPI 

FastAPI es un framework moderno de alto rendimiento diseñado específicamente para APIs. Valida datos automáticamente usando tipos de Python, genera documentación OpenAPI (Swagger) sin configuración adicional y soporta nativamente asincronía con async/await. Ofrece inyección de dependencias robusta 

y detección de errores mediante tipado estático. Es ideal para microservicios, APIs de alto rendimiento y proyectos donde la validación y documentación son críticas.

Flask 

Flask es un micro-framework flexible y simple que no impone estructura. Ofrece enrutamiento básico, plantillas Jinja2 y un ecosistema extenso de extensiones para añadir funcionalidades como ORM o autenticación. Es ideal para prototipos rápidos, aplicaciones web tradicionales y cuando se necesita control total sobre la arquitectura. Tiene una curva de aprendizaje muy baja.

PyJWT 

Biblioteca de Python para crear y verificar tokens JWT (JSON Web Tokens). Se usa comúnmente para autenticación y autorización en APIs, permitiendo intercambiar información segura entre servicios sin necesidad de mantener sesiones en el servidor. 

Python-Jose 

Librería que implementa varios estándares de criptografía incluyendo JWT, JWE y JWS. Ofrece funcionalidades más amplias que PyJWT, soportando múltiples algoritmos de cifrado y firmas digitales para casos de uso que requieren mayor seguridad o 

estándares específicos.

Pymongo 

Driver oficial de Python para MongoDB. Permite interactuar con bases de datos NoSQL MongoDB desde aplicaciones Python, facilitando operaciones CRUD, agregaciones, conexiones a clusters y gestión de índices sin necesidad de usar un ORM tradicional. 

Pydantic 

Biblioteca de validación de datos que usa anotaciones de tipos de Python. Valida y ![](Aspose.Words.1b24649b-511d-41f7-a4a2-def14977c514.001.png)transforma datos automáticamente al inicializar modelos, generando errores claros cuando los datos no cumplen con los esquemas definidos. Es fundamental en FastAPI para validación automática de entradas y salidas.

Uvicorn 

Servidor ASGI (Asynchronous Server Gateway Interface) de alto rendimiento para aplicaciones Python. Ejecuta aplicaciones asíncronas como FastAPI o Starlette, manejando peticiones HTTP de forma eficiente con soporte nativo para async/await y múltiples workers. 
