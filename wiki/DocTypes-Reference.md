# DocTypes Reference — مرجع أنواع البيانات

## All DocTypes — جميع أنواع البيانات

| DocType | Module | Description |
| ------- | ------ | ----------- |
| CF Patient | Patient Management | Core patient record |
| CF Appointment | Appointment | Clinic appointment |
| CF Consultation | Consultation | Clinical encounter notes |
| CF Vital Signs | Consultation | Patient vital measurements |
| CF Prescription | Prescription | Drug prescription |
| CF Prescription Item | Prescription | Child table — drugs |
| CF Lab Order | Laboratory | Lab test request |
| CF Lab Result | Laboratory | Lab test results |
| CF Radiology Order | Radiology | Imaging request |
| CF Radiology Result | Radiology | Imaging result |
| CF Clinic Invoice | Billing | Invoice to patient |
| CF Clinic Payment | Billing | Payment record |
| CF Insurance Claim | Insurance | HMO/insurer claim |
| CF Insurance Policy | Insurance | Patient insurance coverage |
| CF Service | Billing | Billable service catalog |
| CF Doctor Schedule | Clinical Settings | Practitioner availability |
| CF Appointment Template | Clinical Settings | Slot template |
| CF Clinical Settings | Clinical Settings | App configuration (single) |
| CF AI Suggestion | CF AI Clinical | AI differential suggestion |

> **Naming**: All DocTypes prefixed with `CL` to avoid namespace collisions.
> **Fields**: snake_case; child tables end with `Item` or `Detail`.
