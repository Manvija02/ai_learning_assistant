# AI-Powered Learning Assistant

An interactive AI-powered study tool that transforms course PDFs into quizzes, flashcards, and simplified explanations. The application uses large language models (LLMs) to generate learning content and presents it through a clean, interactive Streamlit interface.

This project was built from scratch with a focus on real-world engineering challenges such as PDF parsing, LLM integration, API instability, and stateful UI design.


## Features

* PDF upload and text extraction
* AI-generated quizzes with:

  * Multiple-choice questions
  * Answer selection and submit-to-reveal feedback
  * Final score summary
* Interactive flashcards with click-to-reveal answers
* Simplified explanations for dense academic content
* Stateful UI to preserve quiz and flashcard progress
* Robust handling of non-deterministic LLM outputs

## Tech Stack

* Frontend / UI: Streamlit
* Backend: Python
* PDF Parsing: PyMuPDF (fitz)
* LLM Provider: Groq (LLaMA 3.1)
* Environment: Python 3 (Conda-compatible)

## How It Works

1. PDF Upload

   * The uploaded PDF is processed in memory using PyMuPDF
   * Text is extracted page by page

2. Content Selection

   * User chooses to generate a quiz, flashcards, or an explanation

3. LLM Processing

   * Extracted text is sent to an LLM via Groq
   * The model returns structured JSON for quizzes and flashcards

4. Interactive Learning Interface

   * Streamlit renders:

     * Multiple-choice quizzes with submission feedback
     * Expandable flashcards
     * Plain-text explanations


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-learning-assistant.git
cd ai-learning-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variable (Groq API Key)

```bash
export GROQ_API_KEY="your_api_key_here"
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

