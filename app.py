import streamlit as st
import json
from utils import (
    extract_text_from_pdf,
    generate_quiz,
    generate_flashcards,
    generate_explanation
)

st.set_page_config(page_title="AI Learning Assistant", layout="wide")

st.title("📘 AI-Powered Learning Assistant")
st.write("Upload a course PDF to generate quizzes, flashcards, and explanations.")


def extract_json(text):
    start = text.find("[")
    end = text.rfind("]")
    if start == -1 or end == -1:
        return None
    return text[start:end + 1]


if "content" not in st.session_state:
    st.session_state.content = None
if "mode" not in st.session_state:
    st.session_state.mode = None

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    option = st.selectbox(
        "What would you like to generate?",
        ["Quiz", "Flashcards", "Explanation"]
    )

    if st.button("Generate"):
        if option == "Quiz":
            raw = generate_quiz(text)
            json_text = extract_json(raw)
            if json_text:
                st.session_state.content = json.loads(json_text)
                st.session_state.mode = "Quiz"

        elif option == "Flashcards":
            raw = generate_flashcards(text)
            json_text = extract_json(raw)
            if json_text:
                st.session_state.content = json.loads(json_text)
                st.session_state.mode = "Flashcards"

        else:
            st.session_state.content = generate_explanation(text)
            st.session_state.mode = "Explanation"


if st.session_state.content is not None:
    st.subheader("Generated Output")

 
    if st.session_state.mode == "Explanation":
        st.write(st.session_state.content)

   
    elif st.session_state.mode == "Quiz":
        score = 0

        for i, q in enumerate(st.session_state.content):
            st.markdown(f"### Q{i+1}. {q['question']}")

            selected = st.radio(
                "Choose an answer:",
                q["options"],
                key=f"quiz_{i}"
            )

            
            selected_index = q["options"].index(selected)
            selected_letter = chr(ord("A") + selected_index)

            if st.button("Submit", key=f"submit_{i}"):
                if selected_letter == q["correct_answer"]:
                    st.success("✅ Correct!")
                    score += 1
                else:
                    correct_text = q["options"][
                        ord(q["correct_answer"]) - ord("A")
                    ]
                    st.error(
                        f"❌ Incorrect. Correct answer: "
                        f"{q['correct_answer']} — {correct_text}"
                    )

            st.divider()

        st.markdown(
            f"## 🎯 Final Score: {score} / {len(st.session_state.content)}"
        )

   
    elif st.session_state.mode == "Flashcards":
        st.markdown("## 🧠 Flashcards")

        for i, card in enumerate(st.session_state.content):
            with st.expander(
                f"Flashcard {i+1}: {card['question']}"
            ):
                st.write(card["answer"])
