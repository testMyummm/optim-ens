# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a document management repository for **ENS (Esquema Nacional de Seguridad)** compliance at **optimTech / Optimpeople**. It contains Spain's National Security Framework certification documents in Spanish (ES) and Catalan (CA).

There is no source code, build system, test suite, or linting. This is a structured collection of ISMS (SGSI) compliance and governance documents version-controlled with git.

## Directory Structure

The live document structure follows ENS best practices, organized by document type:

```
ENS/
├── 01_POLITICAS/          # Strategic security policies (D01-D03, D10)
├── 02_NORMAS/             # Standards, instructions, forms (I01-I05)
├── 03_PROCEDIMIENTOS/     # Operational procedures (P01-P05, software dev)
├── 04_REGISTROS/          # Registers and compliance records (D00, D04-D13, procurement)
├── 05_ROLES/              # Job role descriptions (DPT01-DPT05)
├── 06_EVIDENCIAS/         # Proof of implementation
│   ├── personal/          # Signed employee documents (PDFs)
│   ├── proveedores/       # Vendor/cloud certifications (Azure, GCP)
│   └── controles/         # Control implementation screenshots
├── 07_AUDITORIA/          # Audit documents, reports, accreditations
├── 08_GOBERNANZA/         # Committee acts, org charts, appointments, awareness, onboarding
├── 09_NORMATIVA_EXTERNA/  # External regulations, CCN-STIC references
├── 10_PROCEDIMIENTOS_APLICADOS/ # Applied procedures / SOPs
├── PLANTILLAS/            # Document templates
└── snapshots/             # Frozen yearly snapshots
    ├── 2025/              # Original 2025 certification cycle (frozen)
    └── gap_analysis/      # Initial TonniNova gap analysis deliverables
```

## Document Naming Convention

| Prefix | Type | Location |
|--------|------|----------|
| `D##` | Core ISMS documents | `01_POLITICAS/` (policies) or `04_REGISTROS/` (registers/records) |
| `I##` | Forms and instructions | `02_NORMAS/` |
| `P##` | Procedures | `03_PROCEDIMIENTOS/` |
| `DPT##` | Job role descriptions | `05_ROLES/` (editable .docx) or `06_EVIDENCIAS/personal/` (signed .pdf) |
| `AUD##` | Audit documents | `07_AUDITORIA/` |
| (descriptive) | Governance documents (acts, org charts, onboarding guides) | `08_GOBERNANZA/` |

## Workflow

- **Live folders** (`01_POLITICAS/` through `09_NORMATIVA_EXTERNA/`) contain the current, authoritative versions of all documents
- **Editable .docx** files go in the categorized live folders
- **Signed .pdf** files go in `06_EVIDENCIAS/personal/`
- **Vendor certifications** go in `06_EVIDENCIAS/proveedores/`
- **Control evidence screenshots** go in `06_EVIDENCIAS/controles/`
- **Templates** go in `PLANTILLAS/`
- **Governance documents** (committee acts, onboarding guides, awareness plans) go in `08_GOBERNANZA/` using descriptive names
- **snapshots/** contains frozen yearly archives — do not modify

## Languages

- Primary: Spanish (Castellano)
- Secondary: Catalan — used especially for Catalan-jurisdiction contracts (I02)

## Cloud Infrastructure Referenced in Documents

- **Microsoft Azure** (Azure DevOps) — ENS High certified, ISO 27001
- **Google Cloud Platform** — ENS certified
- **Atlassian** (Jira + Confluence) — Project management and documentation

## Atlassian Access

- When using Atlassian tools, only access Confluence space **ENSCORP**. No other spaces are authorized.

## Confluence Integration (ENSCORP)

Git is the **single source of truth** for all ENS documents. The ENSCORP Confluence space is the **viewing and collaboration interface** — content is synced from git via SharePoint.

### Content Types

| Type | Where to Edit | Confluence Role | Examples |
|------|---------------|-----------------|----------|
| **Living** | Edit in Confluence; export .docx to git periodically | Authoring + viewing interface | Procedures (03), Governance (08), SOPs (10), Evidence (06) |
| **Stub** | Edit locally (.docx/.xlsx/.pdf) | Metadata + SharePoint link | Policies (01), Norms (02), Roles (05), Audit (07), External Regs (09) |
| **Mixed** | Spreadsheets locally, descriptions in Confluence | Partial authoring | Registros (04) |

### Mapping File

`confluence_map.md` at the repo root tracks the relationship between local files and Confluence page IDs. Update it whenever pages are created or reorganized.

### Rules

- Living pages: Content is authored and maintained in Confluence. Git stores a .docx export for offline/audit purposes.
- Stub pages: Content is authored locally as .docx/.xlsx. Confluence page shows metadata, summary, and a reference note.
- When creating new documents, add entries to both the appropriate local folder AND `confluence_map.md`.

## SharePoint Sync

Documents are automatically synced from git to SharePoint, with links embedded in the corresponding Confluence pages. The pipeline is: **git → SharePoint (via Microsoft Graph API) → Confluence embed**.

### Script

`scripts/sync_sharepoint.py` — uploads documents (.docx, .xlsx, .pdf, .pptx) to SharePoint and updates Confluence pages with SharePoint links.

```bash
# Sync files changed in last commit (default)
python scripts/sync_sharepoint.py

# Sync ALL mapped documents
python scripts/sync_sharepoint.py --all

# Sync a specific file
python scripts/sync_sharepoint.py --file "01_POLITICAS/D01_Politica_de_seguridad.docx"

# Preview what would be synced
python scripts/sync_sharepoint.py --dry-run

# Upload to SharePoint only (skip Confluence update)
python scripts/sync_sharepoint.py --skip-confluence
```

### GitHub Action

The workflow (`.github/workflows/sync-sharepoint.yml`) triggers automatically on push to `main` when document files change. It can also be triggered manually via `workflow_dispatch` with an option to sync all files.

### Required GitHub Secrets

| Secret | Purpose |
|--------|---------|
| `AZURE_TENANT_ID` | Azure AD tenant for SharePoint access |
| `AZURE_CLIENT_ID` | Azure AD app registration client ID |
| `AZURE_CLIENT_SECRET` | Azure AD app registration client secret |
| `CONFLUENCE_USER` | Atlassian account email |
| `CONFLUENCE_API_TOKEN` | Atlassian API token |

## Claude Code Skills

This repository has Claude Code skills installed for working with Office documents:

- **pptx** — Read, edit, and create PowerPoint presentations (.pptx)
- **docx** — Read, edit, and create Word documents (.docx)
- **xlsx** — Read, edit, and create Excel spreadsheets (.xlsx)

Dependencies: `markitdown`, `pptxgenjs`, LibreOffice, Poppler (poppler-utils).

## Git Notes

- Binary files (PDF, DOCX, XLSX, PPTX) are tracked directly in git
- `.gitignore` excludes: `.DS_Store`, Office temp files (`~$*`), `.pages` files, and credential files
- `snapshots/` preserves the original document structure from each certification cycle
