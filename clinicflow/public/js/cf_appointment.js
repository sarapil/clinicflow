// Copyright (c) 2026, Arkan Lab — ClinicFlow
frappe.ui.form.on("CF Appointment", {
    refresh(frm) {
        if (frm.doc.status === "Scheduled") {
            frm.add_custom_button(__("Confirm"), () => {
                frappe.call({
                    method: "frappe.client.set_value",
                    args: { doctype: "CF Appointment", name: frm.docname,
                            fieldname: "status", value: "Confirmed" },
                    callback() { frm.reload_doc(); },
                });
            }, __("Actions"));

            frm.add_custom_button(__("Cancel Appointment"), () => {
                frappe.prompt(
                    { label: __("Reason"), fieldname: "reason", fieldtype: "Small Text", reqd: 1 },
                    ({ reason }) => {
                        frappe.call({
                            method: "clinicflow.api.v1.appointments.cancel_appointment",
                            args: { appointment_id: frm.docname, reason },
                            callback() { frm.reload_doc(); },
                        });
                    },
                    __("Cancel Appointment")
                );
            }, __("Actions"));
        }

        if (frm.doc.status === "Confirmed") {
            frm.add_custom_button(__("Start Consultation"), () => {
                frappe.new_doc("CF Consultation", {
                    appointment: frm.docname,
                    patient: frm.doc.patient,
                    practitioner: frm.doc.practitioner,
                });
            });
        }
    },

    appointment_date(frm) {
        if (frm.doc.practitioner && frm.doc.appointment_date) {
            frm.call("get_next_slot").then(() => frm.refresh_field("appointment_time"));
        }
    },
});
