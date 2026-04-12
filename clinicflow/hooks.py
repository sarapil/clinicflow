# Copyright (c) 2026, Arkan Lab — ClinicFlow
app_name = "clinicflow"
app_title = "ClinicFlow"
app_publisher = "Arkan Lab"
app_description = "Full-featured clinic management: patients, appointments, consultations, lab, radiology, billing, insurance, pharmacy"
app_email = "dev@arkan.it.com"
app_license = "gpl-3.0"
app_version = "1.0.0"

required_apps = ["frappe", "frappe_visual", "arkan_help", "caps", "medcode"]

add_to_apps_screen = [{
    "name": "clinicflow",
    "logo": "/assets/clinicflow/images/clinicflow-logo.svg",
    "title": "ClinicFlow",
    "route": "/desk#Workspace/Patient Management",
}]

app_include_js = ["/assets/clinicflow/js/clinicflow_boot.js"]
app_include_css = ["/assets/clinicflow/css/clinicflow.css"]

doctype_js = {
    "CF Appointment": "public/js/cf_appointment.js",
    "CF Consultation": "public/js/cf_consultation.js",
    "CF Prescription": "public/js/cf_prescription.js",
    "CF Lab Order": "public/js/cf_lab_order.js",
    "CF Clinic Invoice": "public/js/cf_clinic_invoice.js",
}

after_install = "clinicflow.install.after_install"
after_migrate = ["clinicflow.seed.seed_data"]
before_uninstall = "clinicflow.install.before_uninstall"

scheduler_events = {
    "daily": ["clinicflow.tasks.daily_tasks"],
    "hourly": ["clinicflow.tasks.hourly_tasks"],
}

caps_capabilities = [
    {"name": "CF_manage_patients", "category": "Module", "description": "Manage patient records"},
    {"name": "CF_view_medical_records", "category": "Module", "description": "View full medical history"},
    {"name": "CF_schedule_appointments", "category": "Action", "description": "Create and manage appointments"},
    {"name": "CF_conduct_consultation", "category": "Action", "description": "Write consultation notes"},
    {"name": "CF_prescribe_medications", "category": "Action", "description": "Write prescriptions"},
    {"name": "CF_order_lab_tests", "category": "Action", "description": "Order lab investigations"},
    {"name": "CF_order_radiology", "category": "Action", "description": "Order radiological investigations"},
    {"name": "CF_enter_lab_results", "category": "Action", "description": "Enter lab results"},
    {"name": "CF_manage_billing", "category": "Action", "description": "Create and manage invoices"},
    {"name": "CF_manage_insurance", "category": "Action", "description": "Handle insurance claims"},
    {"name": "CF_dispense_medications", "category": "Action", "description": "Dispense medications"},
    {"name": "CF_view_financial_reports", "category": "Report", "description": "Access financial reports"},
    {"name": "CF_view_clinical_reports", "category": "Report", "description": "Access clinical reports"},
    {"name": "CF_configure_system", "category": "Action", "description": "Configure clinic settings"},
    {"name": "CF_view_cost_data", "category": "Field", "description": "View billing amounts"},
    {"name": "CF_access_ai_features", "category": "Module", "description": "Use AI clinical suggestions"},
]

caps_field_maps = [
    {"capability": "CF_view_cost_data", "doctype": "CF Clinic Invoice", "field": "grand_total", "behavior": "mask"},
]

fixtures = [
    {"dt": "Custom Field", "filters": [["dt", "like", "CF%"]]},
    {"dt": "Desktop Icon", "filters": [["app", "=", "clinicflow"]]},
    {"dt": "Workspace", "filters": [["module", "like", "CF%"]]},
]
