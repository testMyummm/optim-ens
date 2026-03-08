# PA-ACC-001 — Procedimiento de Alta de Personal

| Campo | Valor |
|-------|-------|
| **ID** | PA-ACC-001 |
| **Título** | Procedimiento de Alta de Personal |
| **Dominio** | ACC — Gestión de Accesos |
| **Tipo** | Procedimiento Aplicado (SOP) |
| **Procedimiento marco** | P04 Gestión de Usuarios |
| **Estado** | Vigente |
| **Última revisión** | 2026-03-08 |
| **Autor** | CISO / Responsable de Seguridad |
| **Aprobado por** | CEO |

---

# 1. Objetivo

Describir el proceso completo de alta de un nuevo empleado en optimTech, garantizando que:

- Se crean todas las cuentas y accesos necesarios
- Se entrega y configura el equipo corporativo
- Se firma toda la documentación de seguridad requerida por el ENS
- Se completa la formación de concienciación en seguridad

---

# 2. Alcance

Este procedimiento aplica a todo personal con contrato laboral o profesional que se incorpore a optimTech, incluyendo:

- Empleados con contrato indefinido o temporal
- Personal en prácticas
- Colaboradores externos con acceso a sistemas corporativos

---

# 3. Roles y responsabilidades

| Rol | Responsabilidad |
|-----|-----------------|
| CEO | Aprueba el alta del nuevo empleado |
| CISO / Responsable de Seguridad | Gestiona accesos técnicos y verifica cumplimiento de seguridad |
| Manager directo | Solicita el alta y supervisa la incorporación |

---

# 4. Checklist pre-ingreso

Antes de la fecha de incorporación, el Manager directo y el CISO deben completar:

- [ ] Confirmar fecha de incorporación
- [ ] Solicitar compra de equipo (ver PA-EPT-001)
- [ ] Preparar documentación: I01, I02-L-ES, DPT correspondiente

---

# 5. Alta en Microsoft 365

1. Acceder al Microsoft 365 Admin Center.
2. Crear cuenta de usuario: `usuario@optimtech.es`
3. Asignar licencia Microsoft 365 Business (incluye licencia Intune para gestión de dispositivos).
4. Configurar dirección de email y alias necesarios.
5. Añadir al grupo de seguridad correspondiente según su departamento y rol.
6. Añadir al grupo de Intune correspondiente para que el equipo reciba las políticas de cumplimiento y configuración automáticas.

---

# 6. Alta en SharePoint

1. Dar acceso al sitio de SharePoint departamental correspondiente.
2. Configurar permisos según el rol del empleado (lectura, edición, administración).
3. Verificar que el acceso funciona correctamente.

---

# 7. Alta en Atlassian (JSM)

1. Crear cuenta en Atlassian utilizando el email corporativo.
2. Asignar al portal de clientes JSM según corresponda.
3. No dar acceso a espacios Confluence salvo ENSCORP si aplica al rol.

---

# 8. Entrega de equipo

1. Rellenar formulario I03 Registro entrega dispositivos con los datos del equipo (número de serie, modelo).
2. Configurar equipo según PA-EPT-001 Adquisición y Configuración MacBook (incluye inscripción en Microsoft Intune vía Apple Business Manager).
3. Verificar en el portal de Intune que el dispositivo aparece como **Conforme** y que las políticas de seguridad (FileVault, Firewall, bloqueo de pantalla, actualizaciones) se han aplicado automáticamente.
4. Entregar equipo al empleado con firma del formulario I03.

---

# 9. Documentación de seguridad

El nuevo empleado debe firmar la siguiente documentación:

1. **I01** — Normativa de Seguridad de la Información.
2. **I02-L-ES** — Anexo de Protección de Datos (contrato laboral).
3. **DPT correspondiente** — Descripción del puesto de trabajo.

Una vez firmados, archivar las copias escaneadas (PDF) en `06_EVIDENCIAS/personal/`.

---

# 10. Formación ENS

1. Entregar la **Guía de Incorporación — Principios ENS** (`08_GOBERNANZA/`).
2. Realizar sesión de formación con la **Presentación ENS equipo optimTech** (`08_GOBERNANZA/`).
3. Registrar la asistencia del empleado a la sesión formativa.

---

# 11. Verificación final

Antes de dar por completado el proceso de alta, verificar:

- [ ] Cuenta M365 operativa
- [ ] Email funcional
- [ ] Acceso SharePoint confirmado
- [ ] Cuenta Atlassian/JSM activa
- [ ] Equipo entregado e I03 firmado
- [ ] Dispositivo inscrito en Intune y estado **Conforme**
- [ ] I01, I02, DPT firmados y archivados
- [ ] Sesión de formación ENS completada

---

# 12. Referencias

| Documento | Descripción |
|-----------|-------------|
| P04 | Gestión de Usuarios |
| I01 | Normativa de Seguridad de la Información |
| I02-L-ES | Anexo de Protección de Datos (contrato laboral) |
| I03 | Registro entrega dispositivos |
| PA-EPT-001 | Adquisición y Configuración MacBook |
| Guía de Incorporación | Principios ENS (`08_GOBERNANZA/`) |
| Presentación ENS | Presentación equipo optimTech (`08_GOBERNANZA/`) |

---

**Fin del Procedimiento**
