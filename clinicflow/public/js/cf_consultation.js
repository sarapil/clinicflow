// Copyright (c) 2026, Arkan Lab — ClinicFlow
frappe.ui.form.on("CF Consultation", {
    refresh(frm) {
        // Quick vitals chart at top
        if (frm.doc.vital_signs && frm.doc.vital_signs.length > 1) {
            frm.add_custom_button(__("Vitals Trend"), () => {
                frappe.require("frappe_visual.bundle.js", () => {
                    const data = frm.doc.vital_signs.map(v => ({
                        date: v.recorded_at, bp: v.blood_pressure, pulse: v.pulse_rate
                    }));
                    frappe.visual.sparkline("#vitals-trend", { data, label: __("Pulse & BP") });
                });
            }, __("View"));
        }

        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__("Create Prescription"), () => {
                frappe.new_doc("CF Prescription", {
                    consultation: frm.docname,
                    patient: frm.doc.patient,
                    practitioner: frm.doc.practitioner,
                });
            });

            frm.add_custom_button(__("Generate Invoice"), () => {
                frappe.new_doc("CF Clinic Invoice", {
                    consultation: frm.docname,
                    patient: frm.doc.patient,
                });
            });

            frm.add_custom_button(__("Order Lab Test"), () => {
                frappe.new_doc("CF Lab Order", {
                    consultation: frm.docname,
                    patient: frm.doc.patient,
                    practitioner: frm.doc.practitioner,
                });
            });
        }
    },
});
