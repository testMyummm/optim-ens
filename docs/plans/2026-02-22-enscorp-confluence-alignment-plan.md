# ENSCORP Confluence Alignment — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restructure the ENSCORP Confluence space to mirror the local git repo's 01-10 folder taxonomy, creating living pages for operational content and stub pages for formal documents.

**Architecture:** The ENSCORP Confluence space (knowledge base type) gets a full set of section pages matching local folders `01_`–`10_` plus `Plantillas` and `99_Legacy`. Each section page is a parent container holding child pages that map 1:1 to local documents. Existing content is moved under `99_Legacy` for iterative migration. A local `confluence_map.md` file tracks page IDs and sync directions.

**Tech Stack:** Confluence REST API v2 (via Atlassian MCP tools), Markdown, Git

**Reference:** Design doc at `docs/plans/2026-02-22-enscorp-confluence-alignment-design.md`

**Constants used throughout this plan:**
- `cloudId`: `7273cac1-89f9-4a5a-8f62-e245961125ae`
- `spaceId`: `7372801`
- `rootPageId (homepage)`: `7372803`

**Existing page IDs (for moving to Legacy):**
- Index: `7372864`
- Folder "1. Gobierno y Cumplimiento": `7373166` (child: `7373171`)
- Folder "2. Políticas": `7373167` (children: `7372820`, `7372830`, `7372815`, `7372841`, `7372810`)
- Folder "3. Procedimientos Operativos": `7373169` (child folder: `7373165`, page: `7372805`)
- Folder "4. Controles ENS y evidencias": `7373164` (child folder: `7373170`, pages: `7372848`, `7372895`, `7372903`, `7372890`, `7372918`)
- Folder "10. Plantillas y documentos": `7373168` (pages: `7372885`, `7372854`, `7372859`, `7372875`, `7372825`)
- CVSS: `7372908` (child: `7372880`)
- Recomendaciones póstumas auditoría 1: `7372913`
- Untitled draft: `7372923`

---

## Phase 1: Local Repo Preparation

### Task 1: Create `confluence_map.md` skeleton

**Files:**
- Create: `confluence_map.md` (repo root)

**Step 1: Create the mapping file with headers and placeholder rows**

Write the file with the full list of local documents and placeholder page IDs (`TBD`). Include all files from `01_POLITICAS` through `10_PROCEDIMIENTOS_APLICADOS` plus `PLANTILLAS`.

```markdown
# Confluence Mapping — ENSCORP Space

> This file tracks the relationship between local git files and their corresponding Confluence pages in the ENSCORP space.
>
> - **Space Key:** ENSCORP
> - **Space ID:** 7372801
> - **Cloud ID:** 7273cac1-89f9-4a5a-8f62-e245961125ae
> - **Base URL:** https://optimtech-team-a36pyv7e.atlassian.net/wiki

## Sync Direction Legend

| Direction | Meaning |
|-----------|---------|
| `git → confluence` | Git is canonical. Confluence page shows metadata + link. |
| `confluence → git` | Confluence is canonical. Git stores .docx export for audit. |

## Section Pages

| Section | Confluence Page ID | Page Type |
|---------|-------------------|-----------|
| 01. Políticas | TBD | section (stub children) |
| 02. Normas | TBD | section (stub children) |
| 03. Procedimientos Operativos | TBD | section (living children) |
| 04. Registros y Controles | TBD | section (mixed children) |
| 05. Roles y Responsabilidades | TBD | section (stub children) |
| 06. Evidencias | TBD | section (living children) |
| 07. Auditoría | TBD | section (mixed children) |
| 08. Gobernanza | TBD | section (living children) |
| 09. Normativa Externa | TBD | section (stub children) |
| 10. Procedimientos Aplicados (SOPs) | TBD | section (living children) |
| Plantillas | TBD | section |
| 99. Legacy | TBD | section (archive) |

## Document Pages

| Local Path | Confluence Page ID | Page Type | Sync Direction |
|------------|-------------------|-----------|----------------|
| `01_POLITICAS/D01 Política de Seguridad de la Información.docx` | TBD | stub | git → confluence |
| `01_POLITICAS/D02 Política de Clasificación de la Información.docx` | TBD | stub | git → confluence |
| `01_POLITICAS/D03 Directrices de Seguridad de la Información.docx` | TBD | stub | git → confluence |
| `01_POLITICAS/D10 Política de Protección de Datos Personales.docx` | TBD | stub | git → confluence |
| `02_NORMAS/I01 Normativa de Seguridad de la Información.docx` | TBD | stub | git → confluence |
| `02_NORMAS/I02 (ES/CA Laboral/Profesional variants)` | TBD | stub | git → confluence |
| `02_NORMAS/I03 Registro entrega dispositivos de trabajo.docx` | TBD | stub | git → confluence |
| `02_NORMAS/I04 Registro devolución dispositivos de trabajo.docx` | TBD | stub | git → confluence |
| `02_NORMAS/I05 Autorización uso equipos particulares BYOD.docx` | TBD | stub | git → confluence |
| `03_PROCEDIMIENTOS/P01 Gestión de Riesgos de Seguridad de la Información.docx` | TBD | living | confluence → git |
| `03_PROCEDIMIENTOS/P02 Adquisición de componentes y servicios TIC.docx` | TBD | living | confluence → git |
| `03_PROCEDIMIENTOS/P03 Gestión de Cambios.docx` | TBD | living | confluence → git |
| `03_PROCEDIMIENTOS/P04 Gestión de Usuarios.docx` | TBD | living | confluence → git |
| `03_PROCEDIMIENTOS/P05 Gestión de Incidentes.docx` | TBD | living | confluence → git |
| `03_PROCEDIMIENTOS/[mp.sw.1][mp.sw.2] Desarrollo software.docx` | TBD | living | confluence → git |
| `04_REGISTROS/D00 Lista de informacion documentada.xlsx` | TBD | stub | git → confluence |
| `04_REGISTROS/D04 Categorización y Declaración de Aplicabilidad ENS.xlsx` | TBD | stub | git → confluence |
| `04_REGISTROS/D05 Activos de Seguridad de la Informacion.xlsx` | TBD | stub | git → confluence |
| `04_REGISTROS/D06 Riesgos de Seguridad de la Información.xlsx` | TBD | stub | git → confluence |
| `04_REGISTROS/D07 BIA-Business Impact Analysis.xlsx` | TBD | stub | git → confluence |
| `04_REGISTROS/D09 Registro de Iniciativas de Mejora Continua.xlsx` | TBD | stub | git → confluence |
| `04_REGISTROS/D11 RAT-Registro de Actividades de Tratamiento.xlsx` | TBD | stub | git → confluence |
| `04_REGISTROS/D12 Medidas de Cumplimiento ENS.xlsx` | TBD | stub | git → confluence |
| `04_REGISTROS/D13 Marco Normativo Aplicable.xlsx` | TBD | stub | git → confluence |
| `04_REGISTROS/Adquisición Atlassian.docx` | TBD | stub | git → confluence |
| `04_REGISTROS/Adquisición Azure.docx` | TBD | stub | git → confluence |
| `04_REGISTROS/Adquisición GCP.docx` | TBD | stub | git → confluence |
| `05_ROLES/DPT01 - Responsable de seguridad información-CISO.docx` | TBD | stub | git → confluence |
| `05_ROLES/DPT02 - Director de Tecnología-CTO.docx` | TBD | stub | git → confluence |
| `05_ROLES/DPT03 - Responsable de protección de datos.docx` | TBD | stub | git → confluence |
| `05_ROLES/DPT04 - Director General-CEO.docx` | TBD | stub | git → confluence |
| `05_ROLES/DPT05 - Auditor interno.docx` | TBD | stub | git → confluence |
| `06_EVIDENCIAS/personal/` | TBD | living | confluence → git |
| `06_EVIDENCIAS/proveedores/` | TBD | living | confluence → git |
| `06_EVIDENCIAS/controles/` | TBD | living | confluence → git |
| `07_AUDITORIA/ (informes)` | TBD | stub | git → confluence |
| `07_AUDITORIA/ (plan)` | TBD | stub | git → confluence |
| `07_AUDITORIA/ (acreditaciones)` | TBD | stub | git → confluence |
| `08_GOBERNANZA/Actas Comité Seguridad` | TBD | living | confluence → git |
| `08_GOBERNANZA/Nomenaments responsables seguretat.docx` | TBD | living | confluence → git |
| `08_GOBERNANZA/Organigrama servicios y dept afectados.docx` | TBD | living | confluence → git |
| `08_GOBERNANZA/Pla conscienciació seguretat.docx` | TBD | living | confluence → git |
| `08_GOBERNANZA/Guia de Incorporacion - Principios ENS.docx` | TBD | living | confluence → git |
| `09_NORMATIVA_EXTERNA/normativa_seguridad_info.pdf` | TBD | stub | git → confluence |
| `10_PROCEDIMIENTOS_APLICADOS/backup_recuperacion/PA-BKP-001` | TBD | living | confluence → git |
```

**Step 2: Commit**

```bash
git add confluence_map.md
git commit -m "feat: add confluence_map.md skeleton for ENSCORP alignment"
```

---

### Task 2: Update `CLAUDE.md` with Confluence integration docs

**Files:**
- Modify: `CLAUDE.md`

**Step 1: Add Confluence integration section after the "Atlassian Access" section**

Add the following after the existing `## Atlassian Access` section:

```markdown
## Confluence Integration (ENSCORP)

The ENSCORP Confluence space is the **living knowledge base** for ENS documentation. The local git repo is the **canonical store** for formal binary documents (.docx, .xlsx, .pdf).

### Content Types

| Type | Source of Truth | Where to Edit | Examples |
|------|----------------|---------------|----------|
| **Living** | Confluence | Edit in Confluence; export .docx to git periodically | Procedures (03), Governance (08), SOPs (10), Evidence (06) |
| **Stub** | Git (.docx/.xlsx/.pdf) | Edit locally; Confluence page has metadata + link | Policies (01), Norms (02), Roles (05), Audit (07), External Regs (09) |
| **Mixed** | Both | Spreadsheets in git, descriptions in Confluence | Registros (04) |

### Mapping File

`confluence_map.md` at the repo root tracks the relationship between local files and Confluence page IDs. Update it whenever pages are created or reorganized.

### Rules

- Living pages: Content is authored and maintained in Confluence. Git stores a .docx export for offline/audit purposes.
- Stub pages: Content is authored locally as .docx/.xlsx. Confluence page shows metadata, summary, and a reference note.
- When creating new documents, add entries to both the appropriate local folder AND `confluence_map.md`.
```

**Step 2: Update the Directory Structure section**

Add `10_PROCEDIMIENTOS_APLICADOS/` to the directory structure listing (it exists locally but is missing from CLAUDE.md):

```
├── 10_PROCEDIMIENTOS_APLICADOS/ # Applied procedures / SOPs
```

**Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: add Confluence integration section and update directory structure in CLAUDE.md"
```

---

## Phase 2: Confluence Structure — Create Section Pages

> **Note on Confluence knowledge base spaces:** The existing ENSCORP space uses "folder" type containers. Through the API, we create regular pages as section containers. If the UI requires converting them to folders later, that can be done manually. The hierarchy (parent-child) works identically for pages and folders.

### Task 3: Create the `99. Legacy` section and move existing content

This must happen first so we have a place for existing pages before reorganizing.

**Step 1: Create the `99. Legacy` section page**

Use `createConfluencePage` with:
- `cloudId`: `7273cac1-89f9-4a5a-8f62-e245961125ae`
- `spaceId`: `7372801`
- `parentId`: `7372803` (root/homepage)
- `title`: `99. Legacy`
- `contentFormat`: `markdown`
- `body`:

```markdown
# 99. Legacy — Contenido Pendiente de Reclasificación

Esta sección contiene el contenido original del espacio ENSCORP anterior a la reestructuración de febrero 2026. Las páginas aquí serán revisadas e integradas progresivamente en las secciones 01-10.

## Estado

| Página Original | Sección Destino | Estado |
|----------------|-----------------|--------|
| Política 2.6 Desarrollo Seguro | 03. Procedimientos | Pendiente |
| Política 2.7 Proveedores y Terceros | 03. Procedimientos | Pendiente |
| Política 2.8 Protección de Datos | 01. Políticas | Pendiente |
| Política 2.9 Gestión de Cambios | 03. Procedimientos | Pendiente |
| Política 2.10 Clasificación Info | 01. Políticas | Pendiente |
| Gestión de Accesos | 03. Procedimientos | Pendiente |
| Gestión de Vulnerabilidades y Parches | 03. Procedimientos | Pendiente |
| CVSS + Valoración CIDTA | 04. Registros | Pendiente |
| Acta de Prueba de Restauración | 10. SOPs | Pendiente |
| Recomendaciones póstumas auditoría 1 | 07. Auditoría | Pendiente |
```

Record the returned page ID.

**Step 2: Move existing root-level content pages under `99. Legacy`**

For each of these pages, use `updateConfluencePage` to set `parentId` to the `99. Legacy` page ID:

- `7372908` (CVSS) — also brings child `7372880` (Valoración CIDTA)
- `7372913` (Recomendaciones póstumas auditoría 1)

**Step 3: Move existing folder contents under `99. Legacy`**

Move the content pages (not the folders themselves) that currently sit under old numbered folders. Use `updateConfluencePage` with new `parentId` = `99. Legacy` page ID:

From "2. Políticas" (`7373167`):
- `7372820` (Política 2.6)
- `7372830` (Política 2.7)
- `7372815` (Política 2.8)
- `7372841` (Política 2.9)
- `7372810` (Política 2.10)

From "3. Procedimientos Operativos" → "3.1 Gestión de Accesos":
- `7372805` (Altas, bajas y modificaciones)

From "4. Controles ENS y evidencias":
- `7372848` (Control 1.X)
- `7372895` (Duplicate of Control 1.X)
- `7372903` (Acta de Prueba de Restauración)
- `7372890` (Gestión de Accesos)
- `7372918` (Gestión de Vulnerabilidades y Parches)

From "10. Plantillas y documentos":
- `7372885` (Plantilla: Política ENS)
- `7372854` (Plantilla: Procedimiento Operativo ENS)
- `7372859` (Plantilla Matriz de Controles ENS)
- `7372875` (Plantilla: Registro de Incidentes)
- `7372825` (POL-IA-EXT-ENS-M)

**Step 4: Verify all content pages are now under `99. Legacy`**

Use `getConfluencePageDescendants` on the `99. Legacy` page to confirm all pages landed correctly.

---

### Task 4: Create section pages 01-10 + Plantillas

Create 12 section pages, all as children of the root page (`7372803`). Each is a container with a brief description of its purpose.

**Step 1: Create all section pages**

Use `createConfluencePage` for each. All share:
- `cloudId`: `7273cac1-89f9-4a5a-8f62-e245961125ae`
- `spaceId`: `7372801`
- `parentId`: `7372803`
- `contentFormat`: `markdown`

Create them in this order (record each returned page ID):

**01. Políticas**
```markdown
# 01. Políticas

Políticas estratégicas de seguridad de la información. Documentos formales cuyo original se mantiene en formato .docx en el repositorio git.

**Tipo de contenido:** STUB — Las páginas hijas contienen metadatos y referencia al documento canónico en git.

| Documento | Código | Controles ENS |
|-----------|--------|---------------|
| Política de Seguridad de la Información | D01 | org.1, org.2, org.3 |
| Política de Clasificación de la Información | D02 | mp.info.2 |
| Directrices de Seguridad de la Información | D03 | org.4 |
| Política de Protección de Datos Personales | D10 | mp.info.1, mp.info.6 |
```

**02. Normas**
```markdown
# 02. Normas

Normativas, instrucciones y formularios. Documentos formales en formato .docx (versiones ES y CA disponibles).

**Tipo de contenido:** STUB

| Documento | Código | Descripción |
|-----------|--------|-------------|
| Normativa de Seguridad de la Información | I01 | Normativa general firmada por empleados |
| Anexos de Protección de Datos | I02 | Laboral y Profesional, ES y CA |
| Registro entrega dispositivos | I03 | Control de equipamiento mp.eq |
| Registro devolución dispositivos | I04 | Control de equipamiento mp.eq |
| Autorización BYOD | I05 | Uso de equipos particulares mp.eq.3 |
```

**03. Procedimientos Operativos**
```markdown
# 03. Procedimientos Operativos

Procedimientos operacionales de seguridad. **Contenido vivo** — se edita y mantiene directamente en Confluence.

**Tipo de contenido:** LIVING

| Procedimiento | Código | Controles ENS |
|--------------|--------|---------------|
| Gestión de Riesgos de Seguridad | P01 | op.pl.1 |
| Adquisición de componentes y servicios TIC | P02 | op.ext.1, op.ext.2 |
| Gestión de Cambios | P03 | op.exp.5 |
| Gestión de Usuarios | P04 | op.acc.1-op.acc.6 |
| Gestión de Incidentes | P05 | op.exp.7 |
| Desarrollo Software | mp.sw.1, mp.sw.2 | mp.sw.1, mp.sw.2 |
```

**04. Registros y Controles**
```markdown
# 04. Registros y Controles

Registros de cumplimiento y controles ENS. Los registros en formato .xlsx se mantienen en git; las páginas de control son contenido vivo.

**Tipo de contenido:** MIXED

| Registro | Código | Formato |
|----------|--------|---------|
| Lista de información documentada | D00 | .xlsx → git |
| Categorización y Declaración de Aplicabilidad | D04 | .xlsx → git |
| Activos de Seguridad | D05 | .xlsx → git |
| Riesgos de Seguridad | D06 | .xlsx → git |
| BIA - Business Impact Analysis | D07 | .xlsx → git |
| Mejora Continua | D09 | .xlsx → git |
| RAT - Registro de Actividades de Tratamiento | D11 | .xlsx → git |
| Medidas de Cumplimiento ENS | D12 | .xlsx → git |
| Marco Normativo Aplicable | D13 | .xlsx → git |
| Adquisiciones (Atlassian, Azure, GCP) | — | .docx → git |
```

**05. Roles y Responsabilidades**
```markdown
# 05. Roles y Responsabilidades

Descripciones de puestos de trabajo con responsabilidades de seguridad. Documentos formales en .docx, firmados en .pdf.

**Tipo de contenido:** STUB

| Rol | Código | Responsabilidad Principal |
|-----|--------|--------------------------|
| CISO | DPT01 | Responsable de seguridad de la información |
| CTO | DPT02 | Director de Tecnología |
| DPO | DPT03 | Responsable de protección de datos |
| CEO | DPT04 | Director General |
| Auditor Interno | DPT05 | Auditoría interna SGSI |
```

**06. Evidencias**
```markdown
# 06. Evidencias

Pruebas de implementación de controles ENS. **Contenido vivo** — se actualiza con cada ciclo de evidencia.

**Tipo de contenido:** LIVING

| Subcategoría | Contenido |
|-------------|-----------|
| Personal | Documentos firmados por empleados (PDFs en git) |
| Proveedores | Certificaciones de proveedores cloud (Azure, GCP) |
| Controles | Capturas de pantalla y descripciones de implementación |
```

**07. Auditoría**
```markdown
# 07. Auditoría

Documentación de auditorías internas y externas. Informes formales en git; seguimiento vivo en Confluence.

**Tipo de contenido:** MIXED (stubs para informes PDF, living para seguimiento)

| Documento | Formato | Tipo |
|-----------|---------|------|
| Informes de Auditoría | PDF → git | stub |
| Plan de Auditoría | PDF → git | stub |
| Acreditaciones | PDF → git | stub |
```

**08. Gobernanza**
```markdown
# 08. Gobernanza

Documentación de gobierno de seguridad: actas del comité, nombramientos, organigrama, concienciación. **Contenido vivo** — se edita y mantiene en Confluence.

**Tipo de contenido:** LIVING

| Documento | Descripción |
|-----------|-------------|
| Actas Comité Seguridad | Actas de reuniones del comité de seguridad |
| Nombramientos | Nombramientos de responsables de seguridad |
| Organigrama | Organigrama de servicios y departamentos afectados |
| Plan de Concienciación | Plan de concienciación en seguridad |
| Guía de Incorporación ENS | Guía para nuevos empleados sobre principios ENS |
```

**09. Normativa Externa**
```markdown
# 09. Normativa Externa

Referencias a normativa externa aplicable: RD 311/2022, guías CCN-STIC, RGPD, y otra legislación relevante.

**Tipo de contenido:** STUB — referencias y enlaces

| Referencia | Descripción |
|-----------|-------------|
| Marco normativo de seguridad | Compilación de normativa aplicable |
| CCN-STIC | Guías técnicas del Centro Criptológico Nacional |
```

**10. Procedimientos Aplicados (SOPs)**
```markdown
# 10. Procedimientos Aplicados (SOPs)

Procedimientos operativos aplicados — instrucciones paso a paso para operaciones de seguridad. **Contenido vivo**.

**Tipo de contenido:** LIVING

| SOP | Código | Alcance |
|-----|--------|---------|
| Backup y Restauración Confluence Cloud | PA-BKP-001 | op.cont.1, op.cont.2 |
```

**Plantillas**
```markdown
# Plantillas

Plantillas de documentos ENS para la creación de nuevos documentos de seguridad.

| Plantilla | Uso |
|-----------|-----|
| Plantilla ENS genérica | Base para cualquier documento ENS |
| Plantilla ENS (alternativa) | Formato alternativo |
| PR-020 Procedimiento Desarrollo Software | Plantilla para procedimientos de desarrollo |
```

**Step 2: Record all returned page IDs**

After creating all 12 section pages, update `confluence_map.md` with the actual page IDs in the Section Pages table.

**Step 3: Commit mapping file update**

```bash
git add confluence_map.md
git commit -m "feat: record section page IDs in confluence_map.md"
```

---

## Phase 3: Confluence Structure — Create Stub Pages

Stub pages follow a consistent template. Each stub contains: document title, code, description, ENS control references, file location in git, and last known version date.

### Task 5: Create stub pages under `01. Políticas`

Create 4 child pages under the `01. Políticas` section page.

**Stub template for policies:**

```markdown
# [Title]

| Campo | Valor |
|-------|-------|
| **Código** | [code] |
| **Tipo** | Política |
| **Formato canónico** | .docx (repositorio git) |
| **Ruta en git** | `01_POLITICAS/[filename]` |
| **Controles ENS** | [controls] |
| **Última revisión** | 2025 (ciclo certificación) |

## Resumen

[1-2 sentence summary of the policy's purpose]

---

> **Nota:** Este documento se mantiene en formato .docx en el repositorio git. Esta página sirve como referencia y punto de acceso dentro del sistema de gestión documental.
```

**Pages to create** (all with `parentId` = `01. Políticas` page ID):

1. **D01 Política de Seguridad de la Información**
   - Controls: org.1, org.2, org.3
   - Summary: Define el marco general de seguridad de la información, los principios, objetivos y la organización de la seguridad en optimTech.

2. **D02 Política de Clasificación de la Información**
   - Controls: mp.info.2
   - Summary: Establece los criterios para clasificar la información según su nivel de sensibilidad y las medidas de protección correspondientes.

3. **D03 Directrices de Seguridad de la Información**
   - Controls: org.4
   - Summary: Directrices operativas que desarrollan la política de seguridad con instrucciones concretas para su implementación.

4. **D10 Política de Protección de Datos Personales**
   - Controls: mp.info.1, mp.info.6
   - Summary: Política de cumplimiento con el RGPD y la LOPDGDD integrada con los requisitos del ENS para protección de datos personales.

Record all page IDs and update `confluence_map.md`.

---

### Task 6: Create stub pages under `02. Normas`

Create 5 child pages under `02. Normas`.

**Pages to create:**

1. **I01 Normativa de Seguridad de la Información**
   - Controls: org.4, mp.per.2
   - Summary: Normativa general de seguridad que todo el personal debe conocer y firmar.

2. **I02 Anexos de Protección de Datos**
   - Controls: mp.info.1
   - Summary: Anexos contractuales de protección de datos (versiones ES/CA, laboral/profesional). 4 variantes: I02-L-CA, I02-L-ES, I02-P-CA, I02-P-ES.

3. **I03 Registro entrega dispositivos de trabajo**
   - Controls: mp.eq.1, mp.eq.2
   - Summary: Formulario para registrar la entrega de dispositivos de trabajo a empleados.

4. **I04 Registro devolución dispositivos de trabajo**
   - Controls: mp.eq.1, mp.eq.2
   - Summary: Formulario para registrar la devolución de dispositivos al finalizar la relación laboral o cambio de equipo.

5. **I05 Autorización uso equipos particulares BYOD**
   - Controls: mp.eq.3
   - Summary: Autorización y condiciones para el uso de equipos personales en el entorno laboral.

Record all page IDs and update `confluence_map.md`.

---

### Task 7: Create stub pages under `04. Registros y Controles`

Create 12 child pages under `04. Registros y Controles`.

**Pages to create** (9 registers + 3 acquisitions):

Registers (use stub template adapted for .xlsx):

1. **D00 Lista de información documentada** — op.pl.2
2. **D04 Categorización y Declaración de Aplicabilidad ENS** — op.pl.3
3. **D05 Activos de Seguridad de la Información** — op.pl.2
4. **D06 Riesgos de Seguridad de la Información** — op.pl.1
5. **D07 BIA - Business Impact Analysis** — op.cont.1
6. **D09 Registro de Iniciativas de Mejora Continua** — op.exp.8
7. **D11 RAT - Registro de Actividades de Tratamiento** — mp.info.1
8. **D12 Medidas de Cumplimiento ENS** — op.mon.2
9. **D13 Marco Normativo Aplicable** — org.4

Acquisitions (use stub template for .docx):

10. **Adquisición Atlassian** — op.ext.1
11. **Adquisición Azure** — op.ext.1
12. **Adquisición GCP** — op.ext.1

Record all page IDs and update `confluence_map.md`.

---

### Task 8: Create stub pages under `05. Roles y Responsabilidades`

Create 5 child pages under `05. Roles`.

**Pages to create:**

1. **DPT01 CISO — Responsable de Seguridad de la Información** — org.2
2. **DPT02 CTO — Director de Tecnología** — org.2
3. **DPT03 DPO — Responsable de Protección de Datos** — mp.info.1
4. **DPT04 CEO — Director General** — org.1
5. **DPT05 Auditor Interno** — op.mon.2

Each should note that signed PDFs exist in `06_EVIDENCIAS/personal/`.

Record all page IDs and update `confluence_map.md`.

---

### Task 9: Create stub/reference pages under `07. Auditoría` and `09. Normativa Externa`

**Under 07. Auditoría** (3 pages):

1. **Informes de Auditoría Interna 2025** — op.mon.2
   - References: `Informe auditoria interna 2025-ENS-OPTIMTECH.pdf`, Anexo Detalle .xlsx
2. **Plan de Auditoría Interna 2025** — op.mon.2
   - References: `Plan auditoria interna 2025-ENS-OPTIMTECH.pdf`
3. **Acreditaciones** — op.mon.2
   - References: `Acreditacion Auditor SGSI-ENS-2025.pdf`

**Under 09. Normativa Externa** (1 page):

1. **Marco Normativo y CCN-STIC**
   - References: `normativa_seguridad_info.pdf`
   - Summary: Compilación de normativa externa aplicable: RD 311/2022, CCN-STIC 804, RGPD, LOPDGDD.

Record all page IDs and update `confluence_map.md`.

---

## Phase 4: Confluence Structure — Create Living Pages

Living pages contain full content. For the initial setup, create pages with structured templates that will be populated with real content over time. The content from existing .docx files can be used as a starting point.

### Task 10: Create living pages under `03. Procedimientos Operativos`

Create 6 child pages under `03. Procedimientos Operativos`.

**Living page template for procedures:**

```markdown
# [Title]

| Campo | Valor |
|-------|-------|
| **Código** | [code] |
| **Versión** | 1.0 |
| **Controles ENS** | [controls] |
| **Responsable** | [role] |
| **Última revisión** | Febrero 2026 |

## Objetivo

[Purpose of this procedure]

## Alcance

[Scope]

## Procedimiento

[Steps — to be populated from existing .docx content]

## Registros Asociados

[Related registers from section 04]

---

> **Nota:** Esta página es contenido vivo. Se edita y mantiene directamente en Confluence. El repositorio git almacena una exportación .docx periódica para fines de auditoría.
```

**Pages to create:**

1. **P01 Gestión de Riesgos de Seguridad de la Información** — op.pl.1, Responsable: CISO
2. **P02 Adquisición de componentes y servicios TIC** — op.ext.1, op.ext.2, Responsable: CTO
3. **P03 Gestión de Cambios** — op.exp.5, Responsable: CTO
4. **P04 Gestión de Usuarios** — op.acc.1-op.acc.6, Responsable: CTO
5. **P05 Gestión de Incidentes** — op.exp.7, Responsable: CISO
6. **Desarrollo Software (mp.sw.1/mp.sw.2)** — mp.sw.1, mp.sw.2, Responsable: CTO

Record all page IDs and update `confluence_map.md`.

---

### Task 11: Create living pages under `06. Evidencias`

Create 3 child pages (subsection containers):

1. **Evidencias Personal** — List of signed documents with references to git PDFs in `06_EVIDENCIAS/personal/`
2. **Evidencias Proveedores** — List of vendor certifications with references to git PDFs in `06_EVIDENCIAS/proveedores/`
3. **Evidencias Controles** — Living page for tracking control implementation evidence with screenshots and descriptions

Record all page IDs and update `confluence_map.md`.

---

### Task 12: Create living pages under `08. Gobernanza`

Create 5 child pages:

1. **Actas Comité Seguridad** — Living page tracking all committee meetings. Include template for new meeting minutes.
2. **Nombramientos Responsables Seguridad** — Living page with current appointments.
3. **Organigrama Servicios y Departamentos Afectados** — Living page with current org structure.
4. **Plan de Concienciación Seguridad** — Living page with the current awareness plan and status.
5. **Guía de Incorporación — Principios ENS** — Living page with the onboarding guide for new employees.

Record all page IDs and update `confluence_map.md`.

---

### Task 13: Create living page under `10. Procedimientos Aplicados (SOPs)`

Create 1 child page:

1. **PA-BKP-001 Backup y Restauración Confluence Cloud**
   - Copy content from existing `10_PROCEDIMIENTOS_APLICADOS/backup_recuperacion/PA-BKP-001 Backup y Restauración Confluence Cloud.md`
   - This page already exists as a markdown file locally — transfer its content directly.

Record page ID and update `confluence_map.md`.

---

### Task 14: Create Plantillas section pages

Create template reference pages under `Plantillas`:

1. **Plantilla ENS genérica** — Reference to git template
2. **Plantilla ENS (alternativa)** — Reference to git template
3. **PR-020 Procedimiento Desarrollo Software** — Reference to git template

Also consider merging with existing Confluence templates from `99. Legacy` (pages `7372885`, `7372854`, `7372859`, `7372875`).

Record all page IDs and update `confluence_map.md`.

---

## Phase 5: Finalize

### Task 15: Update the Index page

**Step 1: Update the existing Index page (`7372864`)**

Use `updateConfluencePage` to replace its content with a comprehensive navigation page:

```markdown
# ENSCORP — Sistema de Gestión de Seguridad de la Información

Espacio de conocimiento ENS (Esquema Nacional de Seguridad) nivel medio para optimTech.

## Navegación Rápida

| Sección | Descripción | Tipo |
|---------|-------------|------|
| [01. Políticas] | Políticas estratégicas de seguridad | Stub (git) |
| [02. Normas] | Normativas, instrucciones y formularios | Stub (git) |
| [03. Procedimientos Operativos] | Procedimientos de seguridad | Living |
| [04. Registros y Controles] | Registros de cumplimiento | Mixed |
| [05. Roles y Responsabilidades] | Descripciones de puestos | Stub (git) |
| [06. Evidencias] | Pruebas de implementación | Living |
| [07. Auditoría] | Documentación de auditorías | Mixed |
| [08. Gobernanza] | Gobierno de seguridad | Living |
| [09. Normativa Externa] | Referencias normativas | Stub |
| [10. SOPs] | Procedimientos aplicados | Living |
| [Plantillas] | Plantillas de documentos | Reference |

## Repositorio Git

Los documentos formales (.docx, .xlsx, .pdf) se mantienen en el repositorio git como fuente canónica. El archivo `confluence_map.md` en el repositorio contiene el mapeo completo entre archivos locales y páginas de Confluence.

## Legacy

La sección [99. Legacy] contiene contenido anterior a la reestructuración pendiente de migración.
```

---

### Task 16: Final `confluence_map.md` update and commit

**Step 1: Verify all page IDs are recorded**

Review `confluence_map.md` and ensure every `TBD` has been replaced with an actual page ID.

**Step 2: Final commit**

```bash
git add confluence_map.md
git commit -m "feat: complete confluence_map.md with all ENSCORP page IDs"
```

---

### Task 17: Verify the complete Confluence structure

**Step 1: Get all pages in ENSCORP space**

Use `getPagesInConfluenceSpace` with `spaceId: 7372801` and `limit: 250` to retrieve all pages.

**Step 2: Verify page hierarchy**

Use `getConfluencePageDescendants` on the root page (`7372803`) to confirm:
- 12 section pages exist as direct children of root (01-10 + Plantillas + 99.Legacy)
- Index page is a direct child of root
- All stub/living pages are correctly parented under their sections
- All legacy content is under `99. Legacy`

**Step 3: Count check**

Expected approximate page count:
- Section pages: 12
- Stub pages: ~26 (4 + 5 + 12 + 5 + 4 + 1 = 31 minus some groupings)
- Living pages: ~18 (6 + 3 + 5 + 1 + 3 = 18)
- Legacy pages: ~15 (existing content)
- Index: 1
- Total: ~70+ pages

---

## Summary of Deliverables

| Deliverable | Location |
|------------|----------|
| ENSCORP Confluence space restructured | Confluence (ENSCORP) |
| `confluence_map.md` with all page IDs | Repo root |
| Updated `CLAUDE.md` with Confluence integration docs | Repo root |
| Design document | `docs/plans/2026-02-22-enscorp-confluence-alignment-design.md` |
| This implementation plan | `docs/plans/2026-02-22-enscorp-confluence-alignment-plan.md` |
