# Getting Started — البدء السريع

## Prerequisites — المتطلبات المسبقة

- Frappe bench v16.x on Python 3.11+
- MariaDB 10.6+ (TCP/IP mode — no socket)
- Node.js 18+
- Required apps: `frappe>=16, frappe_visual>=0.1.0, arkan_help>=0.0.1, caps>=1.0.0, medcode>=0.0.1`

## Installation — التثبيت

```bash
# 1. Get the app
bench get-app clinicflow https://github.com/sarapil/clinicflow

# 2. Install on site
bench --site <your-site> install-app clinicflow

# 3. Run migration
bench --site <your-site> migrate
```

## First Steps — الخطوات الأولى

1. Open `/desk` and look for the **ClinicFlow** icon
2. Navigate to **Settings** to configure the app
3. Follow the onboarding wizard (❓ button on dashboard)

## Quick Test — اختبار سريع

```bash
bench --site <your-site> run-tests --app clinicflow
```
