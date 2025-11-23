# eduai_utils.py
from functools import lru_cache
from gemini_utils import ask_gemini
from hf_utils import summarize_text

# Use simple in-memory caching to avoid repeated slow calls in development
@lru_cache(maxsize=128)
def generate_notes(topic: str) -> str:
    if not topic:
        return "Please provide a topic."
    # Placeholder: call your real model here (Gemini/HF/OpenAI)
    prompt = f"Generate simple study notes for grade-appropriate students about: {topic}"
    # real: return ask_gemini(prompt)
    return f"## Notes for: {topic}\n- Point 1 about {topic}\n- Point 2 about {topic}\n- Example: ..."

@lru_cache(maxsize=64)
def generate_quiz(text_or_topic: str, num_questions: int = 5):
    if not text_or_topic:
        return []
    # Placeholder: more sophisticated MCQ generation should be plugged here
    qlist = []
    for i in range(num_questions):
        qlist.append({
            "question": f"What is an important idea of {text_or_topic} (Q{i+1})?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        })
    return qlist

@lru_cache(maxsize=64)
def generate_flashcards(topic: str):
    if not topic:
        return []
    # placeholder
    return [
        {"front": f"{topic} — Term 1", "back": "Definition 1"},
        {"front": f"{topic} — Term 2", "back": "Definition 2"},
    ]

@lru_cache(maxsize=32)
def generate_lesson_plan(topic: str):
    if not topic:
        return "Enter a topic to generate a lesson plan."
    return f"Lesson Plan for {topic}\n\nObjectives:\n- Understand {topic}\nActivities:\n- Intro\n- Practice\nAssessment:\n- Short quiz"

@lru_cache(maxsize=32)
def generate_question_paper(topic: str, difficulty: str = "Medium"):
    if not topic:
        return "Enter topic"
    return f"Question Paper — {topic} (Difficulty: {difficulty})\n1. Short question\n2. Long question\n3. MCQs"

def run_adaptive_test(topic: str):
    # placeholder adaptive test: produce 3 questions with options
    if not topic:
        return []
    return [
        {"question": f"{topic} - Q1", "options": ["A","B","C","D"]},
        {"question": f"{topic} - Q2", "options": ["A","B","C","D"]},
        {"question": f"{topic} - Q3", "options": ["A","B","C","D"]},
    ]
