---
name: brand-guidelines
description: Applies OPTIMTECH's official brand colors, typography, page layout, and document structure to ENS compliance documents. Use it when creating or editing .docx files to match the established optimTech look-and-feel across policies, norms, forms, procedures, records, and role descriptions.
license: Complete terms in LICENSE.txt
---

# OPTIMTECH Brand Guidelines — ENS Document System

## Overview

Brand identity for **OPTIMTECH (Optim AI Improvement s.l.)** ENS compliance documents. Every .docx produced must match the patterns extracted from the live document corpus.

**Keywords**: branding, corporate identity, optimTech, ENS, SGSI, visual formatting, document styling, brand colors, typography

---

## Layer 1: Global Brand Identity

These values apply to **every** ENS document unless a per-type override is specified in Layer 2.

### Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Corporate Teal** | `#0D9A76` | H1–H3 headings, versioning table header text, title accents |
| **Light Teal** | `#D1FBF0` | Versioning table header fill ("Control Documental") |
| **Accent Blue** | `#2E74B5` | H4–H5 headings |
| **Dark Blue** | `#1F4D78` | H6–H7 headings |
| **Display Gray** | `#808080` | 80pt decorative title page text (policies, procedures) |
| **Footer Gray** | `#404040` | Footer text in all sections |
| **Table Border Gray** | `#D9D9D9` | Standard table borders |
| **Header Border Gray** | `#BFBFBF` | Header table cell borders |
| **Form Green** | `#F1FDF9` | Form table header row fill (I03–I05) |
| **Dark Gray** | `#272727` | H8–H9 headings |

### Typography

| Element | Font | Size (pt) | Weight | Color |
|---------|------|-----------|--------|-------|
| Body text | Calibri | 11 | Normal | Black |
| H1 | Calibri | 16 | Bold | `#0D9A76` |
| H2 | Calibri | 13 | Normal | `#0D9A76` |
| H3 | Calibri | 12 | Normal | `#0D9A76` |
| H4 | Calibri | 11 | Italic | `#2E74B5` |
| H5 | Calibri | 11 | Normal | `#2E74B5` |
| H6–H7 | Calibri | 11 | Normal/Italic | `#1F4D78` |
| H8–H9 | Calibri | 10.5 | Normal/Italic | `#272727` |
| Header labels | Segoe UI | 11 | Bold | Black |
| Footer | Calibri | 8 | Italic | `#404040` |
| Title page (D##, P##) | Calibri | 80 | Normal | `#808080` |
| Title page (I## norms) | Calibri | 40 | Bold | `#0D9A76` |
| Title (records) | Calibri | 36 | Bold | `#0D9A76` |
| DPT## (all text) | Segoe UI | 11 | Normal | Black |

**Font fallback chain**: Calibri > Segoe UI > Myriad Pro > Arial > Roboto Light

#### docx-js Styles

```javascript
const OPTIMTECH_STYLES = {
  default: {
    document: {
      run: { font: "Calibri", size: 22 } // 11pt body
    }
  },
  paragraphStyles: [
    {
      id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 32, bold: true, font: "Calibri", color: "0D9A76" },
      paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 0 }
    },
    {
      id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 26, font: "Calibri", color: "0D9A76" },
      paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 1 }
    },
    {
      id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 24, font: "Calibri", color: "0D9A76" },
      paragraph: { spacing: { before: 160, after: 80 }, outlineLevel: 2 }
    },
    {
      id: "Heading4", name: "Heading 4", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 22, italics: true, font: "Calibri", color: "2E74B5" },
      paragraph: { spacing: { before: 120, after: 60 }, outlineLevel: 3 }
    },
    {
      id: "Heading5", name: "Heading 5", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 22, font: "Calibri", color: "2E74B5" },
      paragraph: { spacing: { before: 120, after: 60 }, outlineLevel: 4 }
    },
  ]
};
```

#### DPT## Style Override (Segoe UI)

```javascript
const DPT_STYLES = {
  default: {
    document: {
      run: { font: "Segoe UI", size: 22 }
    }
  },
  paragraphStyles: [
    {
      id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 32, bold: true, font: "Segoe UI", color: "0D9A76" },
      paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 0 }
    },
  ]
};
```

#### XML Heading Style Pattern (styles.xml)

```xml
<w:style w:type="paragraph" w:customStyle="1" w:styleId="Ttol1">
  <w:name w:val="Ttol1"/>
  <w:pPr>
    <w:spacing w:before="240" w:after="120"/>
    <w:outlineLvl w:val="0"/>
  </w:pPr>
  <w:rPr>
    <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
    <w:b/>
    <w:color w:val="0D9A76"/>
    <w:sz w:val="32"/>
  </w:rPr>
</w:style>
```

> **Note**: The template uses Catalan-named style IDs: `Ttol1`–`Ttol9` ("Titol"), `Capalera` (Header), `Peu` (Footer), `Nmerodepgina` (Page Number).

### Page Setup (A4)

| Property | Twips (DXA) | Inches | cm |
|----------|-------------|--------|-----|
| Page width | 11900 | 8.27" | 21.0 |
| Page height | 16840 | 11.69" | 29.7 |
| Top margin | 1985 | 1.39" | 3.5 |
| Right margin | 1127 | 0.79" | 2.0 |
| Bottom margin | 1276 | 0.89" | 2.3 |
| Left margin | 1276 | 0.89" | 2.3 |
| Header distance | 708 | 0.49" | 1.25 |
| Footer distance | 548 | 0.38" | 0.97 |
| **Content width** | **9497** | **6.60"** | **16.8** |

Content width = 11900 − 1276 − 1127 = 9497 twips.

```javascript
const OPTIMTECH_PAGE = {
  size: { width: 11900, height: 16840 },
  margin: {
    top: 1985, right: 1127, bottom: 1276, left: 1276,
    header: 708, footer: 548
  }
};
```

### Logo

| Variant | EMUs | Approx Size | Usage |
|---------|------|-------------|-------|
| Header (small) | 931349 x 378847 | 0.65" x 0.27" | Right-aligned in header table |
| Cover (large) | 3231098 x 1338681 | 2.25" x 0.93" | Title page, centered |
| Alt header | 1548130 x 641350 | 1.08" x 0.45" | Some header variants |

- **Format**: PNG, RGBA 8-bit, 350 x 145 px (~101 KB)
- **Path inside .docx**: `word/media/image1.png`
- **Source**: Extract from `PLANTILLAS/Plantilla ENS.docx` or any existing ENS document

### Footer

All documents share this footer. Italic 8pt Calibri, `#404040`, center-aligned.

```
OPTIMTECH (Optim AI Improvement s.l.)
www.optimtech.com
P.I Venta Nova S/N, Carrer l'Aldea, 0, 43894 Camarles
B22561500  |  +34 650 891 296
```

The website line is rendered as an `ExternalHyperlink`.

#### docx-js Footer

```javascript
const OPTIMTECH_FOOTER = new Footer({
  children: [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "OPTIMTECH (Optim AI Improvement s.l.)", italics: true, size: 16, color: "404040", font: "Calibri" }),
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new ExternalHyperlink({
          link: "https://www.optimtech.com",
          children: [new TextRun({ text: "www.optimtech.com", italics: true, size: 16, color: "404040", font: "Calibri" })]
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "P.I Venta Nova S/N, Carrer l'Aldea, 0, 43894 Camarles", italics: true, size: 16, color: "404040", font: "Calibri" }),
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "B22561500  |  +34 650 891 296", italics: true, size: 16, color: "404040", font: "Calibri" }),
      ]
    }),
  ]
});
```

#### XML Footer Pattern

```xml
<w:ftr>
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:r>
      <w:rPr>
        <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
        <w:i/>
        <w:color w:val="404040"/>
        <w:sz w:val="16"/>
      </w:rPr>
      <w:t>OPTIMTECH (Optim AI Improvement s.l.)</w:t>
    </w:r>
  </w:p>
  <!-- Additional paragraphs for website (hyperlink), address, CIF + phone -->
</w:ftr>
```

### Header

3-column fixed-layout table. Segoe UI Bold 11pt. Borders `#BFBFBF`.

| Column | Width (twips) | Content |
|--------|---------------|---------|
| Left | 3575 | Document title |
| Center | 3049 | Reference (e.g. "D01 Rev.01") |
| Right | 3049 | "USO INTERNO" + Logo |

Total width: 9673 twips. Cell padding: 70 twips left/right.

```javascript
const headerBorder = { style: BorderStyle.SINGLE, size: 1, color: "BFBFBF" };
const headerBorders = { top: headerBorder, bottom: headerBorder, left: headerBorder, right: headerBorder };

const OPTIMTECH_HEADER = new Header({
  children: [
    new Table({
      width: { size: 9673, type: WidthType.DXA },
      columnWidths: [3575, 3049, 3049],
      rows: [
        new TableRow({
          children: [
            new TableCell({
              borders: headerBorders,
              width: { size: 3575, type: WidthType.DXA },
              margins: { left: 70, right: 70 },
              children: [new Paragraph({
                children: [new TextRun({ text: "DOCUMENT TITLE", bold: true, font: "Segoe UI", size: 22 })]
              })]
            }),
            new TableCell({
              borders: headerBorders,
              width: { size: 3049, type: WidthType.DXA },
              margins: { left: 70, right: 70 },
              children: [new Paragraph({
                children: [new TextRun({ text: "REF Rev.XX", bold: true, font: "Segoe UI", size: 22 })]
              })]
            }),
            new TableCell({
              borders: headerBorders,
              width: { size: 3049, type: WidthType.DXA },
              margins: { left: 70, right: 70 },
              verticalAlign: VerticalAlign.CENTER,
              children: [
                new Paragraph({
                  children: [new TextRun({ text: "USO INTERNO", bold: true, font: "Segoe UI", size: 22 })]
                }),
                new Paragraph({
                  alignment: AlignmentType.RIGHT,
                  children: [/* Logo ImageRun — extract from template */]
                })
              ]
            }),
          ]
        })
      ]
    })
  ]
});
```

### Versioning Table ("Control Documental")

Header fill `#D1FBF0`, bold centered text, borders `#D9D9D9` 4pt single.

#### 4-Column (Policies D##, Norms I01)

| Column | Header | Width (twips) |
|--------|--------|---------------|
| 1 | Fecha | 1800 |
| 2 | Version | 1200 |
| 3 | Modificaciones | 4487 |
| 4 | Autor | 2000 |

Total: 9487 twips.

#### 5-Column (Procedures P##)

| Column | Header | Width (twips) |
|--------|--------|---------------|
| 1 | Fecha | 1400 |
| 2 | Estado | 1200 |
| 3 | Version | 1000 |
| 4 | Modificaciones | 4087 |
| 5 | Autor | 1800 |

Total: 9487 twips.

#### docx-js — 4-Column Versioning Table

```javascript
const versionBorder = { style: BorderStyle.SINGLE, size: 4, color: "D9D9D9" };
const versionBorders = { top: versionBorder, bottom: versionBorder, left: versionBorder, right: versionBorder };
const headerShading = { fill: "D1FBF0", type: ShadingType.CLEAR };

function createVersioningTable(rows) {
  const colWidths = [1800, 1200, 4487, 2000];
  return new Table({
    width: { size: 9487, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [
      new TableRow({
        children: ["Fecha", "Version", "Modificaciones", "Autor"].map((text, i) =>
          new TableCell({
            borders: versionBorders,
            width: { size: colWidths[i], type: WidthType.DXA },
            shading: headerShading,
            children: [new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { before: 60, after: 60 },
              children: [new TextRun({ text, bold: true, size: 22, font: "Calibri" })]
            })]
          })
        )
      }),
      ...rows.map(row =>
        new TableRow({
          children: row.map((text, i) =>
            new TableCell({
              borders: versionBorders,
              width: { size: colWidths[i], type: WidthType.DXA },
              children: [new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 60, after: 60 },
                children: [new TextRun({ text, size: 22, font: "Calibri" })]
              })]
            })
          )
        })
      )
    ]
  });
}
```

#### docx-js — 5-Column Versioning Table (Procedures)

```javascript
function createProcedureVersioningTable(rows) {
  const colWidths = [1400, 1200, 1000, 4087, 1800];
  return new Table({
    width: { size: 9487, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [
      new TableRow({
        children: ["Fecha", "Estado", "Version", "Modificaciones", "Autor"].map((text, i) =>
          new TableCell({
            borders: versionBorders,
            width: { size: colWidths[i], type: WidthType.DXA },
            shading: headerShading,
            children: [new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { before: 60, after: 60 },
              children: [new TextRun({ text, bold: true, size: 22, font: "Calibri" })]
            })]
          })
        )
      }),
      ...rows.map(row =>
        new TableRow({
          children: row.map((text, i) =>
            new TableCell({
              borders: versionBorders,
              width: { size: colWidths[i], type: WidthType.DXA },
              children: [new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 60, after: 60 },
                children: [new TextRun({ text, size: 22, font: "Calibri" })]
              })]
            })
          )
        })
      )
    ]
  });
}
```

### Language

- **Primary**: `es-ES` (Spanish) — all document types except I02 Catalan
- **Secondary**: `ca-ES` (Catalan) — I02 variants only

```xml
<!-- Spanish (default) -->
<w:lang w:val="es-ES" w:eastAsia="en-US" w:bidi="ar-SA"/>

<!-- Catalan (I02) -->
<w:lang w:val="ca-ES" w:eastAsia="en-US" w:bidi="ar-SA"/>
```

---

## Layer 2: Per-Document-Type Guidelines

### Quick-Reference Decision Matrix

| Feature | D## Policies | I## Norms | I## Forms | P## Procedures | Records | DPT## Roles | I02 Catalan |
|---------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Title page** | 80pt gray | 40pt teal | No | 80pt gray (2-line) | No | No | No |
| **Versioning table** | 4-col | 4-col | No | 5-col (+Estado) | No | No | No |
| **TOC** | Yes | Yes | No | Yes | No | No | No |
| **Signature** | "Firma:" | "Firma:" | "Firmado:" + border | Yes | No | No | Implied |
| **Header** | 3-col table | 3-col table | 3-col elaborate | 3-col table | Simple | Elaborate (Segoe UI) | "USO INTERNO" only |
| **Footer** | Multi-section | Full | Simple | Multi-section | Single | Standard | Simple text |
| **Font** | Calibri | Calibri | Calibri | Calibri | Calibri | **Segoe UI** | Calibri |
| **Language** | es-ES | es-ES | es-ES | es-ES | es-ES | es-ES | **ca-ES** |
| **Location** | `01_POLITICAS/` | `02_NORMAS/` | `02_NORMAS/` | `03_PROCEDIMIENTOS/` | `04_REGISTROS/` | `05_ROLES/` | `02_NORMAS/` |

---

### D## Policies (`01_POLITICAS/`)

Documents: D01, D02, D03, D10

**Structure**: Cover page → Versioning table → TOC → Body → Signature

- **Cover**: Centered 80pt (160 half-points) Calibri, `#808080`, large logo, page break after
- **Versioning**: 4-column (Fecha / Version / Modificaciones / Autor)
- **TOC**: Titled "Indice"
- **Signature**: "Firma:" block
- **Sections**: Multi-section footers (cover, main, additional)
- **Numbering**: 9-level outline with mixed bullets/numbers

```javascript
// D## Policy skeleton
const doc = new Document({
  styles: OPTIMTECH_STYLES,
  sections: [
    // Section 1: Cover page
    {
      properties: { page: OPTIMTECH_PAGE },
      headers: { default: OPTIMTECH_HEADER },
      footers: { default: OPTIMTECH_FOOTER },
      children: [
        new Paragraph({ spacing: { before: 4000 } }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            // Large logo ImageRun here (2.25" x 0.93")
          ]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "POLICY TITLE", size: 160, color: "808080", font: "Calibri" })
          ]
        }),
        new Paragraph({ children: [new PageBreak()] }),
      ]
    },
    // Section 2: Versioning + TOC + Body
    {
      properties: { page: OPTIMTECH_PAGE },
      headers: { default: OPTIMTECH_HEADER },
      footers: { default: OPTIMTECH_FOOTER },
      children: [
        new Paragraph({
          heading: HeadingLevel.HEADING_1,
          children: [new TextRun("Control Documental")]
        }),
        createVersioningTable([
          ["DD/MM/YYYY", "1.0", "Initial version", "Author Name"]
        ]),
        new Paragraph({ children: [new PageBreak()] }),
        new TableOfContents("Indice", { hyperlink: true, headingStyleRange: "1-3" }),
        new Paragraph({ children: [new PageBreak()] }),
        // Body content...
        new Paragraph({
          heading: HeadingLevel.HEADING_1,
          children: [new TextRun("1. Section Title")]
        }),
        new Paragraph({
          children: [new TextRun({ text: "Body text...", size: 22, font: "Calibri" })]
        }),
      ]
    },
  ]
});
```

---

### I## Norms and Standards (`02_NORMAS/` — I01)

**Structure**: Cover page → Versioning table → TOC → Body → Signature

- **Cover**: Smaller title at 40pt (80 half-points) bold Calibri, `#0D9A76`, with "V1.0" version line
- **Versioning**: 4-column
- **TOC**: Yes, titled "Indice"
- **Signature**: "Firma:"
- **Header**: 3-column table (standard)

```javascript
// I## Norm cover title
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "NORM TITLE", size: 80, bold: true, color: "0D9A76", font: "Calibri" })
  ]
}),
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "V1.0", size: 28, color: "0D9A76", font: "Calibri" })
  ]
}),
```

---

### I## Forms (`02_NORMAS/` — I03, I04, I05)

**Structure**: Header → Body text → Form fields → Signature

- **No title page, no versioning table, no TOC**
- **Yellow highlighting** on fillable fields: `w:highlight w:val="yellow"`
- **Table header rows**: `#F1FDF9` (Form Green) background
- **Elaborate header**: 3-column table (~16KB XML), logo + title + ref + "USO INTERNO"
- **Signature**: "Firmado:" with top border line (`w:pBdr`)
- **Short documents** (~539 lines XML)

```javascript
// Form field highlight
new TextRun({
  text: "[COMPLETAR]",
  font: "Calibri", size: 22,
  highlight: "yellow"
})

// Form table header cell
new TableCell({
  shading: { fill: "F1FDF9", type: ShadingType.CLEAR },
  children: [new Paragraph({
    children: [new TextRun({ text: "Campo", bold: true, font: "Calibri", size: 22 })]
  })]
})
```

#### XML form field pattern

```xml
<w:r>
  <w:rPr>
    <w:highlight w:val="yellow"/>
    <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
  </w:rPr>
  <w:t>[COMPLETAR]</w:t>
</w:r>

<w:tc>
  <w:tcPr>
    <w:shd w:val="clear" w:color="auto" w:fill="F1FDF9"/>
  </w:tcPr>
  <w:p>
    <w:r><w:rPr><w:b/></w:rPr><w:t>Campo</w:t></w:r>
  </w:p>
</w:tc>
```

---

### P## Procedures (`03_PROCEDIMIENTOS/`)

Documents: P01–P05, plus software development procedure

**Structure**: Cover page → Versioning table → TOC → Body → Signature

- **Cover**: TWO centered lines at 80pt — "Procedimiento" then the specific title
- **Versioning**: **5 columns** (Fecha / Estado / Version / Modificaciones / Autor) — adds "Estado"
- **TOC**: Yes, after title page
- **Complex numbering**: numbering.xml can be 243KB+
- **Multi-section footers**

```javascript
// P## Procedure cover (two-line)
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "Procedimiento", size: 160, color: "808080", font: "Calibri" })
  ]
}),
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "Procedure Title", size: 160, color: "808080", font: "Calibri" })
  ]
}),
```

Use `createProcedureVersioningTable()` (5-column) for the versioning table.

---

### Records (`04_REGISTROS/`)

Documents: Procurement records (Atlassian, Azure, GCP), D00, D04–D13

**Structure**: Title → Key-value metadata → Body

- **No title page** — starts with bold 36pt (72 half-points) `#0D9A76` title
- **No versioning table** — key-value metadata pairs instead (Procedimiento, Proveedor, Tipo de servicio)
- **No TOC, no signature**
- **Single header, single footer**
- **Minimal structure**, metadata-driven

```javascript
// Record title
new Paragraph({
  children: [
    new TextRun({ text: "Record Title", size: 72, bold: true, color: "0D9A76", font: "Calibri" })
  ]
}),
```

---

### DPT## Role Descriptions (`05_ROLES/`)

Documents: DPT01 (CISO), DPT02 (CTO), DPT03 (DPO), DPT04 (CEO), DPT05 (Auditor interno)

**Structure**: Header (elaborate) → Tables (15+)

- **No title page** — starts directly with Mission/Role Definition table
- **No separate versioning table** — control info embedded in header
- **No TOC, no signature**
- **Font**: **Segoe UI** throughout (not Calibri)
- **Elaborate header** (~18KB XML): Logo + "DESCRIPCION DE PUESTO DE TRABAJO" + role title + "DPT## Rev.01" + "USO INTERNO"
- **Table-first design**: 15+ tables for mission, reporting line, competencies, skills, responsibilities

Use `DPT_STYLES` (Segoe UI override) when creating these documents.

---

### I02 Catalan Variants (`02_NORMAS/`)

Documents: I02-L-CA (laboral), I02-P-CA (professional)

**Structure**: Legal title → Dense paragraphs → Date/signature field

- **No title page** — centered legal title at 20pt (40 half-points) bold, default color
- **No versioning table, no TOC**
- **ALL `w:lang` tags**: `ca-ES`
- **Minimal branding** — no corporate `#0D9A76` color
- **Header**: "USO INTERNO" text only (no logo table)
- **Footer**: Simple text company info
- **Date field**: "En _______________, a ___ de ______________ de ______"
- **Salutation**: "Apreciat/a treballador/a,"

```xml
<!-- Catalan language setting in docDefaults -->
<w:docDefaults>
  <w:rPrDefault>
    <w:rPr>
      <w:rFonts w:asciiTheme="minorHAnsi" w:hAnsiTheme="minorHAnsi"/>
      <w:sz w:val="22"/>
      <w:lang w:val="ca-ES" w:eastAsia="en-US" w:bidi="ar-SA"/>
    </w:rPr>
  </w:rPrDefault>
</w:docDefaults>
```

---

## Document Creation Checklist

When creating any new ENS document:

1. **Identify document type** — Match the prefix (D##, I##, P##, DPT##) to the decision matrix above
2. **Apply page setup** — Use `OPTIMTECH_PAGE` (A4, asymmetric margins)
3. **Set styles** — Use `OPTIMTECH_STYLES` (or `DPT_STYLES` for role descriptions)
4. **Add header** — 3-column table with Segoe UI Bold, `#BFBFBF` borders, logo in right cell
5. **Add footer** — OPTIMTECH footer with company info, italic 8pt `#404040`
6. **Build title page** (if applicable) — Check matrix for style (80pt gray, 40pt teal, or none)
7. **Add versioning table** (if applicable) — 4-col or 5-col with `#D1FBF0` header fill
8. **Add TOC** (if applicable) — Titled "Indice", heading range 1–3
9. **Set language** — `es-ES` default; `ca-ES` for I02 Catalan variants
10. **Validate** — Run `python scripts/office/validate.py output.docx`

### Logo Extraction

To get the logo PNG from an existing document:

```bash
python scripts/office/unpack.py "PLANTILLAS/Plantilla ENS.docx" /tmp/template_unpacked/
cp /tmp/template_unpacked/word/media/image1.png ./logo.png
```

---

## Template References

- **Base template**: `PLANTILLAS/Plantilla ENS.docx` — extract logo, header/footer XML, and base styles
- **Catalan template**: `PLANTILLAS/Plantilla ENS generica.docx` — Catalan defaults
- **Procedure template**: `PLANTILLAS/PR-020 Procedimiento de Desarrollo de Software.docx`

### Multi-Section Footer Architecture

D## policies and P## procedures use multiple footer sections:
- `footer1.xml`: Cover page footer
- `footer2.xml`: Main content footer
- `footer3.xml`: Additional section footer
- Enabled by `w:titlePg` element for first-page differentiation

### Table Styles Found in Corpus

| Style | Borders | Usage |
|-------|---------|-------|
| **Table Grid** (`Taulaambquadrcula`) | All borders, 4pt `#D9D9D9` | Versioning tables, general tables |
| **Plain Table 2** (`Taulasenzilla2`) | Top/bottom only, 4pt `#7F7F7F`, first row bold | Lightweight data tables |
