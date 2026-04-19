import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def setup_ai_resume_fields():
	"""Add custom fields for AI resume parsing, matching, and compliance."""
	custom_fields = {
		"Job Applicant": [
			{
				"fieldname": "ai_section",
				"fieldtype": "Section Break",
				"label": "AI & Skills",
				"insert_after": "resume_link",
			},
			{
				"fieldname": "skills",
				"fieldtype": "Table MultiSelect",
				"label": "Skills",
				"options": "Job Applicant Skill",
				"insert_after": "ai_section",
				"description": "Skills extracted from resume or added manually",
			},
			{
				"fieldname": "experience_summary",
				"fieldtype": "Small Text",
				"label": "Experience Summary",
				"insert_after": "skills",
				"description": "AI-generated summary of candidate experience",
			},
			{
				"fieldname": "ai_match_score",
				"fieldtype": "Percent",
				"label": "AI Match Score",
				"insert_after": "experience_summary",
				"read_only": 1,
				"description": "Relevance score against the linked Job Opening",
			},
			{
				"fieldname": "ai_parsed",
				"fieldtype": "Check",
				"label": "AI Parsed",
				"insert_after": "ai_match_score",
				"read_only": 1,
				"hidden": 1,
				"description": "Whether resume has been processed by AI",
			},
			{
				"fieldname": "compliance_section",
				"fieldtype": "Section Break",
				"label": "Compliance",
				"insert_after": "ai_parsed",
			},
			{
				"fieldname": "consent_given",
				"fieldtype": "Check",
				"label": "Consent Given",
				"insert_after": "compliance_section",
				"description": "Candidate consented to data processing and AI analysis",
			},
			{
				"fieldname": "data_retention_date",
				"fieldtype": "Date",
				"label": "Data Retention Date",
				"insert_after": "consent_given",
				"description": "Date after which this record should be reviewed for deletion",
			},
		],
	}
	create_custom_fields(custom_fields)
	frappe.db.commit()
	print("AI resume fields created successfully.")
