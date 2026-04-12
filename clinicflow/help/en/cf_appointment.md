---
title: CF Appointment — Appointment Booking
icon: calendar
context_type: doctype
context_reference: CF Appointment
priority: 9
roles: [CF Receptionist, CF Doctor, Administrator]
---

# CF Appointment — Appointment Booking

The **CF Appointment** form manages patient appointment scheduling with real-time slot availability checking.

## ## patient

Link to a **CF Patient** record. Type the patient name or ID to search.

## ## doctor

Select the **treating doctor** (link to User). The available time slots are loaded based on the doctor's schedule.

## ## appointment_date

Select the **date** for the appointment. Only dates with available slots are enabled.

## ## slot

Select an available **time slot** from the doctor's schedule. Slots are validated against existing bookings to prevent double-booking.

## ## appointment_type

Select the type:

- **New Patient** (first visit)
- **Follow Up** (returning patient)
- **Emergency** (urgent, bypasses normal queue)
- **Telemedicine** (video consultation)

## ## chief_complaint

Brief description of the **reason for visit**. This pre-populates the consultation chief complaint field.

## ## status

| Status      | Meaning                   |
| ----------- | ------------------------- |
| Scheduled   | Appointment booked        |
| Checked In  | Patient arrived at clinic |
| In Progress | Doctor seeing patient     |
| Completed   | Consultation done         |
| Cancelled   | Appointment was cancelled |
| No Show     | Patient did not arrive    |

## ## reminder_sent

Checkbox automatically set when the SMS reminder is sent (via NotifyPro 24 hours before the appointment).

## Workflow

1. Receptionist books appointment → Status: **Scheduled**
2. Patient arrives → Click "Check In" → Status: **Checked In**
3. Doctor starts consultation → Status: **In Progress**
4. Consultation saved → Status: **Completed**

## Quick Actions

- **Create Consultation**: Automatically creates a CF Consultation linked to this appointment
- **Reschedule**: Move the appointment to a different slot
- **Cancel**: Cancel with reason (patient record updated)
- **Send Reminder**: Manually trigger SMS reminder
