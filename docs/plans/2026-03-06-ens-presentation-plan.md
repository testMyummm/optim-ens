# ENS Employee Presentation — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a .docx outline document and .pptx slide deck for a 45-60 min ENS presentation to all optimTech employees, in Spanish.

**Architecture:** Content-first approach — Task 1 generates the .docx with full text, speaker notes, and talking points for all 20 slides. Task 2 generates the .pptx slide deck using pptxgenjs, pulling content from the .docx outline. Task 3 runs visual QA on the .pptx.

**Tech Stack:** docx-js (npm `docx`) for .docx, pptxgenjs + react-icons + sharp for .pptx, LibreOffice + pdftoppm for visual QA.

**Skills Required:**
- `docx` skill — for .docx creation (docx-js patterns, validation)
- `pptx` skill — for .pptx creation (pptxgenjs patterns, QA workflow)
- `brand-guidelines` skill — for optimTech colors, fonts, logo

---

## Task 1: Generate the .docx Outline Document

**Files:**
- Create: `08_GOBERNANZA/Presentacion ENS equipo optimTech.docx`
- Read (content sources): All documents listed in design doc Content Sources section
- Read (logo): Extract from `PLANTILLAS/Plantilla ENS.docx`

**Step 1: Extract the logo**

```bash
python scripts/office/unpack.py "PLANTILLAS/Plantilla ENS.docx" /tmp/template_unpacked/
cp /tmp/template_unpacked/word/media/image1.png /tmp/optimtech_logo.png
```

**Step 2: Write the docx-js generation script**

Create `/tmp/gen_outline.js` using `require("docx")`. The document must:

- Use `OPTIMTECH_STYLES` from brand-guidelines (Calibri, teal headings)
- Use A4 page setup from brand-guidelines (`OPTIMTECH_PAGE`)
- Include optimTech header (3-column table, Segoe UI Bold, logo)
- Include optimTech footer (company info, italic 8pt)
- Language: `es-ES`

**Document structure:**

```
Cover Page:
  - Logo (large, centered)
  - "Esquema Nacional de Seguridad" at 80pt gray
  - "Presentacion al Equipo" at 40pt teal bold
  - "Marzo 2026" date line
  - Page break

Control Documental:
  - 4-column versioning table (Fecha: 06/03/2026, Version: 1.0, Modificaciones: Version inicial, Autor: CTO)
  - Page break

For each of the 20 slides (H1 per slide, numbered):
  H1: "Diapositiva N: [Slide Title]"
  H2: "Contenido"
    - Full text content for the slide (paragraphs, bullet lists)
    - Tables where applicable (e.g., org chart, classification levels, scenarios)
  H2: "Notas del Presentador"
    - Speaker notes: talking points, timing, emphasis cues, transitions
    - What to say vs. what's on screen
  H2: "Tiempo Estimado"
    - Duration for this slide
  [Page break between slides]
```

**Content per slide (all in Spanish):**

**Slide 1 — Portada:**
- Content: Title "ENS en optimTech", subtitle "Esquema Nacional de Seguridad — Presentacion al Equipo", date "Marzo 2026"
- Notes: Welcome, introduce yourself, set context

**Slide 2 — Mensaje del CTO:**
- Content: Three key messages as bullet points:
  1. "La seguridad es responsabilidad de todos" — not just IT
  2. "Estamos certificados y debemos mantenerlo" — pride in achievement
  3. "Asi protegemos a nuestros clientes y a nosotros mismos" — business trust
- Notes: Personal tone, share why this matters to you as CTO

**Slide 3 — Que es el ENS:**
- Content: Real Decreto 311/2022, replaces RD 3/2010. Applies to public sector and providers. Establishes minimum security measures. References CCN-STIC guides. Categories: Basica, Media, Alta.
- Notes: Explain legal obligation, mention that our clients require it

**Slide 4 — Por que optimTech esta certificado:**
- Content: We provide services to public administration and regulated sectors. Certification is competitive advantage. Shows our commitment to security. Required by our clients.
- Notes: Concrete examples of why this matters commercially

**Slide 5 — Nuestro recorrido:**
- Content: Timeline table: Gap analysis (TonniNova) -> Documentation (2025) -> Internal audit (Nov 2025) -> Certification -> Continuous improvement (2026)
- Notes: Walk through each phase, mention the effort involved

**Slide 6 — Los 10 Principios del ENS:**
- Content: From onboarding guide — all 10 principles:
  1. Seguridad como proceso integral
  2. Gestion de riesgos
  3. Prevencion, deteccion, respuesta y conservacion
  4. Lineas de defensa
  5. Vigilancia continua y reevaluacion periodica
  6. Diferenciacion de responsabilidades
  7. Proporcionalidad
  8. Transparencia
  9. Profesionalidad
  10. Mejora continua
- Notes: Don't read all 10 — highlight 3-4 most relevant, explain briefly

**Slide 7 — Gobernanza: Quien es quien:**
- Content: Table with roles:
  - CEO (DPT04) — Responsable ultimo, aprueba politicas
  - CTO (DPT02) — Director de Tecnologia, implementacion tecnica
  - CISO (DPT01) — Responsable de Seguridad de la Informacion
  - DPO (DPT03) — Responsable de Proteccion de Datos (RGPD)
  - Auditor Interno (DPT05) — Verificacion independiente
  - Comite de Seguridad — Organo colegiado, reuniones periodicas
- Notes: Explain who to contact for what, mention the Security Committee

**Slide 8 — Nuestra infraestructura:**
- Content: 4 platforms with certifications:
  - Microsoft Azure — ENS Alto certificado, ISO 27001
  - Google Cloud Platform — ENS certificado
  - Azure DevOps — ISO 27001
  - Atlassian (Jira + Confluence) — Gestion de proyectos y documentacion
  - Note: All vendor certifications available in 06_EVIDENCIAS/proveedores/
- Notes: Emphasize that we chose certified providers deliberately

**Slide 9 — Politicas clave:**
- Content: 4 policies with one-line descriptions:
  - D01 Politica de Seguridad de la Informacion — Marco general, principios, compromisos
  - D02 Politica de Clasificacion de la Informacion — Niveles de clasificacion y tratamiento
  - D03 Directrices de Seguridad de la Informacion — Normas operativas de acceso y autorizacion
  - D10 Politica de Proteccion de Datos Personales — Cumplimiento RGPD/LOPDGDD
- Notes: These are the "why" — next slides cover the "how"

**Slide 10 — Normativa que te afecta (I01):**
- Content: Key rules from I01 as bullet list:
  - Contrasenas: minimo 12 caracteres, MFA obligatorio
  - Correo electronico: no abrir adjuntos sospechosos, no reenviar informacion confidencial
  - Uso de internet: solo para fines profesionales, no descargar software no autorizado
  - Dispositivos moviles: cifrado obligatorio, PIN/biometria
  - Teletrabajo: usar VPN siempre, no usar WiFi publicas para datos sensibles
  - Puesto de trabajo: politica de mesa limpia (clean desk), bloquear pantalla (Win+L / Ctrl+Cmd+Q)
  - BYOD: requiere autorizacion formal (I05)
- Notes: This is the slide employees will reference most — be specific and practical

**Slide 11 — Procedimientos operativos:**
- Content: 5 procedures with brief descriptions:
  - P01 Gestion de Riesgos — Identificacion, analisis y tratamiento de riesgos
  - P02 Adquisicion TIC — Evaluacion de proveedores y servicios (Azure, GCP, Atlassian)
  - P03 Gestion de Cambios — Control de cambios en sistemas e infraestructura
  - P04 Gestion de Usuarios — Altas, bajas, modificaciones de acceso
  - P05 Gestion de Incidentes — Deteccion, respuesta y notificacion
- Notes: Employees don't need to memorize these, but need to know they exist and when they apply

**Slide 12 — Desarrollo seguro:**
- Content: From mp.sw.1/mp.sw.2:
  - SDLC seguro: seguridad en cada fase del desarrollo
  - Revision de codigo: obligatoria antes de despliegue
  - Pruebas de seguridad: analisis de vulnerabilidades
  - Control de versiones: Azure DevOps, ramas protegidas
  - Gestion de dependencias: actualizaciones de seguridad
- Notes: Mainly for developers, but all should understand our secure development practices

**Slide 13 — Clasificacion de la informacion:**
- Content: Table with classification levels from D02:
  - PUBLICO — Informacion de acceso libre
  - USO INTERNO — Informacion para empleados (default)
  - CONFIDENCIAL — Informacion restringida, acceso limitado
  - SECRETO — Maxima proteccion, acceso nominal
  - For each: handling rules (labeling, storage, transmission, destruction)
- Notes: Most of our documents are "USO INTERNO" — point to the header in our documents

**Slide 14 — Proteccion de datos (RGPD):**
- Content: From D10 and I02:
  - Reglamento General de Proteccion de Datos (RGPD) + LOPDGDD
  - Derechos de los interesados: acceso, rectificacion, supresion, portabilidad, oposicion
  - Notificacion de brechas: 72 horas a la AEPD
  - DPO: responsable de proteccion de datos (DPT03)
  - Registro de Actividades de Tratamiento (D11 RAT)
  - Anexos de proteccion de datos en contratos laborales y profesionales (I02)
- Notes: Everyone processes personal data — explain what that means practically

**Slide 15 — Escenarios: Que hago si...?:**
- Content: 4 scenario cards:
  1. Recibes un email sospechoso (phishing):
     - No hagas clic en enlaces ni abras adjuntos
     - Reporta inmediatamente al CISO
     - Marca como spam/phishing en el correo
  2. Pierdes o te roban un dispositivo:
     - Notifica al CISO en menos de 24 horas
     - Cambia tus contrasenas inmediatamente
     - El CISO activara el borrado remoto si es necesario
  3. Sospechas una brecha de datos:
     - Notifica al DPO y al CISO inmediatamente
     - Documenta lo que has observado
     - No intentes investigar por tu cuenta
     - El DPO evaluara si hay que notificar a la AEPD (72h)
  4. Necesitas un nuevo proveedor o herramienta:
     - Sigue el procedimiento P02 (Adquisicion TIC)
     - Verifica certificaciones ENS/ISO del proveedor
     - No contrates ni uses herramientas sin aprobacion
- Notes: Make these concrete and memorable — use real examples if possible

**Slide 16 — Tus obligaciones como empleado:**
- Content: Checklist format:
  - [ ] Usar contrasenas de 12+ caracteres con MFA
  - [ ] Bloquear la pantalla al levantarte (Win+L / Ctrl+Cmd+Q)
  - [ ] Reportar incidentes de seguridad en menos de 24 horas
  - [ ] Usar VPN para trabajo remoto
  - [ ] No instalar software no autorizado
  - [ ] Politica de mesa limpia: no dejar documentos sensibles visibles
  - [ ] Firmar la normativa de seguridad (I01) y el anexo de proteccion de datos (I02)
  - [ ] Solicitar autorizacion BYOD si usas equipo personal (I05)
- Notes: This is the "takeaway" slide — reinforce that these are non-negotiable

**Slide 17 — Evidencias y auditoria:**
- Content:
  - Por que recogemos evidencias: demostrar cumplimiento ante auditores
  - Tipos: documentos firmados, capturas de configuracion, certificados de proveedores
  - Auditoria interna 2025: completada en noviembre 2025
  - Resultados: areas de mejora identificadas, plan de accion en marcha
  - Mejora continua: registro D09
- Notes: Brief — explain that audits are routine, not punitive

**Slide 18 — Plan de concienciacion 2026:**
- Content: From awareness plan:
  - Formacion anual obligatoria en seguridad
  - Simulacros de phishing periodicos
  - Actualizaciones trimestrales del Comite de Seguridad
  - Roadmap de certificaciones tecnicas (CTO learning plan)
  - Revision y actualizacion de politicas
- Notes: Show that security is ongoing, not a one-time event

**Slide 19 — Recursos y contactos:**
- Content:
  - Confluence ENSCORP: base de conocimiento viva (documentacion, procedimientos, SOPs)
  - CISO: para incidentes de seguridad y consultas tecnicas
  - DPO: para temas de proteccion de datos personales
  - CEO: para aprobacion de politicas
  - Comite de Seguridad: reuniones periodicas, actas disponibles en 08_GOBERNANZA
  - Documentos clave: todos disponibles en el repositorio ENS y en Confluence
- Notes: Provide specific names/emails if appropriate for your org

**Slide 20 — Preguntas y cierre:**
- Content: "Preguntas?" + key takeaway reinforcement:
  - La seguridad es responsabilidad de todos
  - Reporta cualquier incidente — es mejor una falsa alarma que un incidente no reportado
  - Gracias por vuestro compromiso
- Notes: Open Q&A, thank the team, reinforce the collaborative message

**Step 3: Run the generation script**

```bash
node /tmp/gen_outline.js
```

Expected: Creates `08_GOBERNANZA/Presentacion ENS equipo optimTech.docx`

**Step 4: Validate the .docx**

```bash
python scripts/office/validate.py "08_GOBERNANZA/Presentacion ENS equipo optimTech.docx"
```

Expected: No errors.

**Step 5: Commit**

```bash
git add "08_GOBERNANZA/Presentacion ENS equipo optimTech.docx"
git commit -m "feat: add ENS employee presentation outline (.docx)"
```

---

## Task 2: Generate the .pptx Slide Deck

**Files:**
- Create: `08_GOBERNANZA/Presentacion ENS equipo optimTech.pptx`
- Read: `08_GOBERNANZA/Presentacion ENS equipo optimTech.docx` (for content reference)

**Step 1: Install dependencies**

```bash
npm list -g pptxgenjs || npm install -g pptxgenjs
npm list -g react-icons || npm install -g react-icons react react-dom sharp
```

**Step 2: Write the pptxgenjs generation script**

Create `/tmp/gen_slides.js` using `require("pptxgenjs")` and `react-icons` for icons.

**Design decisions (from pptx skill + brand-guidelines):**

- **Layout:** `LAYOUT_16x9` (10" x 5.625")
- **Color palette — "Teal Trust" adapted to optimTech brand:**
  - Primary: `0D9A76` (Corporate Teal — from brand guidelines)
  - Secondary: `D1FBF0` (Light Teal — from brand guidelines)
  - Dark: `1E2D3D` (Dark navy for title/conclusion slides)
  - Text: `2D3748` (Dark gray body text)
  - Light bg: `F8FAFB` (Off-white content slides)
  - Accent: `2E74B5` (Accent Blue from brand guidelines)
  - White: `FFFFFF`
- **Typography:**
  - Titles: Calibri Bold 36-40pt
  - Section headers: Calibri Bold 20-24pt
  - Body: Calibri 14-16pt
  - Captions: Calibri 10-12pt muted
- **Visual motif:** Left-side teal accent bar (0.08" wide) on content cards
- **Slide sandwich:** Dark backgrounds for title (1) + CTO message (2) + close (20), light for all content slides

**Slide master definitions:**

```javascript
// TITLE_MASTER: dark bg (1E2D3D), large centered text, logo
// CONTENT_MASTER: light bg (F8FAFB), teal top bar, slide number
// SECTION_MASTER: teal bg (0D9A76), white text, transition slides
```

**Slide-by-slide layout plan:**

| # | Layout Type | Visual Elements |
|---|------------|-----------------|
| 1 | Title (dark bg) | Logo centered, large title, subtitle, date |
| 2 | Title (dark bg) | 3 icon+text rows (shield, certificate, handshake) |
| 3 | Content (light) | Two-column: text left, key stats right (RD 311/2022, categories) |
| 4 | Content (light) | 3 icon cards in a row (clients, advantage, trust) |
| 5 | Content (light) | Horizontal timeline with 5 milestones |
| 6 | Content (light) | 2x5 grid of numbered principles with short labels |
| 7 | Content (light) | Org chart style: 5 role cards + committee note |
| 8 | Content (light) | 4 platform cards with certification badges |
| 9 | Content (light) | 4 policy cards with accent borders |
| 10 | Content (light) | Icon + text rows (7 rules from I01) |
| 11 | Content (light) | 5 procedure cards in column |
| 12 | Content (light) | Icon + text rows (secure SDLC steps) |
| 13 | Content (light) | 4-row table: classification levels with color coding |
| 14 | Content (light) | Two-column: RGPD rights left, breach process right |
| 15 | Content (light) | 2x2 scenario cards with colored headers |
| 16 | Content (light) | Checklist with check icons, 8 items |
| 17 | Content (light) | Two-column: evidence types left, audit results right |
| 18 | Content (light) | Timeline/roadmap for 2026 awareness activities |
| 19 | Content (light) | Contact cards: CISO, DPO, Confluence, Committee |
| 20 | Title (dark bg) | "Preguntas?" large, 3 takeaway bullets, "Gracias" |

**Icons to use (react-icons/fa):**
- FaShieldAlt (security), FaCertificate (certification), FaHandshake (trust)
- FaLock (passwords), FaEnvelope (email), FaGlobe (internet), FaMobile (mobile)
- FaLaptopHouse (remote), FaDesktop (workstation), FaUserShield (BYOD)
- FaExclamationTriangle (phishing), FaTablet (lost device), FaDatabase (breach), FaShoppingCart (vendor)
- FaCheckCircle (checklist items), FaUsers (committee), FaBook (confluence)

**Critical pptxgenjs rules:**
- No `#` in hex colors
- Use `bullet: true` not unicode bullets
- Use `breakLine: true` between array text items
- Never reuse option objects (use factory functions for shadows)
- `margin: 0` on text boxes when aligning with shapes

**Step 3: Run the generation script**

```bash
node /tmp/gen_slides.js
```

Expected: Creates `08_GOBERNANZA/Presentacion ENS equipo optimTech.pptx`

**Step 4: Commit**

```bash
git add "08_GOBERNANZA/Presentacion ENS equipo optimTech.pptx"
git commit -m "feat: add ENS employee presentation slide deck (.pptx)"
```

---

## Task 3: Visual QA of the .pptx

**Step 1: Convert to images**

```bash
python scripts/office/soffice.py --headless --convert-to pdf "08_GOBERNANZA/Presentacion ENS equipo optimTech.pptx"
pdftoppm -jpeg -r 150 "08_GOBERNANZA/Presentacion ENS equipo optimTech.pdf" /tmp/ens-slide
```

**Step 2: Visual inspection using subagent**

Launch a subagent to inspect ALL slide images. Look for:
- Overlapping elements
- Text overflow or cut off
- Low-contrast text/icons
- Uneven spacing
- Missing content
- Leftover placeholder text

**Step 3: Fix issues found**

Regenerate affected slides by editing `/tmp/gen_slides.js` and re-running.

**Step 4: Re-verify**

Convert again and inspect fixed slides. Repeat until clean pass.

**Step 5: Content QA**

```bash
python -m markitdown "08_GOBERNANZA/Presentacion ENS equipo optimTech.pptx"
```

Verify all 20 slides present, content matches the .docx outline, no typos.

**Step 6: Final commit**

```bash
git add "08_GOBERNANZA/Presentacion ENS equipo optimTech.pptx"
git commit -m "fix: QA fixes for ENS presentation slides"
```

---

## Task 4: Update confluence_map.md

**Step 1: Add entry for the new document**

Add to the `08_GOBERNANZA` section of `confluence_map.md`:

```
| `08_GOBERNANZA/Presentacion ENS equipo optimTech.docx` | Presentacion ENS equipo optimTech | TBD | living | confluence -> git |
| `08_GOBERNANZA/Presentacion ENS equipo optimTech.pptx` | _(included above)_ | -- | -- | -- |
```

**Step 2: Commit**

```bash
git add confluence_map.md
git commit -m "docs: add ENS presentation to confluence_map.md"
```
