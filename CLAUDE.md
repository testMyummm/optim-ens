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

## Git Notes

- Binary files (PDF, DOCX, XLSX) are tracked directly in git
- `.gitignore` excludes: `.DS_Store`, Office temp files (`~$*`), `.pages` files, and credential files
- `snapshots/` preserves the original document structure from each certification cycle
