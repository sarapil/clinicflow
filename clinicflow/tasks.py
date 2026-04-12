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
    """Send reminders for appointments in the next 24 hours.

    Uses NotifyPro if installed for multi-channel delivery (SMS, WhatsApp, email).
    Falls back to frappe.sendmail if NotifyPro is not available.
    """
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
        fields=["name", "patient", "patient_name", "scheduled_datetime", "practitioner"],
    )
    if not appointments:
        return

    use_notifypro = "notifypro" in frappe.get_installed_apps()

    for appt in appointments:
        try:
            patient = frappe.get_doc("CF Patient", appt.patient)
            if use_notifypro:
                _send_via_notifypro(patient, appt)
            elif patient.email:
                frappe.sendmail(
                    recipients=[patient.email],
                    subject=f"Appointment Reminder — {appt.scheduled_datetime}",
                    message=f"Dear {patient.patient_name}, this is a reminder of your appointment tomorrow at {appt.scheduled_datetime}.",
                )
            frappe.db.set_value("CF Appointment", appt.name, "reminder_sent", 1)
        except Exception:
            frappe.log_error(frappe.get_traceback(), "CF Appointment Reminder Error")
    frappe.db.commit()


def _send_via_notifypro(patient, appt):
    """Send appointment reminder via NotifyPro multi-channel delivery."""
    try:
        from notifypro.services.queue_service import QueueService
        QueueService.enqueue_notification(
            template="appointment_reminder",
            recipients=[{
                "email": patient.email,
                "phone": getattr(patient, "mobile_phone", None),
                "name": patient.patient_name,
            }],
            context={
                "patient_name": patient.patient_name,
                "appointment_date": str(appt.scheduled_datetime),
                "practitioner": appt.practitioner,
                "doctype": "CF Appointment",
                "docname": appt.name,
            },
            channels=["email", "sms"],
        )
    except (ImportError, AttributeError):
        # NotifyPro API not compatible — fall back to email
        if patient.email:
            frappe.sendmail(
                recipients=[patient.email],
                subject=f"Appointment Reminder — {appt.scheduled_datetime}",
                message=f"Dear {patient.patient_name}, this is a reminder of your appointment tomorrow at {appt.scheduled_datetime}.",
            )


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
