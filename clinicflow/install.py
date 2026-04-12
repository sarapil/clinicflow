# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe
from frappe import _


def after_install():
    """Create default roles, settings, and desktop icons after install."""
    _create_roles()
    _create_cf_settings()
    _inject_desktop_icon()
    frappe.db.commit()
    frappe.clear_cache()


def before_uninstall():
    """Clean up before uninstall."""
    pass


def _create_roles():
    roles = [
        ("CF Admin", "مدير العيادة"),
        ("CF Doctor", "طبيب"),
        ("CF Nurse", "ممرض/ة"),
        ("CF Receptionist", "موظف استقبال"),
        ("CF Lab Technician", "فني مختبر"),
        ("CF Radiologist", "أخصائي أشعة"),
        ("CF Pharmacist", "صيدلي"),
        ("CF Accountant", "محاسب"),
        ("CF Insurance Coordinator", "منسق تأمين"),
        ("CF Patient Portal", "بوابة المريض"),
    ]
    for role_name, role_ar in roles:
        if not frappe.db.exists("Role", role_name):
            doc = frappe.get_doc({"doctype": "Role", "role_name": role_name})
            doc.insert(ignore_permissions=True)


def _create_cf_settings():
    if not frappe.db.exists("CF Clinical Settings", "CF Clinical Settings"):
        doc = frappe.get_doc({
            "doctype": "CF Clinical Settings",
            "clinic_name": frappe.defaults.get_global_default("company") or "My Clinic",
            "default_appointment_duration": 30,
            "enable_ai_features": 0,
        })
        doc.insert(ignore_permissions=True)


def _inject_desktop_icon():
    try:
        from clinicflow.desktop_utils import inject_app_desktop_icon
        inject_app_desktop_icon(
            app="clinicflow",
            label="ClinicFlow",
            route="/desk#Workspace/Patient Management",
            logo_url="/assets/clinicflow/images/clinicflow-logo.svg",
            bg_color="#DC2626",
        )
    except Exception:
        pass
