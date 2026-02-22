# PA-BKP-001 — Backup y Restauración Confluence Cloud

| Campo | Valor |
|-------|-------|
| **ID** | PA-BKP-001 |
| **Dominio** | BKP — Backup y Recuperación |
| **Tipo** | Procedimiento Aplicado (SOP) |
| **Propietario** | IT / Administración de Sistemas |
| **Aplica a** | Atlassian Cloud (Confluence) |
| **Entorno** | Atlassian Cloud (SaaS) |
| **Estado** | Vigente |
| **Última revisión** | 2026-02-22 |

---

# 1. Purpose

This procedure defines how the company:

- Creates manual backups of Confluence Cloud
- Validates backup integrity
- Tests restore safely
- Performs controlled production restore when necessary

The goal is to ensure data integrity, operational continuity, and controlled recovery in case of data loss or corruption.

---

# 2. Scope

This SOP applies to:

- Full Confluence site backups
- Space-level restores
- Full production restore scenarios

This SOP does NOT cover Jira Cloud backups.

---

# 3. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| System Administrator | Execute backup and restore procedures |
| IT Lead | Authorize production restore |
| Business Owner | Approve major rollback decisions |

---

# 4. Backup Procedure (Manual)

## 4.1 Frequency

- Minimum: Weekly
- Recommended: Before major changes, migrations, or app installs

## 4.2 Steps to Create Backup

1. Log in as Confluence Administrator.
2. Navigate to:  
   **Settings → Data Management → Backup manager**
3. Select: **Create backup for cloud**
4. Ensure "Backup attachments" is checked.
5. Wait for backup completion.
6. Download the generated XML file.

## 4.3 Backup Storage

- Store backup in secure company storage (encrypted cloud storage or secure server).
- Maintain minimum 4 weekly backups.
- Record:
  - Backup date
  - File size
  - Storage location

---

# 5. Backup Validation (Restore Test Procedure)

Restore testing must be performed at least once per year.

## 5.1 Create Test Site

1. Go to admin.atlassian.com
2. Create a new temporary site
3. Add Confluence to the new site

## 5.2 Import Backup

1. In the test site, go to:
   **Settings → Data Management → Import site**
2. Upload the XML backup file
3. Wait for import completion

## 5.3 Validation Checklist

After restore, verify:

- All spaces exist
- Page counts match production
- Attachments open correctly
- Comments are visible
- Page history is accessible
- Permissions are correctly applied
- Macros render properly

Document validation results.

If validation fails, escalate to IT Lead.

---

# 6. Production Restore Procedure

⚠ Production restore is destructive and replaces all existing content.

## 6.1 When Full Restore Is Allowed

Full restore may be executed only in cases of:

- Major data corruption
- Large-scale accidental deletion
- Critical structural failure

Approval from IT Lead and Business Owner is required.

## 6.2 Production Restore Steps

1. Notify all users of maintenance window.
2. Restrict user access.
3. Navigate to:
   **Settings → Data Management → Import site**
4. Upload approved backup file.
5. Wait for import completion.
6. Perform validation checklist (Section 5.3).
7. Reopen system access.

---

# 7. Partial Recovery Procedure (Recommended for Most Incidents)

If only one space or limited content is affected:

1. Restore backup into test site.
2. Export required space from test site.
3. Import space into production using:
   **Settings → Data Management → Import spaces**

This avoids full production overwrite.

---

# 8. Limitations of Confluence Cloud Restore

- No point-in-time rollback
- No object-level restore natively
- Full site import replaces all content
- Marketplace app data may not fully restore

These limitations must be considered in risk planning.

---

# 9. Documentation and Audit

For each backup and restore action, record:

- Date
- Responsible administrator
- Backup file name
- Validation results
- Approval reference (if production restore)

Maintain records for minimum 12 months.

---

# 10. Review Cycle

This SOP must be reviewed annually or after:

- Major incident
- Significant Atlassian platform change
- Infrastructure policy update

---

**End of Procedure**

