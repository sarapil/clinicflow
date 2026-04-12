# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe
from frappe import _
from clinicflow.api.response import success, error, paginated


@frappe.whitelist()
def get_patients(page=1, page_size=20, search=None, status=None):
    """List patients with pagination and search."""
    frappe.has_permission("CF Patient", "read", throw=True)
    filters = {}
    if status:
        filters["status"] = status
    if search:
        filters["patient_name"] = ["like", f"%{search}%"]
    total = frappe.db.count("CF Patient", filters)
    records = frappe.get_all(
        "CF Patient",
        filters=filters,
        fields=["name", "patient_name", "patient_id", "gender", "date_of_birth", "mobile_number", "blood_group"],
        order_by="creation desc",
        start=(int(page) - 1) * int(page_size),
        page_length=int(page_size),
    )
    return paginated(records, total, page, page_size)


@frappe.whitelist()
def get_patient(patient_id):
    """Get full patient details."""
    frappe.has_permission("CF Patient", "read", throw=True)
    if not frappe.db.exists("CF Patient", patient_id):
        return error(_("Patient not found"), "PATIENT_NOT_FOUND", 404)
    doc = frappe.get_doc("CF Patient", patient_id)
    return success(doc.as_dict())
