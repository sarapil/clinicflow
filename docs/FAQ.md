# ClinicFlow — Frequently Asked Questions
# كلينك فلو — الأسئلة الشائعة

## General — عام

### ❓ What is ClinicFlow?
ClinicFlow is Full-featured clinic management system. It is part of the Arkan Lab ecosystem.

**ما هو كلينك فلو؟**
نظام إدارة عيادات متكامل. جزء من منظومة أركان لاب.

### ❓ What are the system requirements?
- Frappe v16+ with Python 3.14+
- Required apps: frappe, frappe_visual, arkan_help, caps, medcode

### ❓ How do I install ClinicFlow?
```bash
bench get-app clinicflow
bench --site dev.localhost install-app clinicflow
bench --site dev.localhost migrate
```

### ❓ Is Arabic supported?
Yes — full Arabic RTL interface with bilingual support.

**هل يدعم اللغة العربية؟**
نعم — واجهة عربية كاملة مع دعم ثنائي اللغة.

### ❓ How do I report a bug?
Use the GitHub issue templates — select "Bug Report" and fill in the details.

## Feature-Specific — خاص بالميزات

### ❓ How does Patient registration and medical records?
See the [Training Guide](TRAINING.md) for step-by-step instructions.
### ❓ How does Appointment scheduling with visual calendar?
See the [Training Guide](TRAINING.md) for step-by-step instructions.
### ❓ How does Prescription management with drug database?
See the [Training Guide](TRAINING.md) for step-by-step instructions.


## Troubleshooting — استكشاف الأخطاء

### ❓ The page shows a 500 error
Clear cache: `bench --site dev.localhost clear-cache && bench build --app clinicflow`

### ❓ Translations are not showing
Run: `bench --site dev.localhost clear-cache` and reload the page.

---

*Last updated: April 2026*
