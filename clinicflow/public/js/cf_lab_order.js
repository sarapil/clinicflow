// Copyright (c) 2026, Arkan Lab — ClinicFlow
frappe.ui.form.on("CF Lab Order", {
    refresh(frm) {
        // Status indicator color
        const colors = {
            Pending: "orange", "In Progress": "blue", Completed: "green",
            Cancelled: "red", "Partially Completed": "yellow",
        };
        frm.page.set_indicator(__(frm.doc.status), colors[frm.doc.status] || "grey");

        if (frm.doc.docstatus === 1 && frm.doc.status !== "Completed") {
            frm.add_custom_button(__("Enter Results"), () => {
                frappe.new_doc("CF Lab Result", {
                    lab_order: frm.docname,
                    patient: frm.doc.patient,
                });
            });
        }

        if (frm.doc.status === "Completed") {
            frm.add_custom_button(__("View Results"), () => {
                frappe.set_route("List", "CF Lab Result", {
                    lab_order: frm.docname,
                });
            }, __("View"));
        }
    },
});
