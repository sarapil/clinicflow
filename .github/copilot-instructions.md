# ClinicFlow — AI Copilot Instructions

## Overview

**ClinicFlow** (clinicflow) is an Arkan Lab Frappe v16 application.
Comprehensive clinic management system integrated with ERPNext

**Brand Color:** #EF4444

## Architecture

- **Framework:** Frappe v16 + ERPNext v16
- **Pattern:** Thin Controller → Service Layer (mandatory)
- **Permissions:** CAPS capability-based access control
- **UI:** frappe_visual components (307+ available)
- **i18n:** Arabic (ar) + English (en) mandatory

## Key Rules

1. Use `extend_doctype_class` — **NEVER** `override_doctype_class`
2. All business logic in `services/` layer — thin controllers only
3. Parameterized SQL only — **NEVER** raw f-string queries
4. All `@frappe.whitelist()` APIs must have permission checks as first line
5. No `frappe.db.commit()` inside document events
6. CSS Logical Properties only (`margin-inline-start`, NOT `margin-left`)
7. All strings wrapped in `__()` for i18n
8. Icons via `frappe.visual.icons.*` — NEVER Font Awesome

## DocType Prefix

All DocTypes use the `CF` prefix.

## Refer To

- `/workspaces/frappe_docker/.github/copilot-instructions.md` — Master constitution
- `docs/ARCHITECTURE.md` — App-specific architecture
- `CONTEXT.md` — Quick context reference
