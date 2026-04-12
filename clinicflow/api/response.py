# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe


def success(data=None, message=None):
    return {"status": "success", "data": data, "message": message}


def error(message, error_code="UNKNOWN_ERROR", http_status=400):
    frappe.local.response.http_status_code = http_status
    return {"status": "error", "error_code": error_code, "message": message}


def paginated(data, total, page=1, page_size=20):
    return {
        "status": "success",
        "data": data,
        "meta": {
            "total": total,
            "page": int(page),
            "page_size": int(page_size),
            "total_pages": -(-int(total) // int(page_size)),
        },
    }
