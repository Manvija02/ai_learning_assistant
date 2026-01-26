import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text
import requests
import os

from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_llm(prompt):
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=512,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"⚠️ LLM Error: {str(e)}"


def generate_quiz(text):
    prompt = f"""
    Create a quiz with 5 multiple-choice questions from the content below.

    Return the result STRICTLY in this JSON format:
    [
      {{
        "question": "...",
        "options": ["A", "B", "C", "D"],
        "correct_answer": "A"
      }}
    ]

    Content:
    {text[:2000]}
    """
    return query_llm(prompt)

def generate_flashcards(text):
    prompt = f"""
    Create 5 flashcards from the content below.

    Return STRICTLY in this JSON format:
    [
      {{
        "question": "...",
        "answer": "..."
      }}
    ]

    Content:
    {text[:2000]}
    """
    return query_llm(prompt)

def generate_explanation(text):
    prompt = f"""
    Explain the following content in simple terms as if teaching a college student:

    {text[:2000]}
    """
    return query_llm(prompt)
