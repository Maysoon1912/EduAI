# eduai_app.py
import streamlit as st
from eduai_utils import (
    generate_notes,
    generate_quiz,
    generate_flashcards,
    generate_lesson_plan,
    generate_question_paper,
    run_adaptive_test
)
from pdf_utils import extract_text_from_pdf
from gemini_utils import ask_gemini  # placeholder / real wrapper
from hf_utils import summarize_text   # placeholder / real wrapper

st.set_page_config(page_title="EduAI", layout="wide")
st.title("📚 EduAI — Personalized Learning & Assessment (Single Page)")

st.sidebar.title("EduAI")
role = st.sidebar.radio("You are a:", ["Student", "Teacher"])
st.sidebar.markdown("---")
st.sidebar.write("Tips:")
st.sidebar.write("- Run the app using `streamlit run eduai_app.py`")
st.sidebar.write("- This app uses cached placeholder AI functions that load instantly.")
st.sidebar.markdown("---")

# ------------------ STUDENT ------------------
if role == "Student":
    st.header("Student Dashboard")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Notes Generator")
        topic_notes = st.text_input("Enter chapter/topic for notes", key="notes_topic")
        if st.button("Generate Notes"):
            with st.spinner("Generating notes..."):
                notes = generate_notes(topic_notes)
            st.success("Notes generated")
            st.markdown(notes)

        st.subheader("Flashcards")
        topic_cards = st.text_input("Enter topic for flashcards", key="flash_topic")
        if st.button("Generate Flashcards"):
            with st.spinner("Generating flashcards..."):
                cards = generate_flashcards(topic_cards)
            st.success("Flashcards ready")
            for c in cards:
                st.write(f"**{c['front']}** — {c['back']}")
                st.markdown("---")

    with col2:
        st.subheader("Quiz Generator")
        topic_quiz = st.text_input("Enter chapter/topic for quiz", key="quiz_topic")
        num_q = st.slider("Number of MCQs", 1, 10, 5)
        if st.button("Generate Quiz"):
            with st.spinner("Generating quiz..."):
                quiz = generate_quiz(topic_quiz, num_q)
            st.success("Quiz generated")
            for i, q in enumerate(quiz, 1):
                st.write(f"Q{i}. {q['question']}")
                if "options" in q:
                    for opt in q["options"]:
                        st.write(f"- {opt}")
                st.write("")

        st.subheader("Adaptive Test")
        topic_adaptive = st.text_input("Topic for adaptive test", key="adaptive_topic")
        if st.button("Start Adaptive Test"):
            with st.spinner("Preparing adaptive test..."):
                questions = run_adaptive_test(topic_adaptive)
            st.success("Adaptive test ready")
            # Simple UI for answering
            answers = {}
            for idx, q in enumerate(questions):
                st.write(f"{idx+1}. {q['question']}")
                if "options" in q:
                    chosen = st.radio(f"Select (Q{idx+1})", q["options"], key=f"adapt_{idx}")
                    answers[q['question']] = chosen
                else:
                    ans = st.text_input(f"Answer (Q{idx+1})", key=f"adapt_input_{idx}")
                    answers[q['question']] = ans
            if st.button("Submit Adaptive Test"):
                with st.spinner("Evaluating..."):
                    report = {"score": "Sample (placeholder)", "weak_topics": ["Topic A"], "recommendation": "Revise Topic A"}
                st.success("Test evaluated")
                st.write(report)

    st.markdown("---")
    st.subheader("AI Tutor Chat")
    user_q = st.text_input("Ask your AI Tutor (short question):", key="tutor_input")
    if st.button("Ask Tutor"):
        with st.spinner("Getting answer..."):
            ans = ask_gemini(user_q)
        st.success("Answer ready")
        st.write(ans)

# ------------------ TEACHER ------------------
else:
    st.header("Teacher Dashboard")
    st.subheader("Upload PDF / Syllabus")
    uploaded = st.file_uploader("Upload PDF (teacher can upload chapters here)", type=["pdf"])
    # If you uploaded a file earlier via Jupyter UI, you can reference the local test file path:
    STUB_UPLOADED_FILE = "/mnt/data/a6381e9f-0750-402b-b762-caa546929066.jpg"
    st.caption(f"Example local test file path (if you uploaded earlier): {STUB_UPLOADED_FILE}")

    if uploaded:
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded)
        st.success("Text extracted")
        st.write(text[:1000] + ("..." if len(text) > 1000 else ""))

        if st.button("Generate Worksheet from PDF"):
            with st.spinner("Generating worksheet..."):
                qlist = generate_quiz(text, num_questions=5)
            st.success("Worksheet ready")
            for q in qlist:
                st.write("❓", q["question"])
                if "options" in q:
                    st.write("Options:", q["options"])
                st.write("---")

    st.markdown("---")
    st.subheader("Lesson Plan Generator")
    topic_lp = st.text_input("Topic for lesson plan", key="lp_topic")
    if st.button("Generate Lesson Plan"):
        with st.spinner("Generating lesson plan..."):
            plan = generate_lesson_plan(topic_lp)
        st.success("Lesson plan generated")
        st.write(plan)

    st.subheader("Question Paper Generator")
    topic_qp = st.text_input("Topic for question paper", key="qp_topic")
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    if st.button("Generate Question Paper"):
        with st.spinner("Generating question paper..."):
            paper = generate_question_paper(topic_qp, difficulty)
        st.success("Question paper generated")
        st.write(paper)

st.markdown("---")
st.caption("EduAI — Single Page Full Functionality (placeholders).")
