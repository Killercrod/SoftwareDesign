## Consideraciones Generales del Sistema y Protección de Datos

El sistema se concibe como un **CRM integrado con gestión de eventos y capacitaciones**, cuyo flujo funcional cubre desde la **captación de personas interesadas (leads)**, su **seguimiento comercial** y eventual **conversión en oportunidades**, hasta la **inscripción a eventos**, **validación administrativa**, **procesamiento de pagos** y **generación de constancias**.

Dado que el sistema gestiona **datos personales sensibles**, tales como información de contacto, documentos oficiales, comprobantes de pago y datos fiscales, resulta indispensable **reforzar explícitamente el consentimiento del usuario** y establecer mecanismos claros para el **control y uso adecuado de la información**.

Para garantizar lo anterior, el sistema debe:

- Incorporar un **aviso de privacidad obligatorio** antes de cualquier registro, inscripción o carga de documentos.
- Definir de manera explícita **los roles autorizados para acceder a cada tipo de información**.
- Asegurar que las **integraciones externas** se limiten únicamente a la **captación inicial de datos mínimos**.
- Restringir de forma estricta el acceso de fuentes externas a información sensible, como documentos oficiales, pagos o datos fiscales.

Estas medidas permiten asegurar el **cumplimiento legal**, fortalecer la **protección de la privacidad** y generar **confianza en los usuarios** del sistema.

---

## Alternativas Reales a Meta Ads para la Captación de Leads

### 1. Formularios Propios del Sistema
El sistema ofrece formularios de interés o preinscripción alojados directamente en la plataforma.

**Ventajas:**
- Control total de los datos
- Consentimiento explícito del usuario
- Menor riesgo legal
- Cero dependencia de terceros

---

### 2. Landing Pages Independientes
Páginas informativas conectadas al sistema mediante API o importación manual de datos.

**Ventajas:**
- Compatibles con campañas orgánicas o pagadas
- Independencia de plataformas publicitarias específicas
- Flexibilidad en diseño y despliegue

---

### 3. Importación Manual o por Archivo (CSV / Excel)
Carga de leads provenientes de ferias, convenios institucionales o bases de datos autorizadas.

**Ventajas:**
- Adecuado para contextos académicos o gubernamentales
- No requiere mecanismos de rastreo
- Alto control administrativo

---

### 4. Correo Institucional o Contacto Directo
El interesado escribe o llama, y el personal registra el lead manualmente.
Ventajas: cero transferencia de datos a terceros, alto control y trazabilidad.

---

### 5. APIs genéricas de fuentes externas (opcional)
En lugar de “Meta Ads”, el sistema puede definir un módulo abstracto como “Fuente externa de leads”.
Ventajas: el diseño queda neutro, escalable y no amarrado a una empresa específica.
Recomendación de diseño (importante)
Desde el punto de vista técnico y legal, lo mejor es no modelar Meta Ads como actor, sino como una fuente externa opcional, dejando claro que el sistema funciona completamente sin publicidad y que cualquier integración externa solo aporta datos mínimos con consentimiento previo del usuario.
En resumen: Meta Ads no es indispensable, y la alternativa más sólida es un sistema de captación propio con formularios y consentimiento explícito, que además fortalece la privacidad, simplifica el diagrama y hace el proyecto más defendible académica y legalmente.
