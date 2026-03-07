# Design: ENS Employee Presentation

**Date:** 2026-03-06
**Author:** CTO
**Status:** Approved

## Goal

Create a formal, thorough presentation (~45-60 min) for all optimTech employees explaining ENS compliance: what it is, how it affects them, what procedures/policies exist, who is responsible, and what each employee must do.

## Deliverables

1. **Outline document** (.docx) — Full content with talking points and speaker notes per slide
2. **Slide deck** (.pptx) — Visual presentation for projection

**Approach:** Content-first (Option A). Write the .docx outline first, then generate the .pptx from it.

## Parameters

- **Language:** Spanish (Castellano)
- **Audience:** All employees (mixed technical/non-technical)
- **Tone:** Formal and thorough
- **Duration:** 45-60 minutes
- **Key messages:**
  - Security is everyone's responsibility
  - We're certified and must maintain it
  - This is how we protect our clients and ourselves

## Slide Structure (20 slides)

| # | Section | Content | Time |
|---|---------|---------|------|
| 1 | Portada | Title, logo placeholder, date | — |
| 2 | Mensaje del CTO | Triple message: collective responsibility + certified pride + client trust | 2 min |
| 3 | Que es el ENS? | RD 311/2022, legal framework, purpose, who it applies to | 3 min |
| 4 | Por que optimTech esta certificado? | Public sector clients, competitive advantage, trust | 3 min |
| 5 | Nuestro recorrido | Timeline: gap analysis -> docs -> 2025 audit -> certification -> 2026 improvement | 3 min |
| 6 | Los 10 Principios del ENS | From onboarding guide: security as integral process, risk-based, prevention/detection/response, etc. | 5 min |
| 7 | Gobernanza: Quien es quien? | Org chart: CEO (DPT04), CTO (DPT02), CISO (DPT01), DPO (DPT03), Auditor (DPT05), Comite de Seguridad | 4 min |
| 8 | Nuestra infraestructura | Azure (ENS High), GCP (ENS certified), Atlassian, Azure DevOps — all compliant | 3 min |
| 9 | Politicas clave | D01 (Security), D02 (Classification), D03 (Guidelines), D10 (Data Protection) | 5 min |
| 10 | Normativa que te afecta (I01) | Passwords 12+ chars MFA, email, internet, mobile, remote work, clean desk, BYOD | 5 min |
| 11 | Procedimientos operativos | P01 Risk, P02 Vendors, P03 Changes, P04 Users, P05 Incidents | 4 min |
| 12 | Desarrollo seguro | mp.sw.1/mp.sw.2, secure SDLC, code review, testing | 3 min |
| 13 | Clasificacion de la informacion | Levels from D02, labeling, handling per level | 3 min |
| 14 | Proteccion de datos (RGPD) | D10 + I02, data subject rights, breach notification 72h, DPO | 3 min |
| 15 | Escenarios: Que hago si...? | 4 scenarios: phishing, lost device, data breach, new vendor request | 5 min |
| 16 | Tus obligaciones como empleado | Summary checklist: passwords, lock screen, report <24h, VPN, no unapproved SW, clean desk | 3 min |
| 17 | Evidencias y auditoria | Why we collect evidence, 2025 audit results, continuous improvement | 2 min |
| 18 | Plan de concienciacion 2026 | Awareness plan, training roadmap, certifications | 2 min |
| 19 | Recursos y contactos | Confluence ENSCORP, CISO/DPO contacts, incident reporting | 2 min |
| 20 | Preguntas y cierre | Q&A, key takeaway reinforcement | open |

## Content Sources

All content will be drawn from existing ENS documents:

- **D01** — Politica de Seguridad de la Informacion
- **D02** — Politica de Clasificacion de la Informacion
- **D03** — Directrices de Seguridad de la Informacion
- **D10** — Politica de Proteccion de Datos Personales
- **I01** — Normativa de Seguridad de la Informacion
- **I02** — Anexos de Proteccion de Datos
- **I05** — Autorizacion BYOD
- **P01-P05** — Procedimientos operativos
- **mp.sw.1/mp.sw.2** — Desarrollo software
- **DPT01-DPT05** — Role descriptions
- **Guia de Incorporacion** — Principios ENS (onboarding guide)
- **Pla conscienciacio seguretat** — Awareness plan
- **Acta constitucion Comite Seguridad** — Governance
- **Organigrama** — Org chart
- **Vendor certs** — Azure ENS High, GCP ENS, Azure DevOps ISO 27001

## Implementation Order

1. Write full .docx outline with all content, talking points, and speaker notes
2. Generate .pptx slide deck from the outline content
3. Review both for consistency
