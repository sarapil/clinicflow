# Contributing to ClinicFlow — المساهمة في ClinicFlow

> **Language / اللغة:** English first, with Arabic translations for all user-facing content.

## Welcome — مرحباً

Thank you for your interest in contributing to **ClinicFlow** — the Outpatient Clinic Management System for the Arkan Lab ecosystem. ClinicFlow covers patient registration, appointments, EMR, lab orders, radiology, billing, insurance (including Nigerian HMOs), and pharmacy.

شكراً لاهتمامك بالمساهمة في **ClinicFlow** — نظام إدارة العيادات الخارجية.

## Code of Conduct — مدونة السلوك

By participating you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Patient Data Responsibility — مسؤولية بيانات المرضى

ClinicFlow handles **Protected Health Information (PHI)**. Contributors must:

- Never log patient names, IDs, or medical record data
- Ensure all patient APIs have proper CAPS permission checks
- Follow NDPR (Nigeria) and HIPAA (international) principles
- Report any PHI exposure immediately to security@arkan.it.com

## Getting Started — البدء

### Prerequisites

```
Python 3.11+ | Node.js v18+ | Frappe v16+
Required apps: frappe, erpnext, frappe_visual, arkan_help, caps, medcode
```

### Development Setup

```bash
git clone https://github.com/sarapil/clinicflow.git
cd /workspaces/frappe_docker/frappe-bench/apps
bench get-app clinicflow --skip-assets
bench --site dev.localhost install-app clinicflow
bench --site dev.localhost migrate
```

## Branch Strategy — استراتيجية الفروع

```
main          → Production (protected, requires 1 review + CI pass)
develop       → Integration testing
feat/CF-#-desc → Feature branches
fix/CF-#-desc  → Bug fix branches
```

## Commit Convention — اتفاقية الالتزام

```
feat(clinicflow): add insurance claim auto-submission
fix(clinicflow): correct appointment slot overlap detection
docs(clinicflow): update Arabic help for billing module
i18n(clinicflow): add Turkish translations for patient forms
test(clinicflow): integration tests for consultation workflow
security(clinicflow): add rate limiting to patient search API
```

## DocType Naming Convention — اتفاقية تسمية DocTypes

All ClinicFlow DocTypes use the `CF` prefix:

```
CF Patient, CF Appointment, CF Consultation, CF Lab Order,
CF Prescription, CF Clinic Invoice, CF Insurance Claim, etc.
```

## Service Layer Pattern — نمط طبقة الخدمة

Business logic MUST live in `services/`, NOT in DocType controllers:

```python
# ✅ Correct — thin controller
class CFAppointment(Document):
    def validate(self):
        from clinicflow.services.appointment_service import AppointmentService
        AppointmentService.validate_appointment(self)

# ❌ Forbidden — fat controller
class CFAppointment(Document):
    def validate(self):
        # 200 lines of business logic inline...
```

## Pull Request Checklist

- [ ] `CF` prefix on all new DocTypes
- [ ] Business logic in `services/`, not DocType controllers
- [ ] CAPS permissions declared for new features
- [ ] Arabic translations added to `clinicflow/translations/ar.csv`
- [ ] Patient data: no PHI in logs, proper permission checks
- [ ] SQL: parameterized queries only
- [ ] Tests added (unit + integration)
- [ ] Help content added to `clinicflow/help/en/` and `clinicflow/help/ar/`

## Testing — الاختبار

```bash
bench --site dev.localhost run-tests --app clinicflow
```

## Issue Labels

| Label                | Use for            |
| -------------------- | ------------------ |
| `bug`                | Incorrect behavior |
| `priority: critical` | Patient data risk  |
| `scope: api`         | API changes        |
| `scope: doctype`     | Schema changes     |
| `scope: billing`     | Billing/insurance  |
| `i18n`               | Translation        |

## Contact

- Security (PHI/vulnerabilities): security@arkan.it.com
- General: hello@arkan.it.com

---

_Arkan Lab — Empowering healthcare with open-source technology._
