**Definicion de endpoints, esquemas de request/response, códigos de estado y mecanismos de autenticación para cada módulo** 

**1. Autenticación** 

**Tipo:** JWT (JSON Web Token) 

**Headers requeridos en endpoints protegidos:**

Authorization: Bearer <token> Content-Type: application/json 

**Flujo de autenticación:** 

1. El usuario inicia sesión mediante /login  
1. El backend genera un token JWT con expiración (30 minutos) 
1. El cliente envía el token en cada petición protegida ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.001.png)
2. **Formato estándar de errores** 

Todos los errores deben seguir la siguiente estructura:

{ 

`  `"error": true, 

`  `"message": "Descripción del error",   "details": [] 

} ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.002.png)

3. **Módulo: Usuarios ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.003.png)**
1. **Registrar usuario** 

**Endpoint:** POST /api/v1/usuarios/register **Autenticación:** No requerida 

**Headers:** 

Content-Type: application/json **Request:** 

{ 

`  `"nombre": "Juan Pérez", 

`  `"email": "juan@email.com",   "password": "123456" 

} 

**Validaciones:** 

- Email con formato válido  
- Password mínimo 6 caracteres 

**Response (201):** 

{ 

`  `"id": "123", 

`  `"nombre": "Juan Pérez", 

`  `"email": "juan@email.com" } 

**Errores:** 

- 400: Datos inválidos  
- 409: Usuario ya existe  ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.004.png)
2. **Login** 

**Endpoint:** POST /api/v1/usuarios/login **Autenticación:** No requerida 

**Request:** 

{ 

`  `"email": "juan@email.com", 

`  `"password": "123456" } 

**Response (200):** 

{ 

`  `"access\_token": "jwt\_token",   "token\_type": "bearer" 

} 

**Errores:** 

- 401: Credenciales incorrectas ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.005.png)
3. **Obtener perfil** 

**Endpoint:** GET /api/v1/usuarios/me **Autenticación:** Requerida 

**Headers:** 

Authorization: Bearer <token> **Response (200):** 

{ 

`  `"id": "123", 

`  `"nombre": "Juan Pérez", 

`  `"email": "juan@email.com" } 

**Errores:** 

- 401: No autenticado  ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.006.png)
4. **Módulo: Capacitadores ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.007.png)**
1. **Crear capacitador** 

**Endpoint:** POST /api/v1/capacitadores **Autenticación:** Requerida (Admin) 

**Request:** 

{ 

`  `"nombre": "Carlos López", 

`  `"licenciatura": "Contabilidad",   "email": "carlos@email.com" } 

**Response (201):** 

{ 

`  `"id": "cap\_001", 

`  `"nombre": "Carlos López", 

`  `"licenciatura": "Contabilidad" } ![ref1]

2. **Listar capacitadores** 

**Endpoint:** GET /api/v1/capacitadores **Query Params:** 

- page (int)  
- limit (int)  

**Response (200):** 

[ 

`  `{ 

`    `"id": "cap\_001", 

`    `"nombre": "Carlos López"   } 

] ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.009.png)

3. **Actualizar capacitador** 

**Endpoint:** PUT /api/v1/capacitadores/{id} **Parámetro Path:** 

- id  

**Response (200):** 

{ 

`  `"message": "Actualizado correctamente" } ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.010.png)

4. **Eliminar capacitador** 

**Endpoint:** DELETE /api/v1/capacitadores/{id} **Response (200):** 

{ 

`  `"message": "Eliminado correctamente" } ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.011.png)

5. **Módulo: Administración (Eventos) ![ref1]**
1. **Crear evento** 

**Endpoint:** POST /api/v1/eventos **Autenticación:** Requerida 

**Request:** 

{ 

`  `"titulo": "Curso de Python",   "fecha": "2026-05-01", 

`  `"capacitador\_id": "cap\_001",   "cupo": 30 

} 

**Response (201):** 

{ 

`  `"id": "evt\_001", 

`  `"titulo": "Curso de Python" } ![ref2]

2. **Listar eventos** 

**Endpoint:** GET /api/v1/eventos **Query Params:** 

- fecha  
- capacitador\_id  

**Response (200):** 

[ 

`  `{ 

`    `"id": "evt\_001", 

`    `"titulo": "Curso de Python"   } 

] ![ref1]

3. **Obtener evento** 

**Endpoint:** GET /api/v1/eventos/{id} **Response (200):** 

{ 

`  `"id": "evt\_001", 

`  `"titulo": "Curso de Python",   "fecha": "2026-05-01" 

} ![ref3]

4. **Actualizar evento** 

**Endpoint:** PUT /api/v1/eventos/{id} **Response (200):** 

{ 

`  `"message": "Evento actualizado" ![ref2]

} 

5. **Eliminar evento** 

**Endpoint:** DELETE /api/v1/eventos/{id} **Response (200):** 

{ 

`  `"message": "Evento eliminado" 

} ![ref4]

6. **Integraciones externas ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.015.png)**
1. **Webhook Meta Ads** 

**Endpoint:** POST /api/v1/webhooks/meta **Request:** 

{ 

`  `"lead\_id": "123", 

`  `"email": "lead@email.com" } 

**Response (200):** 

{ 

`  `"message": "Lead recibido" } ![ref3]

2. **Integración UADY** 

**Endpoint:** GET /api/v1/integraciones/uady/{matricula} **Response (200):** 

{ 

`  `"nombre": "Alumno",   "estatus": "Activo" 

} ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.016.png)

7. **Códigos HTTP utilizados** 
- 200 → OK  
- 201 → Creado  
- 400 → Bad Request  
- 401 → No autenticado  
- 403 → Prohibido  
- 404 → No encontrado  
- 409 → Conflicto 
- 500 → Error interno del servidor  ![ref4]
8. **Notas técnicas** 
- Backend: FastAPI / Flask  
- Base de datos: MongoDB (PyMongo)  
- Validación: Pydantic  
- Autenticación: JWT  
- Servidor: Uvicorn  ![](Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.017.png)
9. **Valor aportado** 
- Define un contrato claro entre frontend y backend 
- Base para documentación interactiva (Swagger) 
- Facilita pruebas con Postman

[ref1]: Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.008.png
[ref2]: Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.012.png
[ref3]: Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.013.png
[ref4]: Aspose.Words.2e679e77-62df-4143-b7ad-acc7f1078d68.014.png
