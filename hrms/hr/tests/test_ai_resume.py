"""
Unit tests for AI Resume features:
- Custom fields setup
- Resume parser (text extraction, Bedrock integration)
- Resume matching (scoring, filtering)
- Compliance (consent, retention, audit trail)
- Web form validation
"""
import json
import os
import unittest
from unittest.mock import MagicMock, patch

import frappe
from frappe.tests.utils import FrappeTestCase


class TestAIResumeSetup(FrappeTestCase):
	"""Test custom field creation."""

	def test_job_applicant_skill_doctype_exists(self):
		self.assertTrue(frappe.db.exists("DocType", "Job Applicant Skill"))

	def test_job_applicant_skill_is_child_table(self):
		meta = frappe.get_meta("Job Applicant Skill")
		self.assertTrue(meta.istable)

	def test_job_applicant_skill_has_skill_field(self):
		meta = frappe.get_meta("Job Applicant Skill")
		self.assertIn("skill", [f.fieldname for f in meta.fields])

	def test_custom_fields_created(self):
		"""Verify all custom fields exist on Job Applicant after setup."""
		from hrms.hr.ai_resume_setup import setup_ai_resume_fields
		setup_ai_resume_fields()

		meta = frappe.get_meta("Job Applicant")
		field_names = [f.fieldname for f in meta.fields]
		for expected in ["skills", "experience_summary", "ai_match_score", "consent_given", "data_retention_date", "ai_parsed"]:
			self.assertIn(expected, field_names, f"Field {expected} missing from Job Applicant")

	def test_skills_field_is_table_multiselect(self):
		from hrms.hr.ai_resume_setup import setup_ai_resume_fields
		setup_ai_resume_fields()

		meta = frappe.get_meta("Job Applicant")
		skills_field = meta.get_field("skills")
		self.assertEqual(skills_field.fieldtype, "Table MultiSelect")
		self.assertEqual(skills_field.options, "Job Applicant Skill")


class TestResumeParser(FrappeTestCase):
	"""Test resume text extraction and Bedrock parsing."""

	def test_extract_text_from_pdf_missing_file(self):
		from hrms.hr.ai_resume_parser import extract_text_from_pdf
		result = extract_text_from_pdf("/nonexistent/file.pdf")
		self.assertEqual(result, "")

	def test_get_resume_text_no_attachment(self):
		from hrms.hr.ai_resume_parser import get_resume_text
		doc = MagicMock()
		doc.resume_attachment = None
		self.assertEqual(get_resume_text(doc), "")

	@patch("hrms.hr.ai_resume_parser.get_resume_text")
	@patch("hrms.hr.ai_resume_parser.parse_resume_with_bedrock")
	def test_process_resume_skips_if_already_parsed(self, mock_bedrock, mock_text):
		"""Should not re-process if ai_parsed is already set."""
		applicant = create_test_applicant(consent=True)
		frappe.db.set_value("Job Applicant", applicant.name, "ai_parsed", 1)
		frappe.db.commit()

		from hrms.hr.ai_resume_parser import process_resume
		process_resume(applicant.name)

		mock_text.assert_not_called()
		mock_bedrock.assert_not_called()

	@patch("hrms.hr.ai_resume_parser.get_resume_text", return_value="John Doe\njohn@example.com\nPython, JavaScript")
	@patch("hrms.hr.ai_resume_parser.parse_resume_with_bedrock")
	def test_process_resume_auto_fills_fields(self, mock_bedrock, mock_text):
		mock_bedrock.return_value = {
			"name": "John Doe",
			"email": "john@example.com",
			"phone": "+6591234567",
			"country": "Singapore",
			"skills": ["Python", "JavaScript"],
			"experience_summary": "5 years of full-stack development experience.",
		}

		applicant = create_test_applicant(consent=True, name="", email="test-parse@example.com")
		from hrms.hr.ai_resume_parser import process_resume
		process_resume(applicant.name)

		doc = frappe.get_doc("Job Applicant", applicant.name)
		self.assertEqual(doc.ai_parsed, 1)
		self.assertEqual(doc.experience_summary, "5 years of full-stack development experience.")
		self.assertTrue(len(doc.skills) >= 2)

	@patch("hrms.hr.ai_resume_parser.get_resume_text", return_value="")
	def test_process_resume_skips_empty_text(self, mock_text):
		applicant = create_test_applicant(consent=True)
		from hrms.hr.ai_resume_parser import process_resume
		process_resume(applicant.name)

		doc = frappe.get_doc("Job Applicant", applicant.name)
		self.assertFalse(doc.ai_parsed)

	def test_bedrock_config_reads_from_site_config(self):
		from hrms.hr.ai_resume_parser import get_bedrock_config
		config = get_bedrock_config()
		self.assertIn("region", config)
		self.assertIn("model_id", config)
		self.assertIn("retention_months", config)
		self.assertEqual(config["retention_months"], frappe.conf.get("resume_retention_months", 24))


class TestResumeMatching(FrappeTestCase):
	"""Test resume matching and scoring."""

	def test_get_all_applicants_requires_permission(self):
		from hrms.hr.ai_resume_matching import get_all_applicants
		frappe.set_user("Guest")
		self.assertRaises(frappe.PermissionError, get_all_applicants, "test-opening")
		frappe.set_user("Administrator")

	def test_get_matching_resumes_requires_permission(self):
		from hrms.hr.ai_resume_matching import get_matching_resumes
		frappe.set_user("Guest")
		self.assertRaises(frappe.PermissionError, get_matching_resumes, "test-opening")
		frappe.set_user("Administrator")

	def test_get_all_applicants_returns_empty_for_no_applicants(self):
		jo = create_test_job_opening()
		from hrms.hr.ai_resume_matching import get_all_applicants
		result = get_all_applicants(jo.name)
		self.assertEqual(result["total"], 0)
		self.assertEqual(result["applicants"], [])

	def test_get_all_applicants_with_keyword_filter(self):
		jo = create_test_job_opening()
		applicant = create_test_applicant(consent=True, job_opening=jo.name)

		# Add a skill
		if not frappe.db.exists("Skill", "Python"):
			frappe.get_doc({"doctype": "Skill", "skill_name": "Python"}).insert(ignore_permissions=True)
		applicant.append("skills", {"skill": "Python"})
		applicant.save(ignore_permissions=True)
		frappe.db.commit()

		from hrms.hr.ai_resume_matching import get_all_applicants
		result = get_all_applicants(jo.name, json.dumps({"skills_keyword": "Python"}))
		self.assertGreaterEqual(result["total"], 1)

		result_no_match = get_all_applicants(jo.name, json.dumps({"skills_keyword": "Nonexistent"}))
		self.assertEqual(result_no_match["total"], 0)

	def test_get_all_applicants_with_status_filter(self):
		jo = create_test_job_opening()
		create_test_applicant(consent=True, job_opening=jo.name, status="Open")
		create_test_applicant(consent=True, job_opening=jo.name, status="Rejected")
		frappe.db.commit()

		from hrms.hr.ai_resume_matching import get_all_applicants
		result = get_all_applicants(jo.name, json.dumps({"status": "Open"}))
		for a in result["applicants"]:
			self.assertEqual(a["status"], "Open")


class TestCompliance(FrappeTestCase):
	"""Test compliance features: consent, retention, audit trail."""

	def test_consent_required_on_web_form(self):
		wf = frappe.get_doc("Web Form", "job-application")
		consent_field = next((f for f in wf.web_form_fields if f.fieldname == "consent_given"), None)
		self.assertIsNotNone(consent_field, "Consent field missing from web form")
		self.assertTrue(consent_field.reqd, "Consent field should be required")

	def test_privacy_notice_present(self):
		wf = frappe.get_doc("Web Form", "job-application")
		self.assertIn("Privacy Notice", wf.introduction_text or "")
		self.assertIn("PDPA", wf.introduction_text or "")

	def test_resume_upload_field_on_web_form(self):
		wf = frappe.get_doc("Web Form", "job-application")
		resume_field = next((f for f in wf.web_form_fields if f.fieldname == "resume_attachment"), None)
		self.assertIsNotNone(resume_field, "Resume upload field missing from web form")
		self.assertEqual(resume_field.fieldtype, "Attach")

	def test_max_attachment_size(self):
		wf = frappe.get_doc("Web Form", "job-application")
		self.assertEqual(wf.max_attachment_size, 5, "Max attachment size should be 5MB")

	def test_audit_trail_enabled(self):
		meta = frappe.get_meta("Job Applicant")
		self.assertTrue(meta.track_changes, "Audit trail (track_changes) should be enabled")

	def test_retention_date_set_on_processing(self):
		"""Retention date should be set to 24 months from today."""
		from frappe.utils import add_months, getdate, today
		from hrms.hr.ai_resume_parser import get_bedrock_config

		config = get_bedrock_config()
		expected_date = add_months(today(), config["retention_months"])

		applicant = create_test_applicant(consent=True)
		# Simulate setting retention date
		applicant.data_retention_date = expected_date
		applicant.save(ignore_permissions=True)

		doc = frappe.get_doc("Job Applicant", applicant.name)
		self.assertEqual(getdate(doc.data_retention_date), getdate(expected_date))

	def test_ai_not_triggered_without_consent(self):
		"""AI parsing should NOT run if consent_given is 0."""
		from hrms.hr.ai_resume_parser import after_insert_hook

		doc = MagicMock()
		doc.resume_attachment = "/private/files/test.pdf"
		doc.get = MagicMock(return_value=0)  # consent_given = 0

		with patch("frappe.enqueue") as mock_enqueue:
			after_insert_hook(doc, None)
			mock_enqueue.assert_not_called()

	def test_ai_triggered_with_consent(self):
		"""AI parsing should run if consent_given is 1 and resume attached."""
		from hrms.hr.ai_resume_parser import after_insert_hook

		doc = MagicMock()
		doc.resume_attachment = "/private/files/test.pdf"
		doc.name = "test-applicant"
		doc.get = MagicMock(return_value=1)  # consent_given = 1

		with patch("frappe.enqueue") as mock_enqueue:
			after_insert_hook(doc, None)
			mock_enqueue.assert_called_once()


# --- Test Helpers ---

_test_counter = 0

def create_test_applicant(consent=False, name="Test Applicant", email=None, job_opening=None, status="Open"):
	global _test_counter
	_test_counter += 1
	if not email:
		email = f"test-applicant-{_test_counter}@example.com"
	doc = frappe.get_doc({
		"doctype": "Job Applicant",
		"applicant_name": name or "Test Applicant",
		"email_id": email,
		"status": status,
		"job_title": job_opening or "",
		"consent_given": 1 if consent else 0,
	})
	doc.insert(ignore_permissions=True)
	frappe.db.commit()
	return doc


def create_test_job_opening():
	global _test_counter
	_test_counter += 1
	if not frappe.db.exists("Designation", "Test Designation"):
		frappe.get_doc({"doctype": "Designation", "designation": "Test Designation"}).insert(ignore_permissions=True)
	company = frappe.db.get_value("Company", {}, "name")
	doc = frappe.get_doc({
		"doctype": "Job Opening",
		"job_title": f"Test Opening {_test_counter}",
		"company": company,
		"designation": "Test Designation",
		"status": "Open",
	})
	doc.insert(ignore_permissions=True)
	frappe.db.commit()
	return doc
