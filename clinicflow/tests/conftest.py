# Copyright (c) 2024, Arkan Lab and contributors
# For license information, please see license.txt

import pytest
import frappe


@pytest.fixture(scope="module")
def site_setup():
    """Ensure test site context is active."""
    frappe.set_user("Administrator")
    yield
    frappe.set_user("Administrator")


@pytest.fixture
def test_patient(site_setup):
    """Create a test patient for use in tests."""
    patient = frappe.get_doc({
        "doctype": "Patient",
        "first_name": "Test",
        "last_name": "Patient",
        "sex": "Male",
    })
    patient.insert(ignore_permissions=True)
    yield patient
    if frappe.db.exists("Patient", patient.name):
        frappe.delete_doc("Patient", patient.name, force=True)
