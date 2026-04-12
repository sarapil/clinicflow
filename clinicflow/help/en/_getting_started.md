---
title: Getting Started with ClinicFlow
icon: rocket
context_type: guide
priority: 2
roles: [Administrator]
---

# Getting Started — البدء

This guide walks through the initial setup of ClinicFlow for your clinic.

## Step 1: Configure Clinical Settings

Go to **CF Clinical Settings** (Single DocType):

- `default_consultation_duration`: e.g., 15 (minutes)
- `auto_generate_queue`: Enable for automatic queue management
- `sms_reminders`: Enable to send appointment reminders via NotifyPro
- `reminder_hours_before`: e.g., 24 (send reminder 24h before appointment)

## Step 2: Set Up Services (CF Service)

Create entries for all billable services:

```
CONS-001 | Consultation (New Patient)    | Consultation | ₦5,000
CONS-002 | Consultation (Follow Up)      | Consultation | ₦3,000
LAB-001  | Full Blood Count (FBC)        | Lab Test     | ₦2,500
LAB-002  | Malaria Rapid Test            | Lab Test     | ₦1,500
RAD-001  | Chest X-Ray                   | Radiology    | ₦8,000
```

⚠️ **Important**: `service_code` is the autoname field — it must be unique and filled.

## Step 3: Configure Insurance Policies (CF Insurance Policy)

Add your accepted HMO/insurance providers:

- Policy Name, Provider name
- Coverage type (Inpatient/Outpatient/Both)
- Coverage percentage (e.g., 80%)
- Annual limit

## Step 4: Add Doctor Schedules (CF Doctor Schedule)

For each doctor, create a **CF Doctor Schedule** with:

- Days of the week (Mon-Fri)
- Start and end times
- Consultation duration (generates CF Appointment Templates)

## Step 5: Register First Patient

Use the **CF Patient** form:

1. Enter full name, date of birth, gender, phone
2. Add allergies (if known)
3. Link insurance policy (if applicable)
4. Save → Patient ID is auto-generated

## Step 6: Book First Appointment

1. Open CF Appointment (or click "New Appointment" from CF Patient)
2. Select patient, doctor, date
3. Available slots appear automatically
4. Select slot and save

## Verification Checklist

- [ ] CF Clinical Settings configured
- [ ] At least 5 CF Service records created
- [ ] Insurance policies added for your HMO partners
- [ ] Doctor schedules set up
- [ ] Test patient registered and appointment booked
