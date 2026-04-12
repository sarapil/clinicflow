# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe
from frappe import _
from clinicflow.api.response import success, error, paginated


@frappe.whitelist()
def get_patient_consultations(patient, page=1, page_size=10):
    """Get consultation history for a patient."""
    frappe.has_permission("CF Consultation", "read", throw=True)
    total = frappe.db.count("CF Consultation", {"patient": patient})
    records = frappe.get_all(
        "CF Consultation",
        filters={"patient": patient},
        fields=["name", "appointment", "practitioner", "consultation_date",
                "chief_complaint", "diagnosis_summary", "docstatus"],
        order_by="consultation_date desc",
        start=(int(page) - 1) * int(page_size),
        page_length=int(page_size),
    )
    return paginated(records, total, page, page_size)


@frappe.whitelist()
def get_consultation(consultation_id):
    """Get full consultation details."""
    frappe.has_permission("CF Consultation", "read", throw=True)
    if not frappe.db.exists("CF Consultation", consultation_id):
        return error(_("Consultation not found"), "NOT_FOUND", 404)
    doc = frappe.get_doc("CF Consultation", consultation_id)
    return success(doc.as_dict())


@frappe.whitelist()
def get_patient_vitals(patient, limit=10):
    """Get latest vital signs readings for a patient."""
    frappe.has_permission("CF Vital Signs", "read", throw=True)
    records = frappe.db.sql("""
        SELECT vs.name, vs.consultation, vs.temperature, vs.blood_pressure_systolic,
               vs.blood_pressure_diastolic, vs.pulse_rate, vs.spo2, vs.weight, vs.height,
               vs.bmi, vs.recorded_at
        FROM `tabCF Vital Signs` vs
        WHERE vs.patient = %(patient)s
        ORDER BY vs.recorded_at DESC
        LIMIT %(limit)s
    """, {"patient": patient, "limit": int(limit)}, as_dict=True)
    return success(records)
