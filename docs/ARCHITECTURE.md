# ClinicFlow Architecture — بنية ClinicFlow

## Overview — نظرة عامة

ClinicFlow is a comprehensive **Outpatient Clinic Management System** built on Frappe/ERPNext. It covers the full outpatient workflow: patient registration → appointment booking → consultation (EMR) → orders (lab/radiology) → dispensing → billing → insurance claims.

**App prefix:** `CF` | **Color:** `#0EA5E9` Sky Blue | **Wave:** 3 Vertical

---

## Module Structure — هيكل الوحدات

```
clinicflow/clinicflow/
├── patient_management/ → CF Patient + related (5 DocTypes)
├── appointment/        → Scheduling system (5 DocTypes)
├── consultation/       → EMR / clinical notes (7 DocTypes)
├── prescription/       → Drug orders (4 DocTypes)
├── laboratory/         → Lab orders + results (4 DocTypes)
├── radiology/          → Imaging orders (2 DocTypes)
├── billing/            → Invoicing (4 DocTypes)
├── insurance/          → Claims management (3 DocTypes)
├── pharmacy/           → Dispensing (2 DocTypes)
├── clinical_settings/  → Config + schedules (4 DocTypes)
├── cf_ai_clinical/     → AI suggestions (1 DocType)
├── api/v1/             → REST API endpoints
├── services/           → Service classes (AppointmentService, etc.)
├── caps/gate.py        → CAPS capability gate
├── translations/       → ar.csv (134 strings) + T2/T3
└── public/             → JS (5 files), CSS, images
```

**⚠️ Module naming:** The AI module is `cf_ai_clinical` (NOT `ai_clinical`) to avoid conflict with medcode's AI module.

---

## DocType Reference — مرجع DocTypes (42 total)

### Patient Management

| DocType                      | Key Fields                                                | Notes                      |
| ---------------------------- | --------------------------------------------------------- | -------------------------- |
| CF Patient                   | patient_id (autoname), full_name, dob, gender, phone, mrn | autoname = MC-{YYYY}-{###} |
| CF Patient Allergy           | patient (Link), allergen, severity, reaction              | Child Table                |
| CF Patient Chronic Condition | patient, icd_code (Link→MC ICD10 Code), diagnosis_date    | Child Table                |
| CF Patient Document          | patient, document_type, file_attachment                   | Child Table                |
| CF Emergency Contact         | patient, contact_name, relationship, phone                | Child Table                |

### Appointment

| DocType                 | Key Fields                                      | Notes                          |
| ----------------------- | ----------------------------------------------- | ------------------------------ |
| CF Appointment          | patient, doctor, appointment_date, slot, status | autoname = CF-APT-{YYYY}-{###} |
| CF Appointment Slot     | doctor, slot_date, start_time*, end_time*       | \*mandatory fields             |
| CF Appointment Template | template_name, start_time*, end_time*, duration | \*mandatory fields             |
| CF Appointment Queue    | date, queue_data (JSON)                         | Single DocType per day         |
| CF Wait List            | appointment, wait_position, estimated_wait      |                                |

### Consultation (EMR)

| DocType                   | Key Fields                                                  | Notes            |
| ------------------------- | ----------------------------------------------------------- | ---------------- |
| CF Consultation           | patient, doctor, appointment, chief_complaint               | Core EMR DocType |
| CF Vital Signs            | consultation, bp_systolic, bp_diastolic, temp, pulse, spo2  |                  |
| CF Diagnosis Item         | consultation, icd_code (Link→MC ICD10 Code), diagnosis_type | Child Table      |
| CF Chief Complaint Item   | consultation, complaint, duration, severity                 | Child Table      |
| CF Referral               | consultation, refer_to, refer_to_doctor, reason             |                  |
| CF Sick Leave Certificate | consultation, days, from_date, to_date                      |                  |
| CF Treatment Plan         | consultation, plan_items (child)                            |                  |

### Prescription

| DocType                 | Key Fields                                                   | Notes       |
| ----------------------- | ------------------------------------------------------------ | ----------- |
| CF Prescription         | consultation, patient, status                                |             |
| CF Prescription Item    | prescription, drug (Link→MC Drug), dose, frequency, duration | Child Table |
| CF Drug Dispensing      | prescription, dispensed_by, dispensed_at                     |             |
| CF Drug Dispensing Item | dispensing, drug, quantity_dispensed                         | Child Table |

### Laboratory

| DocType            | Key Fields                                                     | Notes       |
| ------------------ | -------------------------------------------------------------- | ----------- |
| CF Lab Order       | consultation, patient, status                                  |             |
| CF Lab Order Item  | lab_order, loinc_code (Link→MC LOINC Code), test_name          | Child Table |
| CF Lab Result      | lab_order, result_date, verified_by                            |             |
| CF Lab Result Item | lab_result, loinc_code, value, unit, reference_range, abnormal | Child Table |

### Radiology

| DocType             | Key Fields                                   | Notes |
| ------------------- | -------------------------------------------- | ----- |
| CF Radiology Order  | consultation, modality, body_region, urgency |       |
| CF Radiology Result | rad_order, findings, impression, radiologist |       |

### Billing

| DocType                | Key Fields                                                            | Notes                           |
| ---------------------- | --------------------------------------------------------------------- | ------------------------------- |
| CF Service             | service_code\* (autoname), service_name, category, unit_price         | \*autoname = field:service_code |
| CF Clinic Invoice      | patient, consultation, total_amount, insurance_amount, patient_amount |                                 |
| CF Clinic Invoice Item | invoice, service (Link→CF Service), quantity, unit_price, total       | Child Table                     |
| CF Clinic Payment      | invoice, payment_method, amount, payment_date                         |                                 |

**⚠️ CF Service `category` options:** "Consultation", "Lab Test", "Radiology", "Procedure", "Medication", "Other" — NOT "Laboratory"

### Insurance

| DocType                 | Key Fields                                             | Notes       |
| ----------------------- | ------------------------------------------------------ | ----------- |
| CF Insurance Policy     | policy_name, provider, coverage_type, coverage_percent |             |
| CF Insurance Claim      | invoice, policy, claim_amount, status                  |             |
| CF Insurance Claim Item | claim, service (Link→CF Service), covered_amount       | Child Table |

### Pharmacy

| DocType                 | Key Fields                                          | Notes |
| ----------------------- | --------------------------------------------------- | ----- |
| CF Pharmacy Bin         | drug (Link→MC Drug), quantity_on_hand, bin_location |       |
| CF Pharmacy Transaction | drug, transaction_type, quantity, dispensing (Link) |       |

### Clinical Settings

| DocType                  | Key Fields                                               | Notes          |
| ------------------------ | -------------------------------------------------------- | -------------- |
| CF Clinical Settings     | default_consultation_duration, auto_queue, sms_reminders | Single DocType |
| CF Doctor Schedule       | doctor (Link→User), schedule_days                        |                |
| CF Consultation Template | template_name, chief_complaints, screening_items         |                |
| CF Schedule Slot         | doctor_schedule (Link), weekday, start_time, end_time    | Child Table    |

### AI Clinical

| DocType          | Key Fields                                                 | Notes                    |
| ---------------- | ---------------------------------------------------------- | ------------------------ |
| CF AI Suggestion | consultation, suggestion_type, suggestion_text, confidence | AI-generated suggestions |

---

## Service Classes — فئات الخدمة

```python
# All service classes in clinicflow/services/

class AppointmentService:
    @staticmethod
    def book_appointment(patient, doctor, date, slot): ...
    @staticmethod
    def get_available_slots(doctor, date): ...
    @staticmethod
    def cancel_appointment(appointment_name, reason): ...

class ConsultationService:
    @staticmethod
    def create_consultation(patient, appointment): ...
    @staticmethod
    def validate_consultation(doc): ...

class BillingService:
    @staticmethod
    def create_invoice_from_consultation(consultation_name): ...
    @staticmethod
    def calculate_insurance_split(invoice, policy): ...

class PatientService:
    @staticmethod
    def generate_patient_id(): ...
    @staticmethod
    def get_patient_summary(patient_name): ...
```

---

## CAPS Capabilities

| Capability               | Category | Description                  |
| ------------------------ | -------- | ---------------------------- |
| `CF_register_patients`   | Module   | Create/edit patient records  |
| `CF_book_appointments`   | Action   | Book and manage appointments |
| `CF_view_clinical_notes` | Module   | Read EMR/consultation notes  |
| `CF_write_consultation`  | Action   | Create/edit consultations    |
| `CF_order_labs`          | Action   | Create lab orders            |
| `CF_view_lab_results`    | Module   | View lab results             |
| `CF_manage_billing`      | Action   | Create invoices and payments |
| `CF_manage_insurance`    | Action   | Manage insurance claims      |
| `CF_dispense_drugs`      | Action   | Pharmacy dispensing          |
| `CF_view_reports`        | Report   | Access analytics reports     |
| `CF_configure`           | Action   | Manage clinical settings     |

---

## Data Flow — تدفق البيانات

```
Patient Arrival
    ↓
CF Patient (registration) ← medcode.MC Specialty
    ↓
CF Appointment (scheduling) ← CF Doctor Schedule
    ↓
CF Consultation (EMR)
    ├── CF Vital Signs
    ├── CF Diagnosis Item ← medcode.MC ICD10 Code
    ├── CF Lab Order ← medcode.MC LOINC Code
    ├── CF Radiology Order
    └── CF Prescription ← medcode.MC Drug
         ↓
CF Clinic Invoice ← CF Service
    ├── CF Clinic Payment (cash/card)
    └── CF Insurance Claim ← CF Insurance Policy
```

---

## Known Constraints & Gotchas — قيود معروفة

1. **`CF Service` autoname**: `autoname = field:service_code` → `service_code` is MANDATORY on insert
2. **`CF Appointment Template`**: Both `start_time` and `end_time` are mandatory
3. **`CF Service.category`**: Must be one of the exact options above — "Lab Test" NOT "Laboratory"
4. **Module naming**: AI module is `cf_ai_clinical` to prevent collision with medcode's `ai_clinical`
5. **medcode dependency**: ICD codes (`MC ICD10 Code`) and drugs (`MC Drug`) must be seeded before clinical workflows
