# hf_utils.py
from transformers import pipeline

# lightweight summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text: str):
    result = summarizer(text, max_length=130, min_length=40)
    return result[0]["summary_text"]

def generate_dummy_mcqs(text, num=5):
    mcqs = []
    for i in range(num):
        mcqs.append({
            "question": f"What is a key idea in this text? (MCQ {i+1})",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        })
    return mcqs
