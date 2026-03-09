// Singapore Statutory Reports — Client-side handlers
// Adds buttons to Payroll Entry and Salary Slip for SG compliance downloads

frappe.ui.form.on("Payroll Entry", {
    refresh(frm) {
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__("CPF Submission File"), function() {
                let month = frm.doc.start_date.split("-")[1];
                let year = frm.doc.start_date.split("-")[0];
                frappe.call({
                    method: "hrms.regional.singapore.statutory.generate_cpf_file",
                    args: { month: month, year: year, company: frm.doc.company },
                    callback(r) {
                        if (r.message) {
                            download_file(r.message.filename, r.message.content);
                            frappe.msgprint(__("{0} records exported", [r.message.records]));
                        }
                    }
                });
            }, __("SG Compliance"));

            frm.add_custom_button(__("GIRO Payment File"), function() {
                let month = frm.doc.start_date.split("-")[1];
                let year = frm.doc.start_date.split("-")[0];
                let d = new frappe.ui.Dialog({
                    title: "Generate GIRO File",
                    fields: [
                        { fieldname: "bank_format", label: "Bank Format", fieldtype: "Select",
                          options: "DBS\nOCBC\nUOB\nGeneric CSV", default: "DBS" }
                    ],
                    primary_action(values) {
                        frappe.call({
                            method: "hrms.regional.singapore.statutory.generate_giro_file",
                            args: { month: month, year: year, company: frm.doc.company, bank_format: values.bank_format },
                            callback(r) {
                                if (r.message) {
                                    download_file(r.message.filename, r.message.content);
                                    frappe.msgprint(__("GIRO file: {0} records, total ${1}", [r.message.records, r.message.total]));
                                }
                            }
                        });
                        d.hide();
                    }
                });
                d.show();
            }, __("SG Compliance"));

            frm.add_custom_button(__("IR8A (Year-End Tax)"), function() {
                let year = frm.doc.start_date.split("-")[0];
                frappe.call({
                    method: "hrms.regional.singapore.statutory.generate_ir8a",
                    args: { year: year, company: frm.doc.company },
                    callback(r) {
                        if (r.message) {
                            download_file(r.message.filename, r.message.content);
                            frappe.msgprint(__("IR8A: {0} employee records for YA{1}", [r.message.records, parseInt(year)+1]));
                        }
                    }
                });
            }, __("SG Compliance"));
        }
    }
});

function download_file(filename, content) {
    let blob = new Blob([content], { type: "text/csv" });
    let url = URL.createObjectURL(blob);
    let a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
}
