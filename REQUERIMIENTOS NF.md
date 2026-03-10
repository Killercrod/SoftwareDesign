**REQUISITOS NO FUNCIONALES![ref1]**

Sistema ECFCA — Educación Continua FCA-UADY![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAngAAAAECAYAAAAd6EKpAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAGZJREFUaIHtzrENwjAARcHvBERHyxZswiKZgpYVWIQRqBgGhOhip2KBSMgSuitf9RIAAP5KSZKc23B83y5JOXT+AQBglVa3r3l6XE+fzTeVVu91GPc9twAAWKck9bkb594fAAD8wAJS8hHTuZe20AAAAABJRU5ErkJggg==)

1. **PROCESO DE GESTIÓN DE REQUISITOS NO FUNCIONALES** 

Los Requisitos No Funcionales (RNF) especifican los estándares y cualidades que debe cumplir un sistema para funcionar de manera eficaz, centrándose en cómo opera el sistema y no en qué hace. En el contexto del Sistema ECFCA, donde se gestionan datos personales sensibles de participantes, capacitadores y personal administrativo, los RNF son críticos para garantizar seguridad. 

1. **Descripción General** 

Este proceso establece la metodología para identificar, definir, documentar, implementar y revisar los RNF del Módulo de Gestión de Usuarios (MU), iniciando con CU-MU-001: Consultar Usuarios. El módulo administra el ciclo de vida completo de todos los actores del sistema: Público General, Capacitadores, Staff, Coordinación y Personal de Contabilidad. 

2. **Objetivo** 

Asegurar que los RNF se implementen correctamente, garantizando que el sistema ECFCA opere con los niveles de rendimiento, seguridad, disponibilidad y calidad requeridos para una plataforma de la UADY. 

3. **Identificación de RNF**  

A partir del caso de uso CU-MU-001 al CU-MU-009 y considerando que el sistema maneja información personal sensible bajo las restricciones del aviso de privacidad obligatorio, se identificaron los siguientes RNF: ![ref2]



|||||
| :- | :- | :- | :- |
|**ID RNF**|**Categoría**|**Descripción**|**Vinculado a RF**|
|||||
|RNF-01|Rendimiento|La consulta de usuarios debe retornar resultados en un “tiempo promedio” para el volumen de registros esperado en ECFCA.||
|RNF-02|Seguridad|Solo usuarios autenticados con rol autorizado (Staff, Coordinación) pueden ejecutar CU-MU-001. Los ||


|||datos personales deben protegerse según el aviso de privacidad del sistema.||
| :- | :- | :- | :- |
|RNF-03|Disponibilidad|El módulo de consulta debe estar disponible el 99% del tiempo en horario operativo institucional.||
|RNF-04|Usabilidad|La interfaz de consulta debe ser operable en menos de 3 pasos desde el menú principal, adaptada al perfil del personal administrativo de la FCA.||
|RNF-05|Mantenibilidad|El módulo debe seguir patrones de arquitectura documentados para facilitar su evolución conforme el sistema ECFCA crezca.||
|RNF-06|Escalabilidad|El sistema debe soportar el ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOQAAAATCAYAAACAwKEsAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMdJREFUeJzt27FNA0EQRuE357PkBAc0Q0AbroNy3AkluAOKcAUIIbw/wVkELuBuJN6X7IaTPO0GuyCpjQL4/Pp+GyMvYdTWA0n/TX44H58OF6oyA4zwWnCCySClldWe98ClgBmgkspyWhqktLIdu7/9tOEckh4YpNSIQUqNGKTUiEFKjRik1IhBSo0YpNSIQUqNGKTUiEFKjcwAgSyLpLXduMH9PevyuLz4yMgzkwemtL66VlXg/rsjyYTXV2kro6rG1kNIevAL9VMlDXSN5r0AAAAASUVORK5CYII=)crecimiento proyectado de usuarios del sistema ECFCA sin degradación visible del servicio.||
4. **Criterios de Calidad ![ref1]**

Los criterios de calidad definen las métricas medibles que determinan si un RNF se ha cumplido satisfactoriamente en el contexto del sistema ECFCA: 



|||||
| :- | :- | :- | :- |
|**RNF ID**|**Criterio**|**Métrica**|**Umbral Aceptable**|
|||||
|RNF-01|Tiempo de respuesta|Respuesta medida bajo carga normal de operación|FALTA RELLENAR |
|RNF-02|Control de acceso|Porcentaje de intentos no autorizados bloqueados|100% de bloqueo|
|RNF-03|Disponibilidad|Tiempo activo dividido entre tiempo total operativo|≥ 99%|
|RNF-04|Pasos de navegación|Número de clics para llegar a la función de consulta|≤ 3 pasos|
|RNF-05|Cobertura documental|Porcentaje de módulos con documentación actualizada|≥ 95%|
|RNF-06|Usuarios concurrentes|Usuarios simultáneos sin tasa de error > 5%|FALTA RELLENAR |

5. **Proceso de Evaluación ![ref2]**

El proceso de evaluación de RNF sigue un flujo estructurado en cinco etapas: ![ref1]

- Etapa 1 — Definición: El equipo identifica los RNF durante la fase de análisis de cada caso de uso. 
- Etapa 2 — Implementación: El desarrollador responsable integra los RNF en el diseño técnico. 
- Etapa 3 — Prueba: Se ejecutan pruebas de rendimiento, seguridad y carga según las métricas definidas. 
- Etapa 4 — Validación: Un integrante diferente al implementador verifica que los criterios se cumplan. 
- Etapa 5 — Cierre: Se documenta el resultado en el registro de RNF y se actualiza el estado del issue. 
6. **Proceso de Revisión ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAngAAAAGCAYAAABQIOOiAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAJ1JREFUaIHt2CEOwkAQRuF/tw0oJAi4Qz0KboDjKtg9Cp4DYOEGBI/CQYohTQVhFkEwlZuQDeR9bmbM0yMBAADgrzhJUgh+rpm/6Oqz1gAAACDJSEPbaW8KwcrPsm7adanBOGcYAAAA0tzUWhWni6PUvD94MbpqtZ3Eh/UytwEAACBB0S/scLqftVk+XefWnQEAAPAbYu4AAAAAfMkLUkAhC/1EqVYAAAAASUVORK5CYII=)**



||||
| :- | :- | :- |
|**Fase de Revisión**|**Responsable**|**Frecuencia**|
||||
|Revisión inicial|Lead del equipo|Al definir cada caso de uso|
|Revisión de ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKoAAAAUCAYAAAAdtqaHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAALdJREFUaIHt2iFuAnEQRvE3LCEBi+YCexk01yLhJtwCj0dXt6JddhCwpHVF/Znk/dy4Tzw5IBUQAJnZnc90fd96jvQ0RsQwHQHw+fW9T8bt45SaCzitlotdRPwAzAGSXENssFS9iSQv/Opx1nCL9G+GqhIMVSUYqkowVJVgqCrBUFWCoaoEQ1UJhqoSDFUlGKpKMFSVMAcYuR5mdMfWY6TJMPIB/P1HBchMX/z0NiLuP/2td0gvuQG3gh9gTjYJZAAAAABJRU5ErkJggg==)implementación|Integrante diferente al ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMoAAAAUCAYAAADMUaL3AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAALJJREFUaIHt2zESAUEQRuHXZg9gD+BiUrdwHscRuYVEQFlVymoBq2Q6I3hf1tkkryb6QdJXAZCZDZhNtyTuwBgRCdABDMN1nZErCEORnnaX83EJnOAVSkbMgQXPX0US7Ftr7x4MQyowFKnAUKQCQ5EKDEUqMBSpwFCkAkORCgxFKjAUqcBQpAJDkQoMRSroAKJjc7uO2zZrv36P9BfGex76vh+m+70/yUy3KNKHabQlqegB3+Agj2HguZcAAAAASUVORK5CYII=)implementador|Antes de merge a rama principal|
|Revisión periódica|Todo el equipo/Profesor|Sprint review / semanal (Jueves)|

2. **EVALUACIÓN DE FEATURES EN RNF**  

Esta sección determina si cada funcionalidad de CU-MU-001 al CU-MU-009 aporta valor real al proyecto ECFCA desde la perspectiva de los RNF, evitando funcionalidades que afecten negativamente el rendimiento o la complejidad del sistema. Se consideran especialmente las restricciones de privacidad y el manejo de datos personales del alumnado y personal de la FCA-UADY. 

1. **Impacto en Rendimiento ![ref2]**



|||||
| :- | :- | :- | :- |
|**Funcionalidad**|**Impacto**|**Riesgo Identificado**|**Acción Recomendada**|
|||||
|Búsqueda por múltiples filtros (rol, estado, fecha)|**MEDIO**|Consultas complejas pueden aumentar la latencia en tablas con muchos usuarios||
|Paginación de resultados|**BAJO**|Carga controlada por página, impacto mínimo|Implementar paginación en todos los listados del módulo|

Búsqueda en tiempo real  **ALTO** Múltiples peticiones  ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARsAAAB7CAYAAABEriTPAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAABBVJREFUeJzt3b9uHFUUwOFzZtbxnwQCCkLUkWhSUNFHdJQ00PAOSEhI0Nmmo+ENeIJ9E6QIhAISBVI6FIqAFBQ73t25FI7Xm4CiJPKeQevvq65sF0ejq5937njXEQAFMiKitZa//Hb/g3feuv5pRNsdeyi4aPfv3Mnvv/xiJ4ZFN/Ysl0XLaDe//e7z27ffuxeRbXL2jWtXd2688fr2Rxn5ZuaIE8IFaxHxcCsXsz9+j2jne541a20xP3r0dWtxLzNieeH7iMjMyCevdmBTnG7oltFaRGsjT3OpPNUSLymBEmIDlBAboITYACVWYtN7CMXG6veuHndXto9e6IcdIj/fS12freVq5THgorXwKIrN1PWTRWSoSLGhPy+T2yighNgAJcQGKCE2QAmxAUqIDVBCbIASYgOUEBughNgAJcQGKCE2QAmxAUqIDTzLh62shdgAL+cVYyw2QAmxAUqIDVBCbIASYgOUEBughNgAJcQGKCE2QAmxAUqIDVBCbIASYgOUEBughNgAJcQGKCE2QAmxAUqIDVBCbIASYgOUEBughNgAJcQGKCE2QAmxAUqIDVBCbIAS57Hp+4jWXu0/hgP8hysr62VsMtq1iLhWPw6s3/zx8W60tjf2HJfNnz/+cONsff7KJqOPzH6UiWDN2jD00Zpjg2I5P5ocHh5mhDMboIjYACXEBijxdGzaSFMAG2+yXLVo88XQMiWHDZRtyNcn0Z0MzW/VIhlDP9md73/1WTs4ODiPzWw2xOOT+Zijwdo87o6iv/kgog1jj3KpXLn17l9n68nK1zMzMiL8YR8bJ2ORLY8jYrC/63T9zs6y7g6IgRJiA5QQG6CE2AAlzt+I2bVZRHgcxWbqtxaZ3Yvt7+bR+HO9xPXpFv2/D4gXi+FRRP59wWPB/0K/vXcc/dbx2HNcNvPM5dO/p26jmqIDa+LMBighNkAJsQFKiA1QQmyAEmIDlBAboITYACXEBighNkAJsQFKiA1QQmyAEmIDz0qfif5cr3h9xAYoITZACbEBSogNUEJsgBJiA5QQG6CE2AAlxAYoITZACbEBSogNUEJsgBJiA5QQG6CE2AAlxAYoITZACbEBSogNUEJsgBJiA5QQG6CE2AAlxAYoITZACbEBSogNUEJsgBKTs0XfdTsRsdvaiNPAmgyzk+2IsL2LDQ9+fi3i/YhYiU1rw3ZEbGeONRas0TCfZBvC9q41f/hg72y9chvVh9CwqVrozFgODw8zwpkNUERsgBJiA5SYrKxbRAxjDQJrdrq30x6vku30Wu/v77eDg4PT2GRG3P316KduK77JIfpxR4SLN+uvL/ZufRgxO7G/i7TMljtv380nT56WJ/SttZxGdB+PNhqsz3Q6jZhOxx7j0vlkOh3i9K4JoMY/fvDAPuJm8rwAAAAASUVORK5CYII=)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAAB7CAYAAAACPdBMAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAArpJREFUeJzt3b1uXEUAhuFv1meTAAoiDTeQjobL4AosOi6Eip5LccMV0YQ6kUGQ2PHOUDhrORIQfoS8n/Q8ze6cPcUUr0azI+2eBEqNJHl1+fqbw1pfjXdjOEVzZf788s23z58/e5GMtSXJZ58++TLJ10l2Dzs9+HPXN4f58ter79fKizGS7d5nI1ZeTtt7fVppqSVeaomXWuKllnjpsZL9vaF46TGSt/eG4qWWeKklXmqJl1ripZZ4qSVeaomXWuKllnipJV5qiZda4qWWeKklXmqJl1ripZZ4qSVeaomXWuKllnipJV5qiZda4qWWeKklXmqJl1ripZZ4qSVeaomXWuKllnipJV5qiZda4qWWeKklXmqJl1ripZZ4qSVeah3jHQ86C/gXjvE+i4A5cSPJJ/uzj4/jY7z7P74dTstu5Ozu/UNOBP4L8VJLvNQSL7W2JJlzzjHGjBMHTtRKslbm2crheG1LkqvrQ9ZaI+LlhN3Mlcvf3rz+PE+THFfetXa5DVe8nKy55u56rXUc2/NSS7zUEi+1xEutXZKMMa4eeiLwYSNb9u9/YVuHeZnbo7QP+3t3wf9g5SZv707EbrcNu50kqWPPSy3xUku81BIvtcRLLfFSS7zUEi+1xEst8VJLvNQSL7XES61/Hq+faHIirLzUEi+1xEst8VJLvNQSL7XESy3xUku81BIvtcRLLfFSS7zUEi+1xEst8VJLvNQSL7XESy3xUku81BIvtcRLLfFSS7zUEi+1xEst8VJLvNTakmSN+TRz+P9HTttK9vsnj4/DLUnOsvtoDs/O5sSNke3s8Og43CXJXMuqSx17XmqJl1ripdb27nUlmfHECU7YSOa2truThS1JXv1y/cNch58sw5yyOedajx7/OMbt0dhIku/W2n2RjPOHnRv8pYuLi5yfn89jvFDrdztxcGkpa7waAAAAAElFTkSuQmCC)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALQAAAB7CAYAAADdc6pTAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAqJJREFUeJzt3bGKJEUAxvGv6gblTA4ExcDkIsGHMRvxcXyfQR/BpzAVc+EQPXD3VrfLYGa9FTG4RRj74/eDnq4eGKjgT9FdE3QCRUaS/PTqty8Ph/HFWmtee0Lwrn65ufv25ScvvhljrEOSfPTh85dr5asxImh2Za3kflvf57w4n4NOkjHOpyvNC55sPlqHrchUETRVBE0VQVNF0Ozelu2vzQxBs3szc70dQxFBU0XQVBE0VQRNFUFTRdBUETRVBE0VQVNF0FQRNFUETRVBU0XQVBE0VQRNFUFTRdBUETRVBE0VQVNF0FQRNFUETRVBU0XQVBE0VQRNFUFTRdBUETRVBE0VQVNF0FQRNFUETRVBU0XQVBE0VQRNFUFTRdBUeQh6XA7Yn/nP4WcRNDs1kw8ejZM8+gL2Zst6djqdRuIemjKCpoqgqSJoqhyS5Pf7bY1kXXsy8K7WSras++PxuJJL0G9u75I5Jc3urKzc3m43eXG+PiTJmPP8x8qwF83OrJHzOn3mHpoqgqaKoKlyDnq78izgPzKTZD1bv157IvBUc+bvD4Uj44fYtGOntu3t7txMkjnnGmMImt3zUEgVQVNF0FQRNFUETRVBU0XQVBE0VQRNFUFTRdBUETRVBE0VQVNF0FQRNFUETRVBU0XQVBE0VQRNFUFTRdBUETRVBE0VQVNF0FQRNFUETRVBU0XQVBE0VQRNFUFTRdBUETRVBE0VQVNF0FQRNFUETRVBU0XQVDkkybpfn66ssbztmx0aY73/MD4Hva2PMzPG+Pcfwf/RWslc472H6/noE/ZpJqfTaVyG0EPQVBE0VQ6X83p0wH6MZCXreDyu5BL0z6/vTtu6/9FyzR7dvPnju1wW45EkX681P0/G8arTgifbxhjuLujzJ5pRabHyJot1AAAAAElFTkSuQmCC)![ref1]

por nombre o correo pueden saturar el  

servidor 

Historial de actividad del  **MEDIO** Consultas sobre  Limitar historial visible a usuario registros históricos  los últimos 30 días por 

pueden ser costosas  defecto

2. **Impacto en Seguridad** 



|||||
| :- | :- | :- | :- |
|**Funcionalidad**|**Nivel de Riesgo**|**Vulnerabilidad Potencial**|**Control Requerido**|
|||||
|Consulta de datos personales (nombre, correo, documentos)|**ALTO**|Exposición de información personal sin autorización|Verificación de rol activo y sesión válida en cada petición|
|<p>Filtro por correo electrónico </p><p>o identificador</p>|**MEDIO**|Posible enumeración de usuarios del sistema|Límite de peticiones y validación estricta de entradas|
|Visualización de roles y permisos asignados|**ALTO**|Información sensible sobre la estructura interna del sistema|Acceso restringido únicamente a Staff y Coordinación|
|Consulta de estado de documentos cargados|**ALTO**|Documentos oficiales son datos sensibles bajo aviso de privacidad|Definir roles autorizados; solo Staff de validación|

3. **Impacto en Mantenimiento ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAngAAAAECAYAAAAd6EKpAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAGhJREFUaIHtzrEJwlAUQNH3giCWwTQO4RDO4iIO4QDZwnXSp01h9Z+dAwThg5xT3upGAADwVzIiIh41XLfXPXIYO/8AALBDRWvbenou8+19+NbMc0abOn4BALBTVbXLeMyl9wgAAL/3AVmfEjsMBqrxAAAAAElFTkSuQmCC)![ref2]**



|||||
| :- | :- | :- | :- |
|**Funcionalidad**|**Complejidad**|**Deuda Técnica Potencial**|**Mitigación**|
|||||
|Filtros dinámicos por tipo de usuario|**ALTA**|Lógica difícil de mantener si crece el número de roles|Usar patrón de diseño para construcción de filtros|
|Paginación estándar de resultados|**BAJA**|Deuda técnica mínima, componente estable|Estandarizar como ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJwAAAAUCAYAAAB4W1T4AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAKtJREFUaIHt2sERAVEQBuGetRkIRQwiEoE4xCEHF+E4KOzvwJYEGFX0d5t3mkNXvcuA1KgAkgzAMM/Sm92qKkBGgNP5uq4p2ySLLy+mHxSyS7KrKsbHy7QMrJhn6Z1Sex6/Z4Zv76L/YnBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqNQKMleMlbMoA9QFTDQcg8DrAnA8vPcDUJ+R5gCn1ugNFNCcQb5nC3wAAAABJRU5ErkJggg==)componente reutilizable ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJwAAAAUCAYAAAB4W1T4AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAK5JREFUaIHt2rGtAkEMBuHx6bqgFgqgHgq4K4Xo0QwSFdAHAexPAK8DMBKaL9rQwcibGKRGBZBker3ru+PoR42qGgAzwPV6294z9hTTd+fSj/pLcqyqzAB3xgbYkWeA0jslnHj+nnGjqZXBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqZXBqdUMMKUuqXGAMkC93QhnIPA6uFzXdVqWxeNLfUr+DzClVg+p9iWFb5+76gAAAABJRU5ErkJggg==)en el sistema|
|Auditoría de consultas realizadas|**MEDIA**|El registro de actividad puede acumular volumen alto de datos|Documentar política de retención y limpieza periódica|

3. **ALCANCE Y COMPLEJIDAD DE REQUERIMIENTOS  ![ref1]**

Clasifica cada funcionalidad del caso de uso, según su nivel de complejidad, facilitando la planificación del desarrollo. Esta clasificación se aplica una vez finalizados los issues de requisitos correspondientes. 

1. **Clasificación de Funcionalidades** 



||||||
| :- | :- | :- | :- | :- |
|**N°**|**Funcionalidad**|**Alcance**|**Complejidad**|**RF / RNF**|
||||||
|1|Listado paginado de usuarios|Mostrar usuarios activos e inactivos con paginación de 20 por página|**SENCILLA**|RF-, RNF-01|
|2|Búsqueda por nombre o correo|Campo de búsqueda con retardo de 300 ms antes de ejecutar la consulta al ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAAATCAYAAADmml17AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMBJREFUaIHt0jFOw1AURNGZyI5AoBQu6S2xDXbCstgSBctwkyKSCwR2fv6jSUo3pLCfdE833RRXApKyJI3j2JW2fbLttQ8BSyIiTsNw7Pt+kq7xfv/MHxHxftvAFtmuJfR2eGw/bUcjSVFrI3sv4sWGRUR1ueykVpK0W/kP8G/Ei7SIF2kRL9IiXqRFvEiLeJEW8SIt4kVaxIu0iBdpES/SIl6kZUmapnid6+9Lo2btP8CiUorOzw9fnT2u/QW4yx+m8i4mSlazfAAAAABJRU5ErkJggg==)servidor|**SENCILLA**|RF-, RNF-01|
|3|Filtros por rol, estado y fecha|Filtrar por tipo de actor del sistema ECFCA: Público General, Capacitador, Staff, Coordinación, entre otros|**INTERMEDIA**|RF-, RNF-01|
|4|Vista de detalle de usuario|Panel con datos completos del usuario, respetando los datos autorizados según el rol del consultante|**SENCILLA**|RF-, RNF-02|
|5|Control de acceso por rol|Verificación de sesión activa y permisos antes de mostrar datos sensibles, incluyendo documentos y datos de perfil|**INTERMEDIA**|RF-, RNF-02|
|6|Auditoría de consultas realizadas|Registro inmutable de quién ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAAAUCAYAAAD7n23DAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMJJREFUaIHt2rFNA0EQRuE3XovQTVDCSWQ0Q0CVlMD1QAE4s4wEp/uJsByBROIb6X3RrrTBBk8TDUhN1c8hSf32UNqCqsrlDHA+fz58sdwPxu1+Jf0hkCx3L4dDvQPsAdasz6PGE1eTWNqagjV8PCY5VlV2t/6Q9F/Gq7aMV20Zr9oyXrVlvGrLeNWW8aot41Vbxqu2jFdtGa/aMl61tQco6i3wStwq03ZV1brs1tPlDpBk4BTWxs3zzDRNy/VCutTSN8MuKq09W7W0AAAAAElFTkSuQmCC)consultó qué datos y cuándo, con retención de 90 días conforme a las políticas del sistema|**COMPLEJA**|RF-, RNF-02|

2. **Resumen por Nivel de Complejidad** 

**Nivel Cantidad Funcionalidades Esfuerzo Estimado ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKIAAACYCAYAAABnEzLQAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAABIpJREFUeJzt3b1uY0UYh/H3HX/F9mYhClkRtNIuUSqEBOI6qGkRNHsd3AESHSXXgKgpEKKioECIFQFpV0qksBjwJrGdc85LwWYMsZEPZh3/hZ9fkSgfTqZ4NPY5mcyYAQL86v1nXz3cPjkZvLDW0WBzTJqj99956/TqQzcziwh/94NP3vvym4cfRkRj2iewGvf29744fGPr7Y8fPLg0M2tefWE8uUyXRdk3s7S20WEjuLuVZdkdHO/kGY/oIIEQIYEQIYEQIYEQISGH6MnDzGKNY8EGy7dvttvtoac0rKrqxYWPiuBWI+YLM/PFcURE7Owf5Ikvh+ipFW5W1ekr3OkQc4XFwjbczNzdB8dH3EeEFkKEBEKEBEKEBEKEBEKEBEKEBEKEBEKEBEKEBEKEBEKEBEKEhLz6ZlJOtsKqbtRcksjCRczlf67AWSz86ZOTvPomh1gURcfNOyzvwqq5uYW5Xwy3WQYGLYQICYQICYQICYQICYQICfn2ze29cXH3cDiJIE6smLvtbrcno5+bs/9O+mvxY+PR6Ou2ESJWzN2t0bvfvLN7OBtiWZUewd9LcAMiv8mY/SCBECGBECGBECEhh9jt9M6T+3mdB3FRg3+ybBs5xHajc2nuk+c2IuBf4KkZEggREggREggREggREggREggREggREggREggREggREggREggREpYKscaZf9hUS8ax5IxIiZhv2TJ4aoYEQoQEQoQEQoQEQoQEQoQEQoQEQoQEQoQEQoQEQoQEQoQEQoSEHGIVZbKIxjoHg82VQ5xMxv0wv7XOwWBzREQ6tZ9yf9MZ0arkFiw0xM24toCW14iQQIiQQIiQQIiQkE+eul9cxPl4GBHVOseDjeC2NzmPzit34/Nnn8khvv77iR/88oMbBwZgxdzdWu1utLea8dGzz+UQG1Za4tgK3JDrrfEaERIIERIIERIIERLyxYo3OiNzH0dEd/HDwtj/BvPVbMPLONjfmT3BPnVuj83ThUdZI0RgvtpTVDT86HiQv5WnZkggREggREggREggREggREggREggREggREggREggREggREggREggREjgLD48V75kG8yIkECIkECIkECIkECIkECIkECIkECIkECIkECIkECIkECIkECIkPCXI6iqZGacxYebcW2RTg6xGD/tWwRn8eFGREQ6s9PZs/jCqrT0YjLgP+I1IiQQIiQQIiQQIiRMN3M/61U26BcWJXFitTyZ93vF8El3djP34nGVLr9vNc1ahIjVcrdUtNLLd27NhmhmxoGQWBdmP0ggREggREggREjIIXqrPTL38ToHg/+BmofPe0Qc7EzP4puufuj3x+5+Ue93cXmN+eqWEe5+NOAsPoghREggREggREggREggREggREggREggREggREggREggREggREiYbjlSlq0wa69zMNgc1/e2ySFWo4uemfVq/RBnixzMV7eNKiKdnfZnN2EC1okQIYEQIYEQISHv9JDcw9zNuBDBqrnb9Tkwh9i+9+rj/mtvflpFxT7aWDG35u5L3/72XbNc90iAv/kDrrf5yN/y1WQAAAAASUVORK5CYII=)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAACYCAYAAABj5uLtAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAA65JREFUeJzt3b9qFFEYhvH3Ozv5Y4KoKcRCUFBES7G1FcROSMDOznsQBPcGvAML+9yA12BtBGtRg2AgRGPI7Mxn4Y7ZBMXGmVfc51fNwBaneDize3Y4RwKMQpKev9xaKwdfV92DwXy4sHhu9969q3tSZEjSlftPXkTkemaEe3D4v0WEbl2/PL6x+O7ZeDxuK0mqJ82pCK1oOiMCfSkRquvJghan997hYN4RIKwIEFYECCsChNVMgOkbBeZWJUkZ+VqKdbEMg56lpKY9uq8kKbIcRiRTIHoXkkYzz12+A8KKAGFFgLAiQFgRIKwIEFYECCsChBUBwooAYUWAsCJAWBEgrKavY7UXFRHihRj0LCU1yiXpqaRx9zpWnA8peB0QfQuFmkkudvc8gmGxtbUZEgHCjABhRYCwIkBYESCsKkl6/PDu9rnTq4cRrMOgf63K/ts7N3MzpgE+un/7Y5RSKXPkHhz+b5nS591vzQNJY00DLKX8+AuE/SkxgDLzzY/vgLAiQFgRIKwIEFYECCsChBUBwooAYUWAsCJAWBEgrAgQVgQIKwKEFQHCigBhRYCwIkBYESCsCBBWBAgrAoQVAcKKAGFFgLAiQFgRIKwIEFYECCsChBUBwooAYUWAsCJAWHUBLouD4jCUOJr4uotrIkAMJdqV7rILsDINBXMpYnOTwwrxDyBAWBEgrAgQVpUk1XUziZDSPRrMhabJemNjI6VpgIeThl/BGERKquvmoLvnEYxhpdTO3BIgrAgQVgQIqx8Btn/4FNCTSpKixKdUZiYvJKB/pRyt+FWSlJHvlRyYjv5lSm17NNEVSSqlZESwDo3B8SMEVgQIKwKEFQHCigBhRYCwIkBYESCsCBBWBAgrAoQVAcKKAGFFgLAiQFgRIKwIEFYECCsChBUBwooAYUWAsCJAWBEgrAgQVgQIKwKEVZGkbLWcmWxNhIHE8bPi2mbCWXEYUB4/Ky5KYZd8DGYkcVYcjMovL4HhESCsCBBWlSRVVfmQGTuhJEj0qpVUIvaPnRW3tFBtSzorZkT0LCV9GZWmuz+5/MJaIPqVUpmZ55jxYEWAsCJAWBEgrAgQw5s5K44AMbyTZ8UBLgQIKwKEFQHCigBhRYCwIkBYESCsCBBWBAgrAoQVAcKqCzDE6/gw6AJcs44CcyWjXeiuuwAviRkQA4mIZfaGwT+BAGFFgLAiQFj93BkhJSnz958E/oKusGN7w+zsfXtVVFYk9olGvzKlg/36jc6cYraD33fyzqFrlrW/KgAAAABJRU5ErkJggg==)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAACYCAYAAABj5uLtAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAA5BJREFUeJzt3b1qFFEYxvHnnZl8aQgIqQLaCF6Bnb2NjbeghbkKr0RstRW8Bjt7K0tFxYBfqMnOOa/F7qxxISSIM08w/1+x7IEhTPHnzM5hMkcCjEKSnjx/ufuz1C33yeBimL1vDvb3b36XpE6SHj5+9kiRtxc9AqNZX2vzxrW9B1I+lSI7SZrVshXSJffJ4f/XNKFZ7dczpQipcZ8QLjYChBUBwooAYUWAsJoHWCVJ6TwRXEydJCn0KnXGdcBMlgtxgtPDSEmRsZzsFgHmLBR5lr8wP4gC8XdCUkYuA+I3IKwIEFYECCsChBUBwooAYUWAsCJAWBEgrAgQVgQIKwKEFQHCav40TNVeNnm2R1xCSh4dxF9KpUopa8N4HqBiN3jKDxMIhbI23TBujn0CkyM9WBEgrAgQVgQIKwKE1fz1bPfuvNu5vHkolmIwulDNejiMOkm6f/fWh0itScmMiFGVmvr89Ucdxp20uA7H8gMYTbOSGDMerAgQVgQIKwKEFQHCigBhRYCwIkBYESCsCBBWBAgrAoQVAcKKAGFFgLAiQFgRIKwIEFYECCsChBUBwooAYUWAsCJAWBEgrAgQVgQIKwKEFQHCigBhRYCwIkBYESCsCBBWQ4Ab4v28mEjbtsvWhgCviwAxkYjYGL4PAXYnHAv8c/XYZMdvQFgRIKwIEFYECKtOkvq+lJrcBmN8JVNHR7MyX/lbBHjYl1ZpPS9cELWmsuTRMOYSDCsChBUBwooAYTUPsJ5yFDCSTpIy9FGpFCsxGFlKUvN7zaWTpFC+VQQBYnSRkioPI+CcIEBYESCsCBBWBAgrAoQVAcKKAGFFgLAiQFgRIKwIEFYECCsChBUBwooAYUWAsCJAWBEgrAgQVgQIKwKEFQHCigBhRYCwIkBYESCsCBBWiwAb9orDdNrVlxNlslccJpN1da+4hr3iMJ0IXs+Gc4IAYUWAsCJAWHWSVPp6oGi+iDthjCxTisjDYdxJ0s725htJ25nJjIhR1Zrq+365Mcgfyy8RTIAY12pizHiwIkBYESCsCBBWBIjJtW273CuOADG5UgoPI+B8IEBYESCsCBBWBAgrAoQVAcKKAGFFgLAiQFgRIKwIEFYECKshwCviP+Iwka5t2+H7EOBVESAmUiPWh+9cgmFFgLAiQFgRIKyOvxkhM5MbEYwqM6VSluNOkj59O3qRWXvqw9gypVnJ1+7zACRJvwDjYKIrcAjsMAAAAABJRU5ErkJggg==)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAACYCAYAAABj5uLtAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAA8RJREFUeJzt3T+OFEcYhvH3q+nZPyyBZSQHFoIIERJzB2PfAMmBb2ASJ6vhDCSEiJwEcYg9ACSECNmyDJZXsg073fU56OmZXQJrZKv7XTHPL5lp7QYVPKrp2umtkgCjkKQnz06udSWuuAeD3fDudP/9g/t3/pSkRpIePn3+KCLvZUZ4h4bPXdOUvH3j6x8z83FEZCNJy7Y9jIgj9+CwG9rMvcViEZKyuAeD3UaAsCJAWBEgrAgQVkWSQpGS0jwW7KCmf4mXqfxWqz9M/6vMbX4LO2m7MKLmerJrJCmVZ9s2lZKCAvE/lLL5woN7QFgRIKwIEFYECCsChBUBwooAYUWAsCJAWBEgrAgQVgQIKwKEVf84Vuh6Krd8lkZKHh3Ef5bqum5/uOoDzPwq+JdgTCLUZu4NV+XCT4CJcQ8IKwKEFQHCigBhRYCwaiTpp++/+fmLqwcfg5UwRhdqu/rX65MXklYB/vDd3V8iYi5mRIysZur96cfuQoClFL7awCRCUjk3zTHjwYoAYUWAsCJAWBEgrAgQVgQIKwKEFQHCigBhRYCwIkBYESCsCBBWBAgrAoQVAcKKAGFFgLAiQFgRIKwIEFYECCsChBUBwooAYUWAsCJAWBEgrAgQVgQIKwKEFQHCigBhNQR4YB0FdkpI5fj4WNImwFtih3xMZBazw+H9EODcNBbsoBp1fevHaZmwYhECKwKEFQHCqpGks7brQkol94EYV81UXXbL4boPcNnNSoQyObEL46qZOmu7D4tFf73+CM5MZj9MopMk9QVyDwgrAoQVAcLqfICsQDC5/sDqiF8zlSxEMLqUijYHpDeSVGu+jZCC/DCylFRV16UVSSqFj194sAiBFQHCigBhRYCwIkBYESCsCBBWBAgrAoQVAcKKAGFFgLAiQFgRIKwIEFYECCsChBUBwooAYUWAsCJAWBEgrAgQVgQIKwKEFQHCigBhxVlxmFyEii6cFZecFYfpNDE7PF69L5JUOSsOE6pKzorD5cAiBFYECCsChFUjSVnztyqdsks0xpYpKePv4bqRpKPD/TcReVXMiBhZTaltazucFdcf01CULIIxhejPaRBnxeFSIEBYESCsCBBWBAiDzVlxBAiDT86KA1wIEFYECCsChBUBwooAYUWAsCJAWBEgrAgQVgQIKwKE1RAgz+NjYuf3hpG+9A0Euyaq5qu9idYB3hSzICYSEevd2NgbBtObbd6yCIEVAcKKAGHVrF5TUmYm94EYVaakbnPdSNLvf3w4UWjO1kQYW6a0bPOV+kkP8PoHlhy17oNLcUAAAAAASUVORK5CYII=)SENCILLA** 3 1, 2, 4 1 a 2 días por 

funcionalidad

**INTERMEDIA** 2 3, 5 3 a 5 días por 

funcionalidad **COMPLEJA** 1 6 1 a 2 semanas![ref2]

4. **REFINAMIENTO Y DESGLOSE DE RNF  ![ref1]![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAngAAAAGCAYAAABQIOOiAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAJNJREFUaIHtziFuAlEARdH3yU8QbVI1CoPAsoSKboIl4LoH9oNvXRVbAI3oEkpSJgO/qrZizCTNOfKqmwAA8K+UJMmuzdaX9+ekPEz8AwDACGW434fPy8dpv+lrkuS4L2X5uG1pi4nfAAAYo5Zbuu6QpC+/bfX6Nv+uX7MJtwAAGKk+de28e7kmaVO/AAAAAAB/+QF+ihweA7iE6QAAAABJRU5ErkJggg==)**

Esta sección especifica en detalle cada RNF identificado para casos de usus, definiendo su propósito e impacto en el sistema ECFCA. 

**RNF-01 — Rendimiento** 



|**Identificador**|RNF-01|
| - | - |
|**Categoría**|Rendimiento|
|**Propósito**|Garantizar que la consulta de usuarios sea percibida como inmediata por el personal administrativo de la FCA, evitando tiempos de espera que interrumpan su trabajo.|
|**Impacto en el sistema**|Requiere clasificación de la base de datos sobre los campos de búsqueda frecuentes, paginación obligatoria en todos los listados y uso de caché para consultas repetidas.|

**RNF-02 — Seguridad** 



|**Identificador**|RNF-02|
| - | - |
|**Categoría**|Seguridad|
|**Propósito**|Proteger los datos personales de participantes, capacitadores y personal gestionados en ECFCA, garantizando que solo actores autorizados puedan acceder a la información según el aviso de privacidad institucional.|
|**Impacto en el sistema**|Agrega una capa de verificación en todos los puntos de acceso de CU- MU-001. Es obligatorio dado el manejo de información personal sensible. |

**RNF-03 — Disponibilidad ![ref2]**



|**Identificador**|RNF-03|
| - | - |
|**Categoría**|Disponibilidad|
|**Propósito**|Garantizar que el personal de la FCA-UADY pueda acceder a la consulta de usuarios en cualquier momento dentro del horario.|
|**Impacto en el sistema**|Requiere una estrategia de despliegue que minimice el tiempo de inactividad, con verificaciones de salud del servicio y un mecanismo de ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAb8AAAAUCAYAAAAdvzPrAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAN9JREFUeJzt3TFOw0AQhtF/YwqfxeIYHIKaiyQ+EbfxBdJTUQSBsxSQmobIkue9bqQtpvu01SQAUExLkt57m+e043HrdQDg/83znNPpdL3NLUneL59P+Vofc9huMQC4oz60/jqO47m11h+SJOv6nEN7yW8MAWBnrh9rljE5J/HXA6Ae8QOgHPEDoBzxA6Ac8QOgHPEDoBzxA6Ac8QOgHPEDoBzxA6Ac8QOgHPEDoBzxA6Ccn6sOLW9JPzvqAMA+9X4Y+uU23Y7ZDsuyDNM0bbcXANxPT7K21q5/vgSAPfoG4LEqXySEhZkAAAAASUVORK5CYII=)recuperación ante fallos documentado.|

**RNF-04 — Usabilidad ![ref1]**



|**Identificador**|RNF-04|
| - | - |
|**Categoría**|Usabilidad|
|**Propósito**|Asegurar que la consulta de usuarios sea entendible y accesible para el personal administrativo, coordinadores y staff, minimizando errores de operación.|
|**Impacto en el sistema**|Condiciona el diseño de la navegación, la disposición del formulario de búsqueda y la retroalimentación visual al mostrar resultados. Se deben validar estos criterios con pruebas de usabilidad con usuarios reales.|

**RNF-05 — Mantenibilidad** 



|**Identificador**|RNF-05|
| - | - |
|**Categoría**|Mantenibilidad|
|**Propósito**|Garantizar que el módulo de consulta pueda ser modificado de forma eficiente por cualquier integrante del equipo de desarrollo FMAT/FCA.|
|**Impacto en el sistema**|Exige separación de responsabilidades, uso de patrones de diseño documentados y revisión de código como parte obligatoria del proceso de integración de cambios.|

**RNF-06 — Escalabilidad ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAngAAAAECAYAAAAd6EKpAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAGhJREFUaIHtzsENAUEAhtF/jIsDBTjpQA2KoDQnFTirRSWbSLA7ThrYRCaR947f6UsAAPgrJUlyvNb9bn2Z0radfwAAmKGUjO9hdbqfD8PyG1um26LVTc8xAADmacn4rI9X7w8AAH7gAz6gErSJyiOaAAAAAElFTkSuQmCC)**



|**Identificador**|RNF-06|
| - | - |
|**Categoría**|Escalabilidad|
|**Propósito**|Asegurar que el módulo soporte el crecimiento esperado de registros en el sistema ECFCA, considerando la incorporación de nuevos eventos, participantes y capacitadores a lo largo del tiempo.|
|**Impacto en el sistema**|Requiere un diseño sin estado en la capa de servicio, agrupación de conexiones a la base de datos y monitoreo activo de métricas de carga ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAb8AAAATCAYAAAAAugNTAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAOlJREFUeJzt3LFNw0AYhuHvnCOW6ViGBViClq2YhFUoMgANRSQECMn4KEjYIFjyPU/3d1/36ppLAKAzJUne3j7uy67enm8A2JhWh6vHccyhlNJqkmQY7pL2EPEDYJuWOfPTmHpIkpok5Td6Q8QPgI2a5++S8fTmW3kLAPw78QOgO+IHQHfED4DuiB8A3RE/ALojfgB0R/wA6I74AdAd8QOgO+IHQHdOf3sOraW1tccAwIW0Wnd/natJsqS9pOW5DP61BmCDltaWJe/nsyTJ8Xi82e/318m03jAAuJjPTNP0Wkr5WnsJAKziB4emJxyEAOoAAAAAAElFTkSuQmCC)para detectar degradación tempranamente.|

5. **MATRIZ DE TRAZABILIDAD RF → RNF → CU** 

La siguiente matriz vincula cada Requisito Funcional (RF) del Módulo de Gestión de Usuarios con los Requisitos No Funcionales que lo condicionan y el Caso de Uso al que pertenece. Los RF-01 a RF-07 corresponden directamente a las acciones definidas en CU-MU-001 (Consultar ![ref2] Usuarios). Los casos de uso CU-MU-002 a CU-MU-009 comparten los RNF base del módulo, ![ref1]pero introducen consideraciones adicionales propias de cada flujo. 

1. **Trazabilidad por Requisito Funcional (CU-MU-001)** 



|||||
| :- | :- | :- | :- |
|**RF ID**|**Descripción del Requisito Funcional**|**RNF Relacionados**|**Caso de Uso**|
|||||
|RF-01|Listar todos los usuarios del sistema|RNF-01, RNF-03, RNF-06|CU-MU-001|
|RF-02|Buscar usuarios por criterios (nombre, correo, rol, estado)|RNF-01, RNF-04|CU-MU-001|
|RF-03|Controlar acceso a datos personales según rol del consultante|RNF-02|CU-MU-001|
|RF-04|Visualizar detalle completo de un usuario seleccionado|RNF-02, RNF-04|CU-MU-001|
|RF-05|Filtrar usuarios por tipo de actor y estado de cuenta|RNF-01, RNF-04|CU-MU-001|
|RF-06|Configurar parámetros de consulta ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAO8AAAATCAYAAAB4IFrbAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMxJREFUeJzt27FNA2EQBeFZc4DsBigAXBkt0RYdkBKQkYAODu45sZFIIfC/0nzZZpuMNlqQ1FIBJJmAzdNxljSeOwiwVFXgGOvb++cDlXtivNKwqtbK5X63q2eACWDNOhV1jZdXGlbBN1BJqqqyOfdCkv7GeKWmjFdqynilpoxXasp4paaMV2rKeKWmjFdqynilpoxXauon3tOngqQxJb8TnQA2sCSZq3xMkEaVsAI5RVoAr/N8e7Ve3HyxGK80rrxst4/7qo9zLyLpHw4Uai8ceVQ7/gAAAABJRU5ErkJggg==)aplicables al módulo|RNF-05|CU-MU-001|
|RF-07|Registrar auditoría de cada consulta realizada por el usuario|RNF-02, RNF-05|CU-MU-001|

2. **RNF Compartidos por Caso de Uso — Módulo de Usuarios** 

Todos los casos de uso, heredan los RNF base del sistema. La siguiente tabla refleja qué RNF son especialmente relevantes para cada CU según la naturaleza de sus flujos, actores y datos involucrados: ![ref2]



|||||
| :- | :- | :- | :- |
|**Caso de Uso**|**Descripción**|**RNF Principales**|**Actores**|
|||||
|CU-MU-001|Consultar Usuarios — listado, búsqueda y filtrado de todos los usuarios del sistema|RNF-01, RNF-02, RNF-03, RNF-04, RNF-06|Coordinación|
|CU-MU-002|Validar Documentación de Usuario — revisión y validación de documentos cargados por usuarios con notificación de ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMQAAAAUCAYAAADSmJJEAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAK5JREFUaIHt2rFNwwAQRuH3G1O4pYlEQ8sALJJlmCKTZCXaTBDJkQJyLkUQug2M5PdNcMU96YoDSX8CUFVPwLDyLNJaliQ3gBFgnr8/CXt+A5G2ZAiHqjomqRGgUm9JPjAIbdBC7XjsfnkmSY1BSI1BSI1BSI1BSI1BSI1BSI1BSI1BSI1BSI1BSI1BSI1BSE0Azufre55vr+PjG1zalEv9fL1M0ylJrT2LJOm/ugN8TB1zWoJrigAAAABJRU5ErkJggg==)resultado|RNF-02, RNF-03, RNF-04|Coordinación|
|CU-MU-003|Registrar Capacitador — captura de información personal y profesional de un nuevo capacitador|RNF-02, RNF-04, RNF-05|Coordinadora de EC|

![ref1]



|CU-MU-004|Consultar Capacitadores — ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMQAAAAUCAYAAADSmJJEAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAALpJREFUaIHt27ENwkAQRNEZ2wGSRUJOA26JYsAJdZDTBUWYRpAQAbcEWLAdnCX/V8EE97M9CcCPJSki2mma2mEYau8BanjbfktzEI/n66wSB9l1ZwE1lHLq+83FdnSSFCV2tveaAwHWJBpv9X370dQeAywJQQAJQQAJQQAJQQAJQQAJQQAJQQAJQQAJQQAJQQAJQQAJQQBJJ0mOuMq6i2tXrJBLc5MU0v+DkMdRPh6r7gJqCdtRewSwOB+oMySprYy81wAAAABJRU5ErkJggg==)listado y búsqueda de capacitadores registrados con opciones de filtrado|RNF-01, RNF-02, RNF-04|Coordinación|
| - | :- | :- | - |
|CU-MU-005|Modificar Información de Capacitador — actualización de datos personales y profesionales (excluye datos de pago)|RNF-02, RNF-04, RNF-05|Coordinadora de EC, Capacitador|
|CU-MU-006|<p>Archivar o Eliminar Capacitador </p><p>— baja lógica o definitiva de un capacitador del sistema con confirmación obligatoria</p>|RNF-02, RNF-05|Coordinadora de EC|
|CU-MU-007|Registrar o Actualizar Información de Pago y Facturación — captura de datos financieros del capacitador pendientes de validación|RNF-02, RNF-05|Coordinadora de EC|
|CU-MU-008|Validar Información de Pago Propia — el capacitador revisa y confirma sus datos financieros ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMQAAAATCAYAAADPnaL8AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMlJREFUaIHt2rFNQ0EQBuH5jydZCNqhAaogRyKlBgfugICUNkAipgVyKgBZkLxbEoOuA1u6+aK9bJPRJgeS/gXgc/9928J1Hd7STNKWp4vN8pykFoCQK8hNDEITqr6+bbe7F6AC8LX/eUxyh0FoQkXdX55vHpL0duxlpFNiENLAIKSBQUgDg5AGBiENDEIaGIQ0MAhpYBDSwCCkwQLQWquq6hiIZtQooOAQRK39nbP2ip/7NKHq68ffHICqangdNK+epB97Cenk/AJqhSsyL37jTgAAAABJRU5ErkJggg==)registrados por la administración|RNF-02, RNF-03, RNF-04|Capacitador|
|CU-MU-009|Consultar Capacitaciones Asignadas — el capacitador visualiza los eventos a los que ha sido asignado|RNF-01, RNF-02, RNF-03|Capacitador|

![ref2]

[ref1]: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAngAAAAGCAYAAABQIOOiAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAIVJREFUaIHt2bERAWEYBND9zs0IlCJUgWpUoABtaMQoQhcKEEgM7heQSAlumPeiDTfcmU0AAPgr9Z7baEUAAPhGJa8x9xx4rdV8vVsmmY1XCgCAT9XQ2vR83B+2q2ufJNmkJnU7dekvI3cDAOAD964bkkWSt4u2lYcWAOBHVZKUNQcA8I8eVGkWq48TDhsAAAAASUVORK5CYII=
[ref2]: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAngAAAAGCAYAAABQIOOiAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAJhJREFUaIHt1iEKQkEUheFz5yWRBxosRrEaLa7CorswuYFxBW8hdrPuwBWYzA9EREGcaxCrYcqA/F886Y9HAgAAwF8xSZK7LZbbcOqPQuEeAAAAZKiHV9/rkBRj+hy8GMPkNt3INSjcBgAAgAwmS+2rtz43s7t9t/FqV3e6qSpaBgAAgCzV4+nHZn6RmZduAQAAAAAAAPDLGxa+HgRQTtwDAAAAAElFTkSuQmCC
