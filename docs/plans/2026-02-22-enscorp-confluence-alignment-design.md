# ENSCORP Confluence Alignment Design

**Date**: 2026-02-22
**Status**: Approved
**Scope**: Align ENSCORP Confluence space with local ENS git repository structure

## Context

optimTech maintains ENS (Esquema Nacional de Seguridad) nivel medio compliance documentation in two locations:

1. **Local git repository** (~80+ documents, 10 categories, proven through 2025 certification cycle)
2. **ENSCORP Confluence space** (~21 pages, 7 folders, created 2025-11-24, nascent skeleton)

The local repo is the mature, authoritative source. Confluence needs to become the living knowledge base while git remains the canonical store for binary documents (.docx, .xlsx, .pdf) and version control.

## Decisions

1. **Confluence = living knowledge base** for collaborative, operational content
2. **Git = canonical store** for formal binary documents and version control
3. **Local structure wins** — replicate the 01-10 folder taxonomy into Confluence
4. **Existing ENSCORP content** → temporary `99_Legacy` section, migrated iteratively
5. **Living vs. stub** distinction determines what gets full content in Confluence vs. just metadata + links

## Target Confluence Structure

```
ENSCORP (Root)
├── Index                              ← Navigation hub (update existing)
│
├── 01. Políticas                      ← STUB pages (link to git .docx)
│   ├── D01 Política de Seguridad de la Información
│   ├── D02 Política de Clasificación de la Información
│   ├── D03 Directrices de Seguridad de la Información
│   └── D10 Política de Protección de Datos Personales
│
├── 02. Normas                         ← STUB pages (link to git .docx)
│   ├── I01 Normativa de Seguridad de la Información
│   ├── I02 Anexos de Protección de Datos (ES/CA, Laboral/Profesional)
│   ├── I03 Registro entrega dispositivos
│   ├── I04 Registro devolución dispositivos
│   └── I05 Autorización BYOD
│
├── 03. Procedimientos Operativos      ← LIVING PAGES (full content)
│   ├── P01 Gestión de Riesgos
│   ├── P02 Adquisición de componentes TIC
│   ├── P03 Gestión de Cambios
│   ├── P04 Gestión de Usuarios
│   ├── P05 Gestión de Incidentes
│   └── Desarrollo Software (mp.sw.1/mp.sw.2)
│
├── 04. Registros y Controles          ← MIXED (stubs for .xlsx, living for controls)
│   ├── D00 Lista de información documentada (→ git .xlsx)
│   ├── D04 Categorización y Declaración de Aplicabilidad (→ git .xlsx)
│   ├── D05 Activos de Seguridad (→ git .xlsx)
│   ├── D06 Riesgos de Seguridad (→ git .xlsx)
│   ├── D07 BIA (→ git .xlsx)
│   ├── D09 Mejora Continua (→ git .xlsx)
│   ├── D11 RAT (→ git .xlsx)
│   ├── D12 Medidas de Cumplimiento ENS (→ git .xlsx)
│   ├── D13 Marco Normativo (→ git .xlsx)
│   └── Adquisiciones/
│       ├── Atlassian
│       ├── Azure
│       └── GCP
│
├── 05. Roles y Responsabilidades      ← STUB pages (link to git .docx)
│   ├── DPT01 CISO
│   ├── DPT02 CTO
│   ├── DPT03 DPO
│   ├── DPT04 CEO
│   └── DPT05 Auditor Interno
│
├── 06. Evidencias                     ← LIVING PAGES (evidence tracking)
│   ├── Personal/
│   ├── Proveedores/
│   └── Controles/
│
├── 07. Auditoría                      ← STUB + living audit tracking
│   ├── Informes de Auditoría (→ git PDFs)
│   ├── Plan de Auditoría (→ git PDF)
│   └── Acreditaciones
│
├── 08. Gobernanza                     ← LIVING PAGES (full content)
│   ├── Actas Comité Seguridad
│   ├── Nombramientos
│   ├── Organigrama
│   ├── Plan de Concienciación
│   └── Guía de Incorporación ENS
│
├── 09. Normativa Externa              ← Reference/link pages
│   └── Marco normativo y CCN-STIC
│
├── 10. Procedimientos Aplicados (SOPs) ← LIVING PAGES
│   └── PA-BKP-001 Backup y Restauración Confluence Cloud
│
├── Plantillas                         ← Merge local + existing Confluence templates
│
└── 99. Legacy                         ← Existing content pending reclassification
    ├── CVSS + Valoración CIDTA
    ├── Recomendaciones póstumas auditoría 1
    ├── Existing policies (2.6-2.10)
    └── Control 1.X pages
```

### Content Type Definitions

| Type | Source of Truth | Confluence Content | Examples |
|------|----------------|-------------------|----------|
| **LIVING** | Confluence | Full native content, actively edited | Procedures, Governance, SOPs, Evidence tracking |
| **STUB** | Git (.docx/.xlsx/.pdf) | Metadata + summary + link to git file | Policies, Norms, Roles, Audit reports |
| **MIXED** | Both | Stubs for spreadsheets, living for descriptive content | Registros section |

## Local Repo Changes

### New: `confluence_map.md`

Root-level mapping file tracking Confluence page IDs and sync directions:

```markdown
| Local Path | Confluence Page ID | Page Type | Sync Direction |
|------------|-------------------|-----------|----------------|
| 01_POLITICAS/D01*.docx | XXXXXXX | stub | git → confluence |
| 03_PROCEDIMIENTOS/P01*.docx | XXXXXXX | living | confluence ← → git |
```

Sync directions:
- `git → confluence`: Git is canonical, Confluence shows metadata/link
- `confluence → git`: Confluence is canonical for content, git stores .docx export
- `bidirectional`: Avoid when possible

### Updated: `CLAUDE.md`

Add documentation about:
- ENSCORP as the living knowledge base
- Mapping file location and usage
- Content type rules (living vs. stub)

### No structural changes to existing folders

The `01_`-`10_` folder structure stays exactly as-is.

## ENS Nivel Medio Control Family Coverage

| Control Family | Code | Local Location | Confluence Type |
|---|---|---|---|
| Marco organizativo | org.1-org.4 | 01_POLITICAS + 08_GOBERNANZA | stub + living |
| Planificación | op.pl.1-op.pl.5 | 04_REGISTROS + 07_AUDITORIA | stub |
| Control de acceso | op.acc.1-op.acc.6 | 03_PROCEDIMIENTOS + 02_NORMAS | living + stub |
| Explotación | op.exp.1-op.exp.10 | 03_PROCEDIMIENTOS + 04_REGISTROS | living + stub |
| Servicios externos | op.ext.1-op.ext.2 | 03_PROCEDIMIENTOS + 04_REGISTROS | living + stub |
| Continuidad | op.cont.1-op.cont.3 | 04_REGISTROS + 10_SOPs | stub + living |
| Monitorización | op.mon.1-op.mon.3 | 04_REGISTROS + 06_EVIDENCIAS | stub + living |
| Instalaciones | mp.if.1-mp.if.7 | 06_EVIDENCIAS/proveedores | living |
| Personal | mp.per.1-mp.per.4 | 05_ROLES + 02_NORMAS + 08_GOBERNANZA | stub + living |
| Equipamiento | mp.eq.1-mp.eq.3 | 02_NORMAS | stub |
| Comunicaciones | mp.com.1-mp.com.4 | 07_AUDITORIA | stub |
| Información | mp.info.1-mp.info.6 | 01_POLITICAS + 04_REGISTROS | stub |
| Servicios | mp.s.1-mp.s.2 | 06_EVIDENCIAS + 04_REGISTROS | living + stub |
| Software | mp.sw.1-mp.sw.2 | 03_PROCEDIMIENTOS | living |

## Legacy Content Migration Plan

Existing ENSCORP pages will be moved to `99_Legacy` and migrated iteratively:

| Existing Page | Target Section | Action |
|---|---|---|
| Política 2.6 Desarrollo Seguro | 03. Procedimientos | Merge with mp.sw.1/mp.sw.2 |
| Política 2.7 Proveedores y Terceros | 03. Procedimientos | Merge with P02 |
| Política 2.8 Protección de Datos | 01. Políticas | Merge with D10 |
| Política 2.9 Gestión de Cambios | 03. Procedimientos | Merge with P03 |
| Política 2.10 Clasificación Info | 01. Políticas | Merge with D02 |
| Gestión de Accesos | 03. Procedimientos | Merge with P04 |
| Gestión de Vulnerabilidades y Parches | 03. Procedimientos | New living page |
| CVSS + Valoración CIDTA | 04. Registros | Risk assessment tool |
| Acta de Prueba de Restauración | 10. SOPs | Evidence for op.cont |
| Recomendaciones póstumas auditoría 1 | 07. Auditoría | Post-audit follow-up |

## Confluence Space Reference

| Field | Value |
|-------|-------|
| Space Key | ENSCORP |
| Space ID | 7372801 |
| Cloud ID | 7273cac1-89f9-4a5a-8f62-e245961125ae |
| Homepage ID | 7372803 |
| Base URL | https://optimtech-team-a36pyv7e.atlassian.net/wiki |
