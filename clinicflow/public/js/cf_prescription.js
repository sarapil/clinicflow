// Copyright (c) 2026, Arkan Lab — ClinicFlow
frappe.ui.form.on("CF Prescription", {
    refresh(frm) {
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__("Dispense Drugs"), () => {
                frappe.new_doc("CF Drug Dispensing", {
                    prescription: frm.docname,
                    patient: frm.doc.patient,
                });
            });

            frm.add_custom_button(__("Print Prescription"), () => {
                frappe.set_route("print", "CF Prescription", frm.docname);
            }, __("View"));
        }
    },
});

frappe.ui.form.on("CF Prescription Item", {
    drug(frm, cdt, cdn) {
        const row = frappe.get_doc(cdt, cdn);
        if (row.drug) {
            frappe.call({
                method: "medcode.api.v1.drugs.get_drug",
                args: { drug_id: row.drug },
                callback({ message }) {
                    if (message) {
                        frappe.model.set_value(cdt, cdn, "drug_name", message.drug_name);
                        frappe.model.set_value(cdt, cdn, "dosage_form", message.dosage_form);
                    }
                },
            });
        }
    },
});
