// Copyright (c) 2026, Arkan Lab
// License: GPL-3.0

// ClinicFlow lightweight bootstrap loaded via hooks.py
window.clinicflow = window.clinicflow || {};

if (typeof frappe === "undefined" || typeof frappe.provide !== "function") {
    window.frappe = window.frappe || {};
    frappe.provide = frappe.provide || function () {};
}

frappe.provide("clinicflow");
frappe.provide("clinicflow.utils");

$(document).on("startup", function () {
    clinicflow.ready = true;
});
