# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe
from frappe import _
from frappe.utils import flt


class BillingService:

    @staticmethod
    def create_invoice_from_consultation(consultation_id: str,
                                         services: list[dict]) -> object:
        """Auto-generate CF Clinic Invoice from consultation."""
        consultation = frappe.get_doc("CF Consultation", consultation_id)
        items = []
        for svc in services:
            service = frappe.get_doc("CF Service", svc["service"])
            items.append({
                "service": service.name,
                "service_name": service.service_name,
                "qty": flt(svc.get("qty", 1)),
                "rate": flt(svc.get("rate", service.price)),
                "amount": flt(svc.get("qty", 1)) * flt(svc.get("rate", service.price)),
            })
        doc = frappe.get_doc({
            "doctype": "CF Clinic Invoice",
            "patient": consultation.patient,
            "consultation": consultation_id,
            "items": items,
        })
        doc.insert(ignore_permissions=True)
        return doc

    @staticmethod
    def calculate_insurance_split(invoice_id: str,
                                  insurance_policy_id: str) -> dict:
        """Calculate patient copay vs insurance-covered amount."""
        invoice = frappe.get_doc("CF Clinic Invoice", invoice_id)
        policy = frappe.get_doc("CF Insurance Policy", insurance_policy_id)
        covered_pct = flt(policy.coverage_percentage or 0) / 100
        total = flt(invoice.grand_total)
        insurance_amount = total * covered_pct
        patient_amount = total - insurance_amount
        return {
            "total": total,
            "insurance_amount": insurance_amount,
            "patient_amount": patient_amount,
            "coverage_percentage": policy.coverage_percentage,
        }
