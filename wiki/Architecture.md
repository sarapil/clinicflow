# Architecture — البنية التقنية

## App Structure — هيكل التطبيق

```
clinicflow/clinicflow/
├── patient_management/   Patient registration and history
├── appointment/          Scheduling and slot management
├── consultation/         EMR: vitals, diagnosis, treatment
├── prescription/         Drug prescriptions and dispensing
├── laboratory/           Lab orders and results
├── radiology/            Radiology orders and results
├── billing/              Invoices and payments
├── insurance/            Claims and policy management
├── pharmacy/             Pharmacy bin and transactions
├── clinical_settings/    Doctor schedules and templates
├── cf_ai_clinical/       AI suggestion engine
├── api/v1/               REST API
├── services/             Business logic layer
└── caps/                 CAPS capability gate
```

## Design Patterns — أنماط التصميم

- **Thin Controller**: DocType controllers delegate to `services/` layer
- **Parameterized SQL**: All queries use `%(param)s` placeholders
- **extend_doctype_class**: Never override_doctype_class
- **CAPS Gate**: All permission checks via `caps/gate.py`

## Key Dependencies — التبعيات الرئيسية

See [Getting Started](Getting-Started) for full prerequisite list.
