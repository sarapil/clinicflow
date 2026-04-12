---
title: CF Consultation — Electronic Medical Record
icon: stethoscope
context_type: doctype
context_reference: CF Consultation
priority: 8
roles: [CF Doctor, CF Nurse, Administrator]
---

# CF Consultation — Electronic Medical Record (EMR)

The **CF Consultation** is the core EMR document. It captures the complete clinical encounter: vital signs, diagnosis, orders, and treatment plan.

## ## patient

Link to the **CF Patient** being seen.

## ## doctor

The **treating physician** conducting this consultation.

## ## appointment

Link to the **CF Appointment** that triggered this consultation (optional for walk-in patients).

## ## consultation_date

The **date and time** of the consultation. Defaults to now.

## ## chief_complaints (child table)

List the patient's **presenting complaints**. For each complaint, record:

- Complaint description
- Duration (e.g., "3 days", "2 weeks")
- Severity (1-10 scale)

## ## vital_signs (linked)

Record in the **CF Vital Signs** sub-form:

- Blood pressure (systolic/diastolic)
- Temperature (°C or °F)
- Pulse rate (bpm)
- Respiratory rate
- Oxygen saturation (SpO₂ %)
- Weight and height (BMI auto-calculated)

## ## diagnosis_items (child table)

Add one or more **diagnoses** linked to ICD-10 codes:

- Search by code or description (uses MedCode ICD database)
- Specify: Primary / Secondary / Rule-out / Working
- Add clinical notes per diagnosis

## ## clinical_notes

Free-text **SOAP notes** field for the doctor's clinical observations. Supports markdown format.

## ## prescription_link

After clicking "Create Prescription", this links to the generated **CF Prescription**.

## ## lab_order_link

Links to the created **CF Lab Order** for test requests.

## ## treatment_plan

Summary of the **treatment plan** including interventions, medications, and follow-up instructions.

## ## follow_up_date

If a follow-up appointment is needed, set the **recommended return date**.

## Workflow

1. Doctor opens consultation → enters vital signs
2. Records chief complaints and examination findings
3. Adds diagnoses with ICD-10 codes
4. Creates prescription (if needed) → CF Prescription
5. Orders lab tests (if needed) → CF Lab Order
6. Orders radiology (if needed) → CF Radiology Order
7. Saves and submits consultation → generates invoice automatically

## Quick Actions

- **Create Prescription**: Opens a new CF Prescription pre-filled with patient/doctor
- **Order Lab Tests**: Opens CF Lab Order
- **Order Radiology**: Opens CF Radiology Order
- **Issue Sick Leave**: Generates CF Sick Leave Certificate
- **Refer Patient**: Creates CF Referral letter
- **Print Summary**: Patient-friendly consultation summary
