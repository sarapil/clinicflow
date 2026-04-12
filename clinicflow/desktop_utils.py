# Copyright (c) 2026, Arkan Lab — ClinicFlow
import frappe


def inject_app_desktop_icon(app, label, route, logo_url, bg_color):
    """Inject ClinicFlow into all Desktop Layouts — idempotent."""
    icon_data = {
        "icon_type": "App",
        "label": label,
        "link": route,
        "link_type": "External",
        "logo_url": logo_url,
        "app": app,
        "background_color": bg_color,
    }
    try:
        layouts = frappe.get_all("Desktop Layout", pluck="name")
        for layout_name in layouts:
            layout = frappe.get_doc("Desktop Layout", layout_name)
            icons = frappe.parse_json(layout.icons or "[]")
            if not any(i.get("label") == label for i in icons):
                icons.append(icon_data)
                layout.icons = frappe.as_json(icons)
                layout.save(ignore_permissions=True)
    except Exception:
        pass
