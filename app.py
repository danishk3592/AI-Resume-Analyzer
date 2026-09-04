import streamlit as st

from pdf_reader import extract_text_from_pdf
from analyzer import analyze_resume, rewrite_resume_bullet


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        opacity: 0.75;
        margin-bottom: 25px;
    }

    .score-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid rgba(128,128,128,0.25);
    }

    .score {
        font-size: 55px;
        font-weight: 800;
    }

    .skill-box {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        min-height: 170px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🤖 AI Resume Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered resume analysis and job matching</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- INPUT ----------------

resume_col, job_col = st.columns(2)

with resume_col:

    st.subheader("📄 Resume")

    uploaded_file = st.file_uploader(
        "Upload your resume",
        type=["pdf"]
    )

    if uploaded_file:
        st.success(f"✅ {uploaded_file.name}")


with job_col:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the job description",
        height=220,
        placeholder=(
            "Paste the complete job description here..."
        )
    )


st.divider()


# ---------------- ANALYSIS ----------------

if st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True
):

    if uploaded_file is None:

        st.warning("Please upload your resume.")

        st.stop()

    if not job_description.strip():

        st.warning("Please paste a job description.")

        st.stop()

    try:

        with st.spinner(
            "🤖 AI is analyzing your resume..."
        ):

            resume_text = extract_text_from_pdf(
                uploaded_file
            )

            if not resume_text:

                st.error(
                    "Could not extract text from this PDF."
                )

                st.stop()

            analysis = analyze_resume(
                resume_text,
                job_description
            )

        st.success(
            "✅ Analysis completed successfully!"
        )

        st.divider()

        # ---------------- ATS SCORE ----------------

        st.markdown(
            '<div class="section-title">📊 ATS Compatibility</div>',
            unsafe_allow_html=True
        )

        score = analysis.get("ats_score", 0)

        score_col1, score_col2, score_col3 = st.columns([1, 2, 1])

        with score_col2:
            st.markdown(
                f"""
                <div class="score-box">
                    <div style="font-size:18px;">ATS MATCH SCORE</div>
                    <div class="score">{score}/100</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(
                min(max(int(score), 0), 100) / 100
            )

            if score >= 80:
              st.success("🔥 Excellent match for this job!")
            elif score >= 60:
               st.info("👍 Good match, but there is room for improvement.")
            else:
                st.warning("⚠️ Significant improvement is recommended.")

        st.write("")


        # ---------------- SKILLS ----------------

        matched = analysis.get(
            "matched_skills",
            []
        )

        missing = analysis.get(
            "missing_skills",
            []
        )

        skill_col1, skill_col2 = st.columns(2)


        with skill_col1:

            st.markdown(
                '<div class="skill-box">',
                unsafe_allow_html=True
            )

            st.markdown(
                "### ✅ Matched Skills"
            )

            for skill in matched:

                st.write(f"• {skill}")

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


        with skill_col2:

            st.markdown(
                '<div class="skill-box">',
                unsafe_allow_html=True
            )

            st.markdown(
                "### ❌ Missing Skills"
            )

            for skill in missing:

                st.write(f"• {skill}")

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


        st.write("")


        # ---------------- IMPROVEMENTS ----------------

        st.subheader("💡 Resume Improvements")

        improvements = analysis.get(
            "improvements",
            []
        )

        for index, improvement in enumerate(
            improvements,
            start=1
        ):

            st.info(
                f"{index}. {improvement}"
            )


        # ---------------- INTERVIEW QUESTIONS ----------------

        st.subheader("🎯 AI Interview Questions")

        questions = analysis.get(
            "interview_questions",
            []
        )

        for index, question in enumerate(
            questions,
            start=1
        ):

            with st.expander(
                f"Question {index}"
            ):

                st.write(question)


        # ---------------- VERDICT ----------------

        st.subheader("🧠 AI Verdict")

        verdict = analysis.get(
            "verdict",
            "No verdict available."
        )

        st.success(verdict)


        # ---------------- DOWNLOAD ----------------

        report = f"""
AI RESUME ANALYZER REPORT
=========================

ATS SCORE: {score}/100

MATCHED SKILLS:
{chr(10).join("- " + x for x in matched)}

MISSING SKILLS:
{chr(10).join("- " + x for x in missing)}

RESUME IMPROVEMENTS:
{chr(10).join("- " + x for x in improvements)}

INTERVIEW QUESTIONS:
{chr(10).join(str(i + 1) + ". " + x for i, x in enumerate(questions))}

AI VERDICT:
{verdict}
"""

        st.download_button(
            label="📥 Download Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain",
            use_container_width=True
        )


    except Exception as e:

        st.error(
            f"Something went wrong: {e}"
        )


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Built with Python • Streamlit • Gemini • PDF Processing"
)

st.divider()

st.header("✍️ AI Resume Rewriter")

st.write(
    "Improve individual resume bullet points using AI and the target job description."
)

bullet = st.text_area(
    "Paste a resume bullet point",
    placeholder="Example: Developed a task scheduler using Java."
)

if st.button(
    "✨ Rewrite Bullet Point",
    use_container_width=True
):

    if not bullet.strip():
        st.warning("Please enter a resume bullet point.")

    elif not job_description.strip():
        st.warning(
            "Please enter a job description above so the AI can tailor the bullet."
        )

    else:

        with st.spinner("✨ Rewriting your bullet point..."):

            try:

                improved_bullet = rewrite_resume_bullet(
                    bullet,
                    job_description
                )

                st.subheader("✅ Improved Version")

                st.success(improved_bullet)

                st.download_button(
                    "📥 Download Improved Bullet",
                    data=improved_bullet,
                    file_name="improved_resume_bullet.txt",
                    mime="text/plain",
                    use_container_width=True
                )

            except Exception as e:

                st.error(f"Something went wrong: {e}")