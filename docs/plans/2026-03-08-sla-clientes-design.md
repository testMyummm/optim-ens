# Diseño: I06 Acuerdo de Nivel de Servicio (SLA)

**Fecha:** 2026-03-08
**Estado:** Aprobado

## Contexto

optimTech ofrece desarrollo de soluciones IA y consultoría de mejora de procesos IA, principalmente al sector público. Los entregables típicos son aplicaciones web/API que quedan en producción y requieren mantenimiento. La empresa tiene 2 personas y opera en horario laboral L-V.

Actualmente no existe un documento SLA formal, aunque el rol de Responsable del Servicio ya tiene asignada la función de "Definir i supervisar els Nivells de Servei (SLA)" y el Plan de Concienciación marca como objetivo Q1 2026 obtener ITIL v4 Foundation para establecer SLA y OLA.

Documentos relacionados que ya referencian SLAs:
- P02 Adquisición de componentes TIC
- P03 Gestión de Cambios
- Organigrama Servicios y Departamentos
- Plan de Concienciación Seguridad
- Checklist Preparación Auditoría ENS

## Decisiones de diseño

- **Enfoque:** SLA como Anexo al Contrato (plantilla-marco con valores personalizables)
- **Código:** I06
- **Ubicación:** `02_NORMAS/I06 Acuerdo de Nivel de Servicio.docx`
- **Idioma:** Castellano
- **Formato:** Documento .docx con branding optimTech, campos `[PERSONALIZAR]`
- **Alcance:** Cubre tanto ejecución de proyecto como soporte post-entrega

## Estructura del documento

### 1. Objeto y alcance
Qué servicios cubre: desarrollo, despliegue, mantenimiento de aplicaciones web/API con IA. Campos personalizables para nombre del cliente y descripción del servicio concreto.

### 2. Definiciones
Términos clave: incidencia, petición, tiempo de respuesta, tiempo de resolución, disponibilidad, ventana de mantenimiento, fuerza mayor.

### 3. Niveles de servicio durante la ejecución del proyecto

| Compromiso | Valor por defecto |
|------------|-------------------|
| Informes de avance | Quincenal |
| Respuesta a peticiones de cambio | 5 días laborables |
| Entrega de hitos | Según cronograma acordado ±10% |

### 4. Niveles de servicio de soporte post-entrega

| Prioridad | Descripción | Respuesta | Resolución |
|-----------|-------------|-----------|------------|
| P1 - Crítica | Servicio caído, sin workaround | 4h laborables | 1 día laborable |
| P2 - Alta | Funcionalidad degradada | 8h laborables | 3 días laborables |
| P3 - Media | Error menor con workaround | 2 días laborables | 5 días laborables |
| P4 - Baja | Mejora o consulta | 5 días laborables | A planificar |

Disponibilidad: 99.0% mensual (excluye mantenimientos planificados).

### 5. Horario de servicio y contacto
- Horario: Lunes a Viernes, 9:00-18:00 (hora peninsular española)
- Canales: email, teléfono, sistema de tickets (Jira)
- Festivos: calendario laboral de Cataluña

### 6. Exclusiones
- Fuerza mayor
- Mantenimientos planificados (notificados con 48h de antelación)
- Incidencias causadas por mal uso del cliente
- Componentes de terceros fuera del control de optimTech (Azure, GCP)

### 7. Métricas y reporting
- Informe mensual de cumplimiento SLA
- Métricas: disponibilidad, tiempo medio de respuesta, tiempo medio de resolución, nº incidencias por prioridad

### 8. Penalizaciones y compensaciones
- Incumplimiento de disponibilidad: crédito proporcional al tiempo de indisponibilidad
- Incumplimiento reiterado de tiempos de respuesta: descuento en facturación
- Topes: máximo 10% de la facturación mensual del servicio afectado

### 9. Revisión y vigencia
- Vigencia: vinculada al contrato principal
- Revisión: anual o ante cambios significativos en el servicio
- Procedimiento de modificación: acuerdo mutuo por escrito

## Formato del documento .docx

- Branding optimTech (skill brand-guidelines)
- Tabla de control de versiones
- Campos `[PERSONALIZAR]` claramente marcados: nombre cliente, servicio, valores SLA específicos
- Pie de página con código I06 y numeración de páginas
