// Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Job Opening", {
	onload: function (frm) {
		frm.set_query("department", function () {
			return {
				filters: {
					company: frm.doc.company,
				},
			};
		});
	},
	designation: function (frm) {
		if (frm.doc.designation && frm.doc.company) {
			frappe.call({
				method: "hrms.hr.doctype.staffing_plan.staffing_plan.get_active_staffing_plan_details",
				args: {
					company: frm.doc.company,
					designation: frm.doc.designation,
					date: frappe.datetime.now_date(), // ToDo - Date in Job Opening?
				},
				callback: function (data) {
					if (data.message) {
						frm.set_value("staffing_plan", data.message[0].name);
						frm.set_value("planned_vacancies", data.message[0].vacancies);
					} else {
						frm.set_value("staffing_plan", "");
						frm.set_value("planned_vacancies", 0);
						frappe.show_alert({
							indicator: "orange",
							message: __("No Staffing Plans found for this Designation"),
						});
					}
				},
			});
		} else {
			frm.set_value("staffing_plan", "");
			frm.set_value("planned_vacancies", 0);
		}
	},
	company: function (frm) {
		frm.set_value("designation", "");
	},
});

// --- AI Resume Matching ---
frappe.ui.form.on("Job Opening", {
	refresh: function(frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__("Find Matching Resumes"), function() {
				show_resume_matcher(frm);
			}, __("AI"));

			frm.add_custom_button(__("View All Applicants"), function() {
				show_all_applicants(frm);
			}, __("AI"));
		}
	}
});

function show_resume_matcher(frm) {
	let d = new frappe.ui.Dialog({
		title: __("AI Resume Matching — " + frm.doc.job_title),
		size: "extra-large",
		fields: [
			{fieldtype: "HTML", fieldname: "filters_html"},
			{fieldtype: "HTML", fieldname: "results_html"},
		],
	});

	let filters_html = `
		<div class="row mb-3">
			<div class="col-4"><input class="form-control" id="rm-keyword" placeholder="Search skills, keywords..."></div>
			<div class="col-3"><select class="form-control" id="rm-status">
				<option value="">All Statuses</option>
				<option value="Open">Open</option><option value="Replied">Replied</option>
				<option value="Accepted">Accepted</option><option value="Rejected">Rejected</option><option value="Hold">Hold</option>
			</select></div>
			<div class="col-3"><button class="btn btn-primary btn-sm" id="rm-search">🔍 AI Rank</button>
			<button class="btn btn-default btn-sm ml-1" id="rm-all">All</button></div>
		</div>`;
	d.fields_dict.filters_html.$wrapper.html(filters_html);
	d.fields_dict.results_html.$wrapper.html('<p class="text-muted">Click "AI Rank" to score applicants or "All" to view all.</p>');

	d.$wrapper.find("#rm-search").on("click", function() {
		let filters = JSON.stringify({
			skills_keyword: d.$wrapper.find("#rm-keyword").val(),
			status: d.$wrapper.find("#rm-status").val(),
		});
		d.fields_dict.results_html.$wrapper.html('<p class="text-muted">⏳ Scoring resumes with AI...</p>');
		frappe.call({
			method: "hrms.hr.ai_resume_matching.get_matching_resumes",
			args: {job_opening: frm.doc.name, filters: filters},
			callback: function(r) { render_results(d, r.message); }
		});
	});

	d.$wrapper.find("#rm-all").on("click", function() {
		let filters = JSON.stringify({
			skills_keyword: d.$wrapper.find("#rm-keyword").val(),
			status: d.$wrapper.find("#rm-status").val(),
		});
		d.fields_dict.results_html.$wrapper.html('<p class="text-muted">Loading...</p>');
		frappe.call({
			method: "hrms.hr.ai_resume_matching.get_all_applicants",
			args: {job_opening: frm.doc.name, filters: filters},
			callback: function(r) { render_results(d, r.message); }
		});
	});

	d.show();
}

function show_all_applicants(frm) {
	frappe.set_route("List", "Job Applicant", {job_title: frm.doc.name});
}

function render_results(dialog, data) {
	if (!data || !data.applicants || data.applicants.length === 0) {
		dialog.fields_dict.results_html.$wrapper.html('<p class="text-muted">No applicants found.</p>');
		return;
	}
	let html = `<p class="text-muted mb-2">${data.total} applicant(s) found</p>
		<table class="table table-bordered table-sm"><thead><tr>
		<th>Score</th><th>Name</th><th>Email</th><th>Skills</th><th>Status</th><th>Resume</th>
		</tr></thead><tbody>`;
	data.applicants.forEach(function(a) {
		let score = a.ai_match_score ? `<span class="badge" style="background:${a.ai_match_score>=70?'#28a745':a.ai_match_score>=40?'#ffc107':'#dc3545'};color:#fff">${Math.round(a.ai_match_score)}%</span>` : '-';
		let skills = (a.skills || []).slice(0, 5).join(", ");
		if ((a.skills || []).length > 5) skills += "...";
		let resume = a.resume_attachment ? `<a href="${a.resume_attachment}" target="_blank">📄</a>` : '-';
		html += `<tr>
			<td>${score}</td>
			<td><a href="/app/job-applicant/${encodeURIComponent(a.name)}" target="_blank">${a.applicant_name || a.name}</a></td>
			<td>${a.email_id || '-'}</td>
			<td><small>${skills || '-'}</small></td>
			<td>${a.status || '-'}</td>
			<td>${resume}</td>
		</tr>`;
	});
	html += "</tbody></table>";
	dialog.fields_dict.results_html.$wrapper.html(html);
}
