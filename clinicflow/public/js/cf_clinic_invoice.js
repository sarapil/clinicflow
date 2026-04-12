// Copyright (c) 2026, Arkan Lab — ClinicFlow
frappe.ui.form.on("CF Clinic Invoice", {
    refresh(frm) {
        if (frm.doc.docstatus === 1 && frm.doc.outstanding_amount > 0) {
            frm.add_custom_button(__("Record Payment"), () => {
                frappe.new_doc("CF Clinic Payment", {
                    invoice: frm.docname,
                    patient: frm.doc.patient,
                    amount: frm.doc.outstanding_amount,
                });
            }, __("Actions"));

            frm.add_custom_button(__("File Insurance Claim"), () => {
                frappe.new_doc("CF Insurance Claim", {
                    invoice: frm.docname,
                    patient: frm.doc.patient,
                });
            }, __("Actions"));
        }

        if (frm.doc.outstanding_amount === 0 && frm.doc.docstatus === 1) {
            frm.page.set_indicator(__("Paid"), "green");
        } else if (frm.doc.docstatus === 1) {
            frm.page.set_indicator(__("Outstanding"), "orange");
        }
    },
});
