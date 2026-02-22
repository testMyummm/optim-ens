# Procedimientos Aplicados — Catálogo

Procedimientos operativos específicos por herramienta y plataforma (SOPs). Complementan los procedimientos marco del ENS (`03_PROCEDIMIENTOS/`) con instrucciones detalladas para la operación diaria de los sistemas de información.

## Convención de nomenclatura: `PA-DDD-NNN`

- **PA** = Procedimiento Aplicado
- **DDD** = Código de dominio (3 letras)
- **NNN** = Número secuencial dentro del dominio (001–999)

Ejemplo: `PA-BKP-001 Backup y Restauración Confluence Cloud.md`

## Dominios

| Código | Carpeta | Alcance |
|--------|---------|---------|
| BKP | `backup_recuperacion/` | Backup, restauración, recuperación ante desastres |
| ACC | `gestion_accesos/` | Provisión de usuarios, permisos, SSO, IAM |
| INF | `infraestructura/` | Infraestructura cloud, servidores, almacenamiento, red |
| DEV | `desarrollo/` | CI/CD pipelines, repositorios, herramientas de desarrollo, despliegues |
| MON | `monitorizacion/` | Monitorización, logging, alertas, observabilidad |
| COM | `comunicaciones/` | Red, VPN, firewalls, correo, mensajería |
| EPT | `gestion_endpoints/` | Portátiles, dispositivos móviles, MDM, BYOD |

Para añadir un nuevo dominio: crear la carpeta correspondiente y añadir el código a esta tabla.

## Formato de documentos

- **Fuente de verdad:** Markdown (`.md`) en la carpeta del dominio
- **Copias formales:** `.docx` generados bajo demanda con la plantilla corporativa, almacenados en `<dominio>/docx/`

## Catálogo de procedimientos

| ID | Título | Dominio | Plataforma | Estado | Última revisión |
|----|--------|---------|------------|--------|-----------------|
| PA-BKP-001 | Backup y Restauración Confluence Cloud | BKP | Atlassian | Vigente | 2026-02-22 |
