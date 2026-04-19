"""
AI Resume Parser for HRDL8
Extracts candidate information from uploaded resumes using Amazon Bedrock (Claude Sonnet 4.6).
Runs as a background job after Job Applicant creation.
"""
import json
import os

import frappe
from frappe import _
from frappe.utils import add_months, today


# Configuration — read from site config, no hardcoding
def get_bedrock_config():
	return {
		"region": frappe.conf.get("bedrock_region", "us-east-1"),
		"model_id": frappe.conf.get("bedrock_model_id", "anthropic.claude-sonnet-4-6"),
		"retention_months": frappe.conf.get("resume_retention_months", 24),
	}


def extract_text_from_pdf(file_path):
	"""Extract text from a PDF file using pdfplumber (preferred) or PyPDF2 fallback."""
	text = ""
	try:
		import pdfplumber
		with pdfplumber.open(file_path) as pdf:
			for page in pdf.pages:
				page_text = page.extract_text()
				if page_text:
					text += page_text + "\n"
	except ImportError:
		try:
			from PyPDF2 import PdfReader
			reader = PdfReader(file_path)
			for page in reader.pages:
				page_text = page.extract_text()
				if page_text:
					text += page_text + "\n"
		except ImportError:
			frappe.log_error("Neither pdfplumber nor PyPDF2 is installed", "AI Resume Parser")
			return ""
	except Exception as e:
		frappe.log_error(f"PDF extraction error: {e}", "AI Resume Parser")
		return ""
	return text.strip()


def extract_text_from_docx(file_path):
	"""Extract text from a DOCX file."""
	try:
		import docx
		doc = docx.Document(file_path)
		return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
	except ImportError:
		frappe.log_error("python-docx is not installed", "AI Resume Parser")
		return ""
	except Exception as e:
		frappe.log_error(f"DOCX extraction error: {e}", "AI Resume Parser")
		return ""


def get_resume_text(doc):
	"""Get text content from the resume attachment."""
	if not doc.resume_attachment:
		return ""

	file_doc = frappe.get_doc("File", {"file_url": doc.resume_attachment})
	file_path = file_doc.get_full_path()

	if not os.path.exists(file_path):
		frappe.log_error(f"Resume file not found: {file_path}", "AI Resume Parser")
		return ""

	ext = os.path.splitext(file_path)[1].lower()
	if ext == ".pdf":
		return extract_text_from_pdf(file_path)
	elif ext in (".doc", ".docx"):
		return extract_text_from_docx(file_path)
	else:
		frappe.log_error(f"Unsupported file type: {ext}", "AI Resume Parser")
		return ""


def parse_resume_with_bedrock(resume_text):
	"""Send resume text to Bedrock Sonnet 4.6 and get structured data back."""
	try:
		import boto3
	except ImportError:
		frappe.log_error("boto3 is not installed", "AI Resume Parser")
		return None

	config = get_bedrock_config()
	client = boto3.client("bedrock-runtime", region_name=config["region"])

	prompt = """Analyze this resume and extract the following information in JSON format:
{
  "name": "Full name of the candidate",
  "email": "Email address if found",
  "phone": "Phone number if found",
  "country": "Country if mentioned",
  "skills": ["list", "of", "technical", "and", "professional", "skills"],
  "experience_summary": "A 2-3 sentence summary of the candidate's professional experience and key qualifications"
}

Rules:
- Only extract information explicitly present in the resume
- For skills, include both technical skills (programming languages, tools) and professional skills (project management, etc.)
- Keep skills as individual items, not phrases
- If a field is not found, use null
- Return ONLY valid JSON, no other text

Resume:
"""
	body = json.dumps({
		"anthropic_version": "bedrock-2023-05-31",
		"max_tokens": 1024,
		"messages": [{"role": "user", "content": prompt + resume_text[:8000]}],
	})

	response = client.invoke_model(modelId=config["model_id"], body=body)
	result = json.loads(response["body"].read())
	content = result["content"][0]["text"]

	# Extract JSON from response
	try:
		# Handle case where model wraps JSON in markdown code block
		if "```json" in content:
			content = content.split("```json")[1].split("```")[0]
		elif "```" in content:
			content = content.split("```")[1].split("```")[0]
		return json.loads(content.strip())
	except (json.JSONDecodeError, IndexError):
		frappe.log_error(f"Failed to parse Bedrock response: {content}", "AI Resume Parser")
		return None


def process_resume(doc_name):
	"""Background job: parse resume and auto-fill fields on Job Applicant."""
	try:
		doc = frappe.get_doc("Job Applicant", doc_name)

		if doc.get("ai_parsed"):
			return

		resume_text = get_resume_text(doc)
		if not resume_text:
			return

		parsed = parse_resume_with_bedrock(resume_text)
		if not parsed:
			return

		# Auto-fill fields only if they're empty (don't overwrite user input)
		if not doc.applicant_name and parsed.get("name"):
			doc.applicant_name = parsed["name"]

		if not doc.email_id and parsed.get("email"):
			doc.email_id = parsed["email"]

		if not doc.phone_number and parsed.get("phone"):
			doc.phone_number = parsed["phone"]

		if not doc.country and parsed.get("country"):
			country = frappe.db.get_value("Country", {"name": ["like", f"%{parsed['country']}%"]})
			if country:
				doc.country = country

		if parsed.get("experience_summary"):
			doc.experience_summary = parsed["experience_summary"]

		# Add skills
		if parsed.get("skills"):
			existing_skills = [s.skill for s in doc.get("skills", [])]
			for skill_name in parsed["skills"]:
				if skill_name in existing_skills:
					continue
				# Create Skill if it doesn't exist
				if not frappe.db.exists("Skill", skill_name):
					frappe.get_doc({"doctype": "Skill", "skill_name": skill_name}).insert(ignore_permissions=True)
				doc.append("skills", {"skill": skill_name})

		# Set compliance fields
		config = get_bedrock_config()
		if not doc.data_retention_date:
			doc.data_retention_date = add_months(today(), config["retention_months"])

		doc.ai_parsed = 1
		doc.save(ignore_permissions=True)
		frappe.db.commit()

	except Exception as e:
		frappe.log_error(f"Resume processing failed for {doc_name}: {e}", "AI Resume Parser")


def after_insert_hook(doc, method):
	"""Hook called after Job Applicant is inserted. Enqueues background job."""
	if doc.resume_attachment and doc.get("consent_given") and not doc.get("ai_parsed"):
		frappe.enqueue(
			"hrms.hr.ai_resume_parser.process_resume",
			doc_name=doc.name,
			queue="short",
			enqueue_after_commit=True,
		)


@frappe.whitelist(allow_guest=True)
def parse_resume_on_upload(file_url):
	"""Synchronous resume parsing — called from client on file upload.
	Returns parsed data for the client to populate fields before save."""
	if not file_url:
		return {"error": "No file URL provided"}

	try:
		file_doc = frappe.get_doc("File", {"file_url": file_url})
		file_path = file_doc.get_full_path()

		ext = os.path.splitext(file_path)[1].lower()
		if ext == ".pdf":
			text = extract_text_from_pdf(file_path)
		elif ext in (".doc", ".docx"):
			text = extract_text_from_docx(file_path)
		else:
			return {"error": f"Unsupported file type: {ext}. Please upload PDF, DOC, or DOCX."}

		if not text:
			return {"error": "Could not extract text from the file."}

		parsed = parse_resume_with_bedrock(text)
		if not parsed:
			return {"error": "AI could not parse the resume. Please fill in details manually."}

		return {"success": True, "data": parsed}

	except Exception as e:
		frappe.log_error(f"Resume parse on upload failed: {e}", "AI Resume Parser")
		return {"error": str(e)}
