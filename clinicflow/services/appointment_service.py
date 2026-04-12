# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe
from frappe import _
from frappe.utils import getdate, get_time, now_datetime, add_to_date
from clinicflow.exceptions import AppointmentConflict, PractitionerUnavailable


class AppointmentService:

    @staticmethod
    def get_available_slots(practitioner: str, date: str) -> list[dict]:
        """Return list of available time slots for practitioner on date."""
        day_name = getdate(date).strftime("%A")
        schedules = frappe.get_all(
            "CF Doctor Schedule",
            filters={"practitioner": practitioner, "day_of_week": day_name, "is_active": 1},
            fields=["from_time", "to_time", "slot_duration"],
        )
        if not schedules:
            return []

        booked = frappe.get_all(
            "CF Appointment",
            filters={"practitioner": practitioner, "appointment_date": date,
                     "status": ["not in", ["Cancelled", "No Show"]]},
            pluck="appointment_time",
        )
        booked_set = {str(t) for t in booked}

        slots = []
        for sched in schedules:
            slot_mins = sched.slot_duration or 30
            current = get_time(sched.from_time)
            end = get_time(sched.to_time)
            import datetime
            while current < end:
                time_str = current.strftime("%H:%M:%S")
                slots.append({
                    "time": time_str,
                    "available": time_str not in booked_set,
                })
                current = (datetime.datetime.combine(datetime.date.today(), current)
                           + datetime.timedelta(minutes=slot_mins)).time()
        return slots

    @staticmethod
    def book_appointment(patient: str, practitioner: str, appointment_date: str,
                         appointment_time: str, appointment_type: str = None,
                         notes: str = None) -> object:
        """Create a new appointment with conflict checking."""
        # Check slot available
        slots = AppointmentService.get_available_slots(practitioner, appointment_date)
        slot_times = {s["time"] for s in slots if s["available"]}
        if appointment_time not in slot_times:
            frappe.throw(_("Selected time slot is not available"), AppointmentConflict)

        patient_doc = frappe.get_doc("CF Patient", patient)
        doc = frappe.get_doc({
            "doctype": "CF Appointment",
            "patient": patient,
            "patient_name": patient_doc.patient_name,
            "practitioner": practitioner,
            "appointment_date": appointment_date,
            "appointment_time": appointment_time,
            "appointment_type": appointment_type or "General Consultation",
            "status": "Scheduled",
            "notes": notes,
            "reminder_sent": 0,
        })
        doc.insert(ignore_permissions=True)
        return doc

    @staticmethod
    def cancel_appointment(appointment_id: str, reason: str = None) -> None:
        """Cancel an appointment."""
        doc = frappe.get_doc("CF Appointment", appointment_id)
        if doc.status in ("Completed", "Cancelled"):
            frappe.throw(_("Cannot cancel a {0} appointment").format(doc.status))
        doc.status = "Cancelled"
        doc.cancellation_reason = reason
        doc.save(ignore_permissions=True)
