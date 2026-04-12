---
title: CF Lab Order — Lab Test Ordering
icon: flask
context_type: doctype
context_reference: CF Lab Order
priority: 7
roles: [CF Doctor, CF Lab Technician, Administrator]
---

# CF Lab Order — Lab Test Ordering

The **CF Lab Order** allows doctors to order laboratory tests for patients, with results linked to LOINC codes.

## ## consultation

Link to the **CF Consultation** that requested these tests.

## ## patient

The **patient** (auto-populated from consultation).

## ## items (child table)

Each ordered test includes:

- LOINC code (from MedCode database)
- Test name
- Specimen type (blood, urine, swab, etc.)
- Priority (Routine / Urgent / STAT)

## ## status

| Status             | Meaning             |
| ------------------ | ------------------- |
| Ordered            | Tests requested     |
| Specimen Collected | Sample collected    |
| Processing         | Tests being run     |
| Results Available  | Ready for review    |
| Verified           | Doctor has reviewed |

## Workflow

1. Doctor creates CF Lab Order from consultation
2. Lab technician collects specimen → Updates status to "Specimen Collected"
3. Tests processed → Lab enters results in CF Lab Result
4. Status updates to "Results Available"
5. Doctor reviews → Status: "Verified"
6. Results auto-link back to the consultation

## Result Entry (CF Lab Result)

Each result item includes:

- Test value
- Unit (e.g., mg/dL, mmol/L)
- Reference range
- Abnormal flag (High/Low/Critical)

Critical values automatically trigger a notification to the ordering doctor.
