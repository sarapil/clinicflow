# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe


def daily_tasks():
    """Run daily maintenance tasks."""
    _mark_no_shows()
    _send_appointment_reminders()
    _expire_old_wait_list()


def hourly_tasks():
    """Run hourly tasks."""
    _process_pending_lab_results()


def _mark_no_shows():
    """Mark appointments as No-Show if past their time and still Confirmed."""
    from frappe.utils import now_datetime, add_to_date
    cutoff = add_to_date(now_datetime(), hours=-2)
    appointments = frappe.get_all(
        "CF Appointment",
        filters={"status": "Confirmed", "scheduled_datetime": ["<", cutoff]},
        pluck="name",
    )
    for appt in appointments:
        frappe.db.set_value("CF Appointment", appt, "status", "No Show")
    if appointments:
        frappe.db.commit()


def _send_appointment_reminders():
    """Send reminders for appointments in the next 24 hours."""
    from frappe.utils import now_datetime, add_to_date
    now = now_datetime()
    tomorrow = add_to_date(now, hours=24)
    appointments = frappe.get_all(
        "CF Appointment",
        filters={
            "status": "Confirmed",
            "scheduled_datetime": ["between", [now, tomorrow]],
            "reminder_sent": 0,
        },
        fields=["name", "patient", "scheduled_datetime", "practitioner"],
    )
    for appt in appointments:
        try:
            patient = frappe.get_doc("CF Patient", appt.patient)
            if patient.email:
                frappe.sendmail(
                    recipients=[patient.email],
                    subject=f"Appointment Reminder — {appt.scheduled_datetime}",
                    message=f"Dear {patient.patient_name}, this is a reminder of your appointment tomorrow at {appt.scheduled_datetime}.",
                )
            frappe.db.set_value("CF Appointment", appt.name, "reminder_sent", 1)
        except Exception:
            frappe.log_error(frappe.get_traceback(), "CF Appointment Reminder Error")
    if appointments:
        frappe.db.commit()


def _expire_old_wait_list():
    """Remove expired entries from waitlist."""
    from frappe.utils import add_to_date, now_datetime
    cutoff = add_to_date(now_datetime(), days=-7)
    frappe.db.delete("CF Wait List", {"creation": ["<", cutoff], "status": "Waiting"})
    frappe.db.commit()


def _process_pending_lab_results():
    """Notify doctors of newly verified lab results."""
    results = frappe.get_all(
        "CF Lab Result",
        filters={"status": "Verified", "doctor_notified": 0},
        fields=["name", "lab_order", "patient"],
        limit=50,
    )
    for r in results:
        frappe.db.set_value("CF Lab Result", r.name, "doctor_notified", 1)
    if results:
        frappe.db.commit()
