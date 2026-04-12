# Permissions — الصلاحيات

## CAPS Capabilities — قدرات CAPS

| Capability | Category | Description |
| ---------- | -------- | ----------- |
| CF_manage_patients | Module | Register and edit patients |
| CF_view_medical_records | Module | Access full EMR history |
| CF_schedule_appointments | Action | Book/cancel appointments |
| CF_conduct_consultation | Action | Write consultation notes |
| CF_manage_prescriptions | Action | Create/edit prescriptions |
| CF_dispense_drugs | Action | Mark drugs as dispensed |
| CF_manage_lab_orders | Action | Order and result lab tests |
| CF_manage_billing | Module | Create invoices and payments |
| CF_submit_insurance_claims | Action | Submit to HMO/insurer |
| CF_configure_clinic | Action | Modify clinic settings |

## Permission Check Pattern

```python
from clinicflow.caps.gate import check_user_capability

# Throws PermissionDenied if user lacks capability
check_user_capability("CF_manage_patients")

# Returns bool without throwing
has_perm = check_user_capability("CF_view_medical_records", throw=False)
```
