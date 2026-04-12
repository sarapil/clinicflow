---
title: CF Patient — Patient Registration
icon: person
context_type: doctype
context_reference: CF Patient
priority: 10
roles: [CF Receptionist, Administrator]
---

# CF Patient — Patient Registration

The **CF Patient** form is used to register new patients and maintain their complete medical profile.

## ## patient_id

The **Patient ID** is auto-generated when you save a new patient. Format: `MC-YYYY-###` (e.g., MC-2025-001).

## ## full_name

Enter the patient's **full legal name** as it appears on their ID document. This name will appear on all forms, prescriptions, and invoices.

## ## full_name_ar

The patient's name in **Arabic script** (if applicable). Used for Arabic printed documents.

## ## date_of_birth

Enter the patient's **date of birth**. Age is automatically calculated from this field.

## ## gender

Select: Male / Female / Other

## ## phone

The patient's **primary phone number**. Used for appointment reminders (SMS via NotifyPro).

## ## email

The patient's **email address** for digital reports and appointment confirmations.

## ## blood_type

Select the patient's **blood group**: A+, A−, B+, B−, AB+, AB−, O+, O−

## ## national_id

The patient's **National Identification Number** (NIN or equivalent). Used for insurance claim verification.

## ## insurance_policy

Link to the patient's active **CF Insurance Policy** for automatic billing split calculations.

## ## allergies (child table)

List all known **drug or environmental allergies**. Each allergy includes:

- Allergen name
- Severity (Mild / Moderate / Severe / Life-threatening)
- Reaction description

## ## chronic_conditions (child table)

List all **chronic diseases** the patient is being treated for. Links to MC ICD10 Code for standardized coding.

## Quick Actions

- **New Appointment**: Click "Book Appointment" to schedule directly from the patient record
- **Patient Summary**: View consultation history, pending orders, and outstanding invoices
- **Print Patient Card**: Generate a printable patient ID card
