# streamlit_app.py
import streamlit as st
from openai_utils import ask_gpt
from hf_utils import summarize_text, generate_dummy_mcqs

st.set_page_config(page_title="EduAI", layout="wide")
st.title("EduAI — Personalized Learning Prototype")

tab1, tab2 = st.tabs(["Student", "Teacher"])

with tab1:
    st.header("Student Tools")
    text = st.text_area("Enter topic/chapter text")
    grade = st.selectbox("Select Grade", list(range(1, 13)), index=9)

    if st.button("Generate Notes & MCQs"):
        with st.spinner("Generating..."):
            notes = ask_gpt(f"Write simple notes for grade {grade}: {text}")
            mcqs = generate_dummy_mcqs(text)

        st.subheader("AI Notes")
        st.write(notes)

        st.subheader("MCQs")
        for i, q in enumerate(mcqs):
            st.markdown(f"**Q{i+1}. {q['question']}**")
            for opt in q["options"]:
                st.write(f"- {opt}")

with tab2:
    st.header("Teacher Tools")
    uploaded = st.file_uploader("Upload PDF (prototype only)", type=["pdf"])
    if uploaded:
        st.success(f"Received file: {uploaded.name}")
        st.info("Full PDF → Worksheet will be implemented later.")
