"""
AI Resume Matching for HRDL8
Scores Job Applicants against a Job Opening using Bedrock Sonnet 4.6.
Provides ranked results with filters for HR.
"""
import json

import frappe
from frappe import _

from hrms.hr.ai_resume_parser import get_bedrock_config, get_resume_text


@frappe.whitelist()
def get_matching_resumes(job_opening, filters=None):
	"""
	Score all applicants for a Job Opening and return ranked results.
	Called from Job Opening form via button click.

	Args:
		job_opening: Name of the Job Opening
		filters: Optional JSON string with filter criteria
	"""
	if not frappe.has_permission("Job Opening", "read", job_opening):
		frappe.throw(_("Insufficient permissions"), frappe.PermissionError)

	jo = frappe.get_doc("Job Opening", job_opening)
	job_description = f"Title: {jo.job_title}\nDesignation: {jo.designation}\nDescription: {jo.description or ''}"

	# Build applicant query with filters
	query_filters = {"job_title": job_opening}
	parsed_filters = json.loads(filters) if filters else {}

	if parsed_filters.get("status"):
		query_filters["status"] = parsed_filters["status"]

	applicants = frappe.get_all(
		"Job Applicant",
		filters=query_filters,
		fields=[
			"name", "applicant_name", "email_id", "phone_number", "status",
			"country", "resume_attachment", "experience_summary",
			"ai_match_score", "applicant_rating",
		],
		order_by="modified desc",
		limit_page_length=0,
	)

	if not applicants:
		return {"applicants": [], "total": 0}

	# Get skills for each applicant
	for app in applicants:
		skills = frappe.get_all(
			"Job Applicant Skill",
			filters={"parent": app.name, "parenttype": "Job Applicant"},
			fields=["skill"],
		)
		app["skills"] = [s.skill for s in skills]

	# Apply client-side filters
	if parsed_filters.get("skills_keyword"):
		keyword = parsed_filters["skills_keyword"].lower()
		applicants = [
			a for a in applicants
			if keyword in " ".join(a.get("skills", [])).lower()
			or keyword in (a.get("experience_summary") or "").lower()
			or keyword in (a.get("applicant_name") or "").lower()
		]

	# AI scoring — only for applicants with resumes
	applicants_to_score = [a for a in applicants if a.get("resume_attachment") and not a.get("ai_match_score")]
	if applicants_to_score:
		score_applicants(job_description, applicants_to_score)

	# Re-fetch scores after update
	for app in applicants:
		app["ai_match_score"] = frappe.db.get_value("Job Applicant", app.name, "ai_match_score") or 0

	# Sort by AI match score descending
	applicants.sort(key=lambda x: x.get("ai_match_score", 0), reverse=True)

	return {"applicants": applicants, "total": len(applicants)}


def score_applicants(job_description, applicants):
	"""Score a batch of applicants against a job description using Bedrock."""
	try:
		import boto3
	except ImportError:
		frappe.log_error("boto3 not installed", "AI Resume Matching")
		return

	config = get_bedrock_config()
	client = boto3.client("bedrock-runtime", region_name=config["region"])

	for app in applicants:
		try:
			resume_summary = app.get("experience_summary") or ""
			skills = ", ".join(app.get("skills", []))
			candidate_profile = f"Name: {app.applicant_name}\nSkills: {skills}\nExperience: {resume_summary}"

			prompt = f"""Score this candidate's fit for the job on a scale of 0-100.
Return ONLY a JSON object: {{"score": <number>, "reason": "<one sentence>"}}

Job:
{job_description[:3000]}

Candidate:
{candidate_profile[:3000]}"""

			body = json.dumps({
				"anthropic_version": "bedrock-2023-05-31",
				"max_tokens": 256,
				"messages": [{"role": "user", "content": prompt}],
			})

			response = client.invoke_model(modelId=config["model_id"], body=body)
			result = json.loads(response["body"].read())
			content = result["content"][0]["text"]

			# Parse score
			if "```json" in content:
				content = content.split("```json")[1].split("```")[0]
			elif "```" in content:
				content = content.split("```")[1].split("```")[0]

			parsed = json.loads(content.strip())
			score = min(100, max(0, float(parsed.get("score", 0))))

			frappe.db.set_value("Job Applicant", app.name, "ai_match_score", score, update_modified=False)

		except Exception as e:
			frappe.log_error(f"Scoring failed for {app.name}: {e}", "AI Resume Matching")

	frappe.db.commit()


@frappe.whitelist()
def get_all_applicants(job_opening, filters=None):
	"""Get all applicants for a Job Opening without AI scoring (fast)."""
	if not frappe.has_permission("Job Opening", "read", job_opening):
		frappe.throw(_("Insufficient permissions"), frappe.PermissionError)

	query_filters = {"job_title": job_opening}
	parsed_filters = json.loads(filters) if filters else {}

	if parsed_filters.get("status"):
		query_filters["status"] = parsed_filters["status"]

	applicants = frappe.get_all(
		"Job Applicant",
		filters=query_filters,
		fields=[
			"name", "applicant_name", "email_id", "phone_number", "status",
			"country", "resume_attachment", "experience_summary",
			"ai_match_score", "applicant_rating",
		],
		order_by="modified desc",
		limit_page_length=0,
	)

	for app in applicants:
		skills = frappe.get_all(
			"Job Applicant Skill",
			filters={"parent": app.name, "parenttype": "Job Applicant"},
			fields=["skill"],
		)
		app["skills"] = [s.skill for s in skills]

	# Apply keyword filter
	if parsed_filters.get("skills_keyword"):
		keyword = parsed_filters["skills_keyword"].lower()
		applicants = [
			a for a in applicants
			if keyword in " ".join(a.get("skills", [])).lower()
			or keyword in (a.get("experience_summary") or "").lower()
			or keyword in (a.get("applicant_name") or "").lower()
		]

	return {"applicants": applicants, "total": len(applicants)}
