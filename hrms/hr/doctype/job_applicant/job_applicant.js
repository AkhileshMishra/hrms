// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

// For license information, please see license.txt

// for communication
cur_frm.email_field = "email_id";

frappe.ui.form.on("Job Applicant", {
	refresh: function (frm) {
		frm.set_query("job_title", function () {
			return {
				filters: {
					status: "Open",
				},
			};
		});
		frm.events.create_custom_buttons(frm);
		frm.events.make_dashboard(frm);
	},

	create_custom_buttons: function (frm) {
		if (!frm.doc.__islocal && frm.doc.status !== "Rejected" && frm.doc.status !== "Accepted") {
			frm.add_custom_button(
				__("Interview"),
				function () {
					frm.events.create_dialog(frm);
				},
				__("Create"),
			);
		}

		if (!frm.doc.__islocal && frm.doc.status == "Accepted") {
			if (frm.doc.__onload && frm.doc.__onload.job_offer) {
				$('[data-doctype="Employee Onboarding"]').find("button").show();
				$('[data-doctype="Job Offer"]').find("button").hide();
				frm.add_custom_button(
					__("Job Offer"),
					function () {
						frappe.set_route("Form", "Job Offer", frm.doc.__onload.job_offer);
					},
					__("View"),
				);
			} else {
				$('[data-doctype="Employee Onboarding"]').find("button").hide();
				$('[data-doctype="Job Offer"]').find("button").show();
				frm.add_custom_button(
					__("Job Offer"),
					function () {
						frappe.route_options = {
							job_applicant: frm.doc.name,
							applicant_name: frm.doc.applicant_name,
							designation: frm.doc.job_opening || frm.doc.designation,
						};
						frappe.new_doc("Job Offer");
					},
					__("Create"),
				);
			}
		}
	},

	make_dashboard: function (frm) {
		frappe.call({
			method: "hrms.hr.doctype.job_applicant.job_applicant.get_interview_details",
			args: {
				job_applicant: frm.doc.name,
			},
			callback: function (r) {
				if (r.message) {
					$("div").remove(".form-dashboard-section.custom");
					frm.dashboard.add_section(
						frappe.render_template("job_applicant_dashboard", {
							data: r.message.interviews,
							number_of_stars: r.message.stars,
						}),
						__("Interview Summary"),
					);
				}
			},
		});
	},

	create_dialog: function (frm) {
		let d = new frappe.ui.Dialog({
			title: "Enter Interview Round",
			fields: [
				{
					label: "Interview Round",
					fieldname: "interview_round",
					fieldtype: "Link",
					options: "Interview Round",
				},
			],
			primary_action_label: __("Create Interview"),
			primary_action(values) {
				frm.events.create_interview(frm, values);
				d.hide();
			},
		});
		d.show();
	},

	create_interview: function (frm, values) {
		frappe.call({
			method: "hrms.hr.doctype.job_applicant.job_applicant.create_interview",
			args: {
				doc: frm.doc,
				interview_round: values.interview_round,
			},
			callback: function (r) {
				var doclist = frappe.model.sync(r.message);
				frappe.set_route("Form", doclist[0].doctype, doclist[0].name);
			},
		});
	},
});

// --- AI Resume Upload with Progress ---
frappe.ui.form.on("Job Applicant", {
	resume_attachment: function(frm) {
		if (!frm.doc.resume_attachment) return;

		let d = new frappe.ui.Dialog({
			title: __("🤖 AI Processing Resume"),
			indicator: "blue",
			fields: [{fieldtype: "HTML", fieldname: "progress_html"}],
			no_cancel_flag: true,
		});

		let steps = [
			"Uploading resume...",
			"Extracting text from document...",
			"Analyzing with AI...",
			"Extracting skills and experience...",
			"Populating fields..."
		];

		function update_progress(step, pct) {
			d.fields_dict.progress_html.$wrapper.html(`
				<div style="padding: 10px 0;">
					<div class="progress" style="height: 20px; border-radius: 10px;">
						<div class="progress-bar" role="progressbar"
							style="width: ${pct}%; background: linear-gradient(135deg, #003D6B, #0066B3); transition: width 0.5s;"
							aria-valuenow="${pct}" aria-valuemin="0" aria-valuemax="100">${pct}%</div>
					</div>
					<p class="text-muted mt-2" style="font-size: 13px;">✨ ${steps[step]}</p>
				</div>
			`);
		}

		d.show();
		update_progress(0, 10);

		// Animate progress while waiting
		let fake_step = 0;
		let interval = setInterval(() => {
			if (fake_step < 3) {
				fake_step++;
				update_progress(fake_step, 10 + fake_step * 20);
			}
		}, 1500);

		frappe.call({
			method: "hrms.hr.ai_resume_parser.parse_resume_on_upload",
			args: { file_url: frm.doc.resume_attachment },
			callback: function(r) {
				clearInterval(interval);
				if (r.message && r.message.success) {
					update_progress(4, 100);
					let data = r.message.data;

					// Auto-fill fields only if empty
					if (data.name && !frm.doc.applicant_name) frm.set_value("applicant_name", data.name);
					if (data.email && !frm.doc.email_id) frm.set_value("email_id", data.email);
					if (data.phone && !frm.doc.phone_number) frm.set_value("phone_number", data.phone);
					if (data.experience_summary) frm.set_value("experience_summary", data.experience_summary);

					// Add skills
					if (data.skills && data.skills.length) {
						frm.clear_table("skills");
						data.skills.forEach(function(skill) {
							let row = frm.add_child("skills");
							row.skill = skill;
						});
						frm.refresh_field("skills");
					}

					setTimeout(() => {
						d.hide();
						frappe.show_alert({
							message: __(`✅ AI extracted ${data.skills ? data.skills.length : 0} skills. Review and click Save.`),
							indicator: "green"
						}, 7);
					}, 800);
				} else {
					clearInterval(interval);
					d.hide();
					let err = (r.message && r.message.error) || "Unknown error";
					frappe.msgprint({title: __("Resume Processing"), message: err, indicator: "orange"});
				}
			},
			error: function() {
				clearInterval(interval);
				d.hide();
				frappe.msgprint({title: __("Error"), message: __("Failed to process resume. Please fill in details manually."), indicator: "red"});
			}
		});
	}
});
