# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe
from frappe import _


class ConsultationService:

    @staticmethod
    def create_consultation(appointment: str, chief_complaint: str,
                            examination: str = None, diagnosis_summary: str = None,
                            plan: str = None) -> object:
        """Create a clinical consultation from an appointment."""
        appt = frappe.get_doc("CF Appointment", appointment)
        if appt.status == "Cancelled":
            frappe.throw(_("Cannot create consultation for cancelled appointment"))

        doc = frappe.get_doc({
            "doctype": "CF Consultation",
            "appointment": appointment,
            "patient": appt.patient,
            "patient_name": appt.patient_name,
            "practitioner": appt.practitioner,
            "consultation_date": appt.appointment_date,
            "chief_complaint": chief_complaint,
            "examination_findings": examination,
            "diagnosis_summary": diagnosis_summary,
            "management_plan": plan,
        })
        doc.insert(ignore_permissions=True)
        frappe.db.set_value("CF Appointment", appointment, "status", "Completed")
        return doc

    @staticmethod
    def validate_consultation(doc) -> None:
        """Validate consultation before save."""
        if not doc.chief_complaint:
            frappe.throw(_("Chief complaint is required"))
        if doc.docstatus == 1 and not doc.diagnosis_summary:
            frappe.throw(_("Diagnosis summary required before submitting"))
