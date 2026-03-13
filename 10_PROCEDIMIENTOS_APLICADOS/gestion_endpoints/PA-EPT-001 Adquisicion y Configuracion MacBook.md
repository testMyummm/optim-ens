# PA-EPT-001 — Adquisición y Configuración MacBook

| Campo | Valor |
|-------|-------|
| **ID** | PA-EPT-001 |
| **Título** | Adquisición y Configuración MacBook |
| **Dominio** | EPT — Gestión de Endpoints |
| **Tipo** | Procedimiento Aplicado (SOP) |
| **Procedimiento marco** | P02 Adquisición de componentes y servicios TIC |
| **Estado** | Vigente |
| **Última revisión** | 2026-03-08 |
| **Autor** | CISO / CTO |
| **Aprobado por** | CEO |

---

# 1. Objetivo

Definir el proceso de adquisición, inscripción en Microsoft Intune, configuración de seguridad y entrega de portátiles MacBook corporativos, garantizando el cumplimiento de los requisitos de seguridad del ENS.

---

# 2. Alcance

Este procedimiento aplica a todos los MacBook adquiridos para uso corporativo por empleados de optimTech. Todos los equipos se gestionan de forma centralizada mediante **Microsoft Intune** como solución MDM (Mobile Device Management).

---

# 3. Roles y responsabilidades

| Rol | Responsabilidad |
|-----|-----------------|
| CEO | Aprueba la compra del equipo |
| CTO / CISO | Realiza la inscripción en Intune, configuración técnica y supervisión de cumplimiento |
| Empleado | Custodia del equipo y cumplimiento de las políticas de uso |

---

# 4. Adquisición

1. El Manager o CISO realiza la solicitud de compra, autorizada por el CEO.
2. Comprar a proveedor autorizado (Apple Store, distribuidor oficial).
3. Registrar el equipo en **D05 Activos de Seguridad de la Información** con:
   - Número de serie
   - Modelo
   - Fecha de compra
   - Usuario asignado
4. Archivar la factura de compra.

---

# 5. Inscripción en Microsoft Intune

1. Registrar el equipo en **Apple Business Manager** (ABM) para habilitar la inscripción automática (Automated Device Enrollment).
2. Asignar el dispositivo al perfil de inscripción de Intune correspondiente.
3. Al encender el equipo por primera vez, el Asistente de Configuración de macOS guiará la inscripción automática en Intune.
4. Verificar en el portal de Intune que el dispositivo aparece como **Conforme** y que los perfiles de configuración se han aplicado correctamente.

---

# 6. Políticas aplicadas automáticamente por Intune

Las siguientes políticas de seguridad se despliegan de forma centralizada a través de perfiles de configuración de Intune. **No requieren configuración manual** en el equipo:

| Control | Política Intune | Detalle |
|---------|-----------------|---------|
| Cifrado de disco | FileVault | Activación forzada con custodia de clave de recuperación en Intune |
| Firewall | Firewall de macOS | Activado y configurado para bloquear conexiones entrantes no autorizadas |
| Bloqueo de pantalla | Perfil de restricciones | Bloqueo automático tras 5 minutos de inactividad; contraseña requerida |
| Requisitos de contraseña | Perfil de contraseña | Longitud mínima, complejidad y caducidad según política corporativa |
| Actualizaciones de macOS | Perfil de actualización | Actualizaciones automáticas de seguridad y del sistema operativo |
| Inicio de sesión automático | Perfil de restricciones | Deshabilitado |
| Gatekeeper | Perfil de restricciones | Solo permite apps de App Store y desarrolladores identificados |
| Cuenta sin privilegios admin | Perfil de inscripción | El usuario se crea sin rol de administrador local |

> **Nota:** La custodia centralizada de claves FileVault en Intune garantiza la recuperación del equipo en caso de pérdida de la contraseña del usuario.

---

# 7. Configuración adicional (manual)

Una vez inscrito en Intune y verificado el cumplimiento, el CTO/CISO completa:

1. Instalar software corporativo base (si no se despliega vía Intune):
   - Microsoft 365 (Word, Excel, PowerPoint, Outlook, Teams)
   - Navegador corporativo
   - Herramientas de comunicación
2. Configurar la cuenta de email corporativa en Outlook.
3. Configurar **copias de seguridad** (Time Machine local o equivalente cloud) si aplica.

---

# 8. Entrega

1. Rellenar formulario **I03** con los datos del equipo (número de serie, modelo).
2. El empleado firma el formulario I03.
3. Entregar el equipo con cargador y accesorios.
4. Archivar el I03 firmado (PDF) en `06_EVIDENCIAS/personal/`.

---

# 9. Control y mantenimiento

1. Revisar periódicamente el **estado de cumplimiento** del dispositivo en el portal de Intune.
2. Las actualizaciones de macOS se gestionan automáticamente a través de Intune; verificar que se aplican correctamente.
3. Registrar cualquier incidencia de seguridad según **P05 Gestión de Incidentes de Seguridad**.
4. En caso de baja del empleado: seguir procedimiento **I04 Devolución de dispositivos** y realizar un **borrado remoto (wipe)** del equipo desde Intune.

---

# 10. Acciones remotas disponibles vía Intune

En caso necesario, el CTO/CISO puede ejecutar las siguientes acciones remotas desde el portal de Intune:

| Acción | Uso |
|--------|-----|
| **Borrado remoto (Wipe)** | Pérdida, robo o baja del empleado |
| **Bloqueo remoto** | Sospecha de acceso no autorizado |
| **Rotación de clave FileVault** | Compromiso de la clave de recuperación |
| **Reinicio del código de acceso** | Empleado olvida la contraseña |
| **Sincronización forzada** | Forzar la aplicación inmediata de políticas actualizadas |

---

# 11. Referencias

| Documento | Descripción |
|-----------|-------------|
| P02 | Adquisición de componentes y servicios TIC |
| I03 | Registro entrega dispositivos |
| I04 | Devolución de dispositivos |
| D05 | Activos de Seguridad de la Información |
| P05 | Gestión de Incidentes de Seguridad |

---

**Fin del Procedimiento**
