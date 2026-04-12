# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe
from frappe import _
from frappe.utils import random_string


class PatientService:

    @staticmethod
    def generate_patient_id() -> str:
        """Generate unique patient ID: CF-YYYY-NNNNN."""
        from frappe.utils import getdate
        year = getdate().year
        last = frappe.db.sql(
            "SELECT MAX(CAST(SUBSTRING_INDEX(patient_id, '-', -1) AS UNSIGNED)) "
            "FROM `tabCF Patient` WHERE patient_id LIKE %(prefix)s",
            {"prefix": f"CF-{year}-%"},
        )
        seq = (last[0][0] or 0) + 1
        return f"CF-{year}-{seq:05d}"

    @staticmethod
    def get_patient_summary(patient_id: str) -> dict:
        """Return complete patient summary for dashboard."""
        frappe.has_permission("CF Patient", "read", throw=True)
        patient = frappe.get_doc("CF Patient", patient_id)
        last_visit = frappe.get_all(
            "CF Consultation",
            filters={"patient": patient_id, "docstatus": 1},
            fields=["consultation_date", "practitioner", "diagnosis_summary"],
            order_by="consultation_date desc",
            limit=1,
        )
        upcoming = frappe.get_all(
            "CF Appointment",
            filters={"patient": patient_id, "status": ["in", ["Scheduled", "Confirmed"]]},
            fields=["appointment_date", "appointment_time", "practitioner", "appointment_type"],
            order_by="appointment_date asc",
            limit=3,
        )
        outstanding = frappe.db.sql(
            "SELECT SUM(outstanding_amount) FROM `tabCF Clinic Invoice` "
            "WHERE patient = %(patient)s AND docstatus = 1",
            {"patient": patient_id},
        )
        return {
            "patient": patient.as_dict(),
            "last_visit": last_visit[0] if last_visit else None,
            "upcoming_appointments": upcoming,
            "outstanding_balance": float(outstanding[0][0] or 0),
        }
