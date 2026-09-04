# 🤖 AI Resume Analyzer & Job Match Assistant

An AI-powered web application that analyzes a candidate's resume against a job description and provides an ATS compatibility score, skill-gap analysis, resume improvement suggestions, and interview questions.

## 🚀 Features

- 📄 Upload resume in PDF format
- 💼 Paste any job description
- 🤖 AI-powered resume analysis
- 📊 ATS compatibility score
- ✅ Matched skills detection
- ❌ Missing skills identification
- 💡 Personalized resume improvement suggestions
- 🎯 AI-generated interview questions
- 📥 Downloadable analysis report
- 🌐 Interactive Streamlit web interface

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- PyPDF
- Python-dotenv
- Generative AI / NLP

## 🏗️ Architecture

```text
                 ┌─────────────────┐
                 │   User Resume   │
                 │      (PDF)      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  PDF Extraction │
                 │     PyPDF       │
                 └────────┬────────┘
                          │
                          ▼
┌─────────────────┐   ┌─────────────────┐
│ Job Description │──▶│  Gemini AI      │
└─────────────────┘   │ Analysis Engine │
                      └────────┬────────┘
                               │
                               ▼
                 ┌────────────────────────┐
                 │ Resume Analysis        │
                 │                        │
                 │ ATS Score              │
                 │ Matched Skills         │
                 │ Missing Skills         │
                 │ Improvements            │
                 │ Interview Questions    │
                 └────────────────────────┘
                               │
                               ▼
                     ┌─────────────────┐
                     │ Streamlit UI    │
                     └─────────────────┘