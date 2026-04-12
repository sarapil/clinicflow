# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe


def check_user_capability(capability_name: str, throw: bool = True) -> bool:
    """Check if current user has the named CAPS capability."""
    try:
        from caps.services.capability_service import check_capability
        return check_capability(capability_name, frappe.session.user, throw=throw)
    except ImportError:
        # CAPS not installed — fall back to role check
        return frappe.has_permission("CF Clinical Settings", "read", throw=throw)
