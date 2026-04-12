# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe
from frappe import _
from frappe.utils import getdate, get_time
from clinicflow.api.response import success, error, paginated


@frappe.whitelist()
def get_appointments(date=None, practitioner=None, status=None, page=1, page_size=20):
    """List appointments with filters."""
    frappe.has_permission("CF Appointment", "read", throw=True)
    filters = {}
    if date:
        filters["appointment_date"] = date
    if practitioner:
        filters["practitioner"] = practitioner
    if status:
        filters["status"] = status
    total = frappe.db.count("CF Appointment", filters)
    records = frappe.get_all(
        "CF Appointment",
        filters=filters,
        fields=["name", "patient", "patient_name", "practitioner", "appointment_date",
                "appointment_time", "status", "appointment_type"],
        order_by="appointment_date asc, appointment_time asc",
        start=(int(page) - 1) * int(page_size),
        page_length=int(page_size),
    )
    return paginated(records, total, page, page_size)


@frappe.whitelist()
def get_available_slots(practitioner, date):
    """Get available appointment slots for a practitioner on a given date."""
    frappe.has_permission("CF Appointment", "read", throw=True)
    from clinicflow.services.appointment_service import AppointmentService
    slots = AppointmentService.get_available_slots(practitioner, date)
    return success(slots)


@frappe.whitelist()
def book_appointment(patient, practitioner, appointment_date, appointment_time,
                     appointment_type=None, notes=None):
    frappe.only_for(["CF User", "CF Manager", "System Manager"])
    """Public-facing appointment booking API."""
    from clinicflow.services.appointment_service import AppointmentService
    try:
        appt = AppointmentService.book_appointment(
            patient=patient,
            practitioner=practitioner,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            appointment_type=appointment_type,
            notes=notes,
        )
        return success({"appointment_id": appt.name}, _("Appointment booked successfully"))
    except Exception as e:
        return error(str(e))
