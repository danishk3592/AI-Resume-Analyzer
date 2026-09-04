import os
import json
import re
import streamlit as st

from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing in .env")

client = genai.Client(api_key=api_key)


def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an expert ATS resume evaluator and technical recruiter.

Analyze the candidate's resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return ONLY valid JSON.
Do not use markdown.
Do not use ```json.
Do not add any text before or after the JSON.

Use exactly this structure:

{{
  "ats_score": 90,
  "matched_skills": [
    "Java",
    "Python",
    "SQL"
  ],
  "missing_skills": [
    "JUnit",
    "Docker"
  ],
  "improvements": [
    "Add measurable achievements to project descriptions",
    "Mention testing frameworks used",
    "Add CI/CD experience if applicable"
  ],
  "interview_questions": [
    "Explain one major project from your resume.",
    "Why did you choose your technology stack?",
    "How would you improve the scalability of your project?",
    "Explain a difficult technical problem you solved.",
    "How would you test your application?"
  ],
  "verdict": "Strong match with some opportunities for improvement."
}}

Rules:
- ats_score must be an integer from 0 to 100.
- matched_skills should contain skills clearly supported by the resume and relevant to the job.
- missing_skills should contain important job requirements not clearly demonstrated in the resume.
- improvements should be practical and specific.
- Generate 5 interview questions relevant to this candidate and job.
- Keep the verdict under 40 words.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    raw_text = response.text.strip()

    # Remove accidental markdown fences if Gemini adds them
    raw_text = re.sub(r"^```json\s*", "", raw_text)
    raw_text = re.sub(r"^```\s*", "", raw_text)
    raw_text = re.sub(r"\s*```$", "", raw_text)

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        raise ValueError(
            "AI returned an invalid response. Please try analyzing again."
        )


def rewrite_resume_bullet(bullet, job_description):
    prompt = f"""
You are an expert technical resume writer.

Rewrite the following resume bullet point to make it:
- Professional
- Concise
- Achievement-oriented
- ATS-friendly
- Relevant to the job description
- Truthful — do not invent technologies, metrics, or achievements

JOB DESCRIPTION:
{job_description}

ORIGINAL BULLET:
{bullet}

Return only the improved bullet point.
Do not add quotation marks.
Do not explain your changes.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text.strip()