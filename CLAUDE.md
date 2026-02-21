# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a document management repository for **ENS (Esquema Nacional de Seguridad)** compliance at **optimTech / Optimpeople**. It contains Spain's National Security Framework certification documents in Spanish (ES) and Catalan (CA).

There is no source code, build system, test suite, or linting. This is a structured collection of ISMS (SGSI) compliance and governance documents version-controlled with git.

## Directory Structure

- `2025/` — Active working documents for the current certification cycle
  - `AUDITORIA INTERNA 2025/` — Internal audit reports and plans
  - `TonniNova/` — Client-specific document set
    - `SGSI/` — Final, approved, and signed documents (organized by type)
    - `WIP/` — Work-in-progress drafts
    - `Gap Analysis/` — Gap analysis deliverables
- `EVIDENCIES/` — Screenshot evidence for ENS control compliance
- `NORMATIVA/` — Regulatory reference material

## Document Naming Convention

| Prefix | Type | Examples |
|--------|------|---------|
| `D##` | Core ISMS documents | D01 Security Policy, D04 Statement of Applicability, D06 Risk Register |
| `I##` | Forms and instructions | I01 Security Normative, I02 Data Protection Annex, I05 BYOD Auth |
| `P##` | Procedures | P01 Risk Management, P03 Change Management, P05 Incident Management |
| `DPT##` | Job role descriptions | DPT01 CISO, DPT02 CTO, DPT03 DPO |
| `AUD##` | Audit documents | AUD02 System Description, AUD13 Security Architecture |

## Workflow

- **WIP/** contains active drafts being developed
- **SGSI/** contains final, approved, signed documents
- **Pendent signar [Name]/** holds documents awaiting a specific person's signature
- Evidence screenshots go in **EVIDENCIES/** or under `SGSI/REGISTRES/`

## Languages

- Primary: Spanish (Castellano)
- Secondary: Catalan — used especially for Catalan-jurisdiction contracts (I02)

## Cloud Infrastructure Referenced in Documents

- **Microsoft Azure** (Azure DevOps) — ENS High certified, ISO 27001
- **Google Cloud Platform** — ENS certified
- **Atlassian** (Jira + Confluence) — Project management and documentation

## Git Notes

- Binary files (PDF, DOCX, XLSX, Pages) are tracked directly in git
- `.gitignore` is effectively empty
