# API Reference — مرجع API

All endpoints are `@frappe.whitelist()` and require authentication.

## Endpoints — نقاط الوصول

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `clinicflow.api.v1.patients.get_patients` | Paginated patient list |
| GET | `clinicflow.api.v1.patients.get_patient` | Single patient + summary |
| GET | `clinicflow.api.v1.appointments.get_appointments` | Appointment list |
| GET | `clinicflow.api.v1.appointments.get_available_slots` | Open time slots |
| POST | `clinicflow.api.v1.appointments.book_appointment` | Book appointment |
| POST | `clinicflow.api.v1.appointments.cancel_appointment` | Cancel appointment |
| GET | `clinicflow.api.v1.clinical.get_patient_consultations` | Consultation history |
| GET | `clinicflow.api.v1.clinical.get_consultation` | Single consultation |
| GET | `clinicflow.api.v1.clinical.get_patient_vitals` | Vitals history |

## Authentication — المصادقة

```
POST /api/method/login
  Body: usr=<email>&pwd=<password>
  Returns: Set-Cookie session token
```

## Response Format — تنسيق الاستجابة

```json
{"status": "success", "data": {...}, "message": null}
{"status": "error", "error_code": "VALIDATION_ERROR", "message": "Human-readable error"}
{"status": "success", "data": [...], "meta": {"total": 100, "page": 1, "page_size": 20}}
```
