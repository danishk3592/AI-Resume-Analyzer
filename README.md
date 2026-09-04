# 🤖 AI Resume Analyzer & Job Match Assistant

An AI-powered web application that analyzes resumes against job descriptions and provides ATS-style scoring, skill-gap analysis, personalized improvement suggestions, interview questions, and AI-powered resume rewriting.

## 🌐 Live Demo

🚀 **[Try the Live Application]((https://ai-resume-analyzer-virtuoso.streamlit.app/))**

📂 **[View Source Code on GitHub]((https://github.com/danishk3592/AI-Resume-Analyzer.git))**

---

## ✨ Features

- 📄 Upload resume in PDF format
- 💼 Analyze resume against any job description
- 📊 AI-powered ATS compatibility score
- ✅ Identify matched skills
- ❌ Identify missing skills
- 💡 Generate personalized resume improvement suggestions
- 🎯 Generate role-specific interview questions
- ✍️ Rewrite resume bullet points using AI
- 📥 Download analysis report
- 🌐 Deployed as a live web application

---

## 🧠 How It Works

```text
             Resume PDF
                 │
                 ▼
        ┌─────────────────┐
        │  PDF Extraction │
        │     PyPDF       │
        └────────┬────────┘
                 │
                 ▼
Job Description ────────► Gemini AI
                            │
                            ▼
                 ┌────────────────────┐
                 │ AI Resume Analysis │
                 └─────────┬──────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      ATS Score       Skill Analysis    Suggestions
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                  Interview Questions
                           │
                           ▼
                    Resume Rewriter
