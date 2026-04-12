# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe
from frappe import _


def seed_data():
    """Idempotent seed data — called on every migrate."""
    _ensure_settings()
    _seed_appointment_templates()
    _seed_service_catalog()
    frappe.db.commit()


def _ensure_settings():
    """Ensure CF Clinical Settings exists — auto-create with defaults if missing."""
    if not frappe.db.exists("CF Clinical Settings", "CF Clinical Settings"):
        frappe.get_doc({
            "doctype": "CF Clinical Settings",
            "clinic_name": frappe.defaults.get_global_default("company") or "My Clinic",
            "default_appointment_duration": 30,
            "enable_ai_features": 0,
        }).insert(ignore_permissions=True)
        frappe.logger().info("CF Clinical Settings created with defaults")


def _seed_appointment_templates():
    templates = [
        {"template_name": "General Consultation", "start_time": "08:00:00", "end_time": "17:00:00", "slot_duration": 30, "max_appointments": 16, "is_active": 1},
        {"template_name": "Follow-up", "start_time": "09:00:00", "end_time": "17:00:00", "slot_duration": 15, "max_appointments": 24, "is_active": 1},
        {"template_name": "New Patient Intake", "start_time": "08:00:00", "end_time": "14:00:00", "slot_duration": 45, "max_appointments": 8, "is_active": 1},
        {"template_name": "Procedure", "start_time": "10:00:00", "end_time": "16:00:00", "slot_duration": 60, "max_appointments": 6, "is_active": 1},
        {"template_name": "Emergency", "start_time": "08:00:00", "end_time": "22:00:00", "slot_duration": 20, "max_appointments": 12, "is_active": 1},
    ]
    for t in templates:
        if not frappe.db.exists("CF Appointment Template", t["template_name"]):
            frappe.get_doc({"doctype": "CF Appointment Template", **t}).insert(ignore_permissions=True)


def _seed_service_catalog():
    services = [
        {"service_code": "CF-CONS-001", "service_name": "General Consultation", "standard_price": 0, "category": "Consultation"},
        {"service_code": "CF-CONS-002", "service_name": "Follow-up Visit", "standard_price": 0, "category": "Consultation"},
        {"service_code": "CF-LAB-001", "service_name": "Blood Test (CBC)", "standard_price": 0, "category": "Lab Test"},
        {"service_code": "CF-RAD-001", "service_name": "X-Ray", "standard_price": 0, "category": "Radiology"},
        {"service_code": "CF-PROC-001", "service_name": "ECG", "standard_price": 0, "category": "Procedure"},
    ]
    for s in services:
        if not frappe.db.exists("CF Service", s["service_code"]):
            frappe.get_doc({"doctype": "CF Service", **s}).insert(ignore_permissions=True)
