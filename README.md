# AI Learning Assistant (Dockerized)

An AI-powered learning assistant that processes course PDFs (syllabi,
lecture slides, notes) and generates quizzes, flashcards, and
explanations using Large Language Models.

The application uses Streamlit for the UI, PyMuPDF for PDF text
extraction, and Groq LLM APIs for content generation. The entire
application is containerized using Docker, enabling reproducible
deployment across environments.

------------------------------------------------------------------------

## Features

-   Upload course PDFs
-   Automatic text extraction from PDFs
-   Generate multiple-choice quizzes
-   Generate flashcards for studying
-   Generate explanations of course content
-   Interactive Streamlit web interface
-   Dockerized deployment

------------------------------------------------------------------------

## Tech Stack

-   Python
-   Streamlit
-   PyMuPDF
-   Groq API
-   Docker

------------------------------------------------------------------------

## Project Structure

    ai_learning_assistant/
    │
    ├── app.py
    ├── utils.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .dockerignore
    └── README.md

------------------------------------------------------------------------

## Local Setup

### 1. Clone the repository

    git clone https://github.com/yourusername/ai-learning-assistant.git
    cd ai-learning-assistant

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Set your Groq API key

Create a `.env` file:

    GROQ_API_KEY=your_api_key_here

### 4. Run the application

    streamlit run app.py

Open your browser and go to:

    http://localhost:8501

------------------------------------------------------------------------

## Running with Docker

### Build the Docker image

    docker build -t ai-learning-assistant .

### Run the Docker container

    docker run -p 8501:8501 -e GROQ_API_KEY=your_api_key ai-learning-assistant

### Open the application

    http://localhost:8501

------------------------------------------------------------------------

## Docker Environment

| Component \| Description \|

\|-----------\|-------------\| Base Image \| Python 3.10 Slim \| \| Port
\| 8501 \| \| Framework \| Streamlit \| \| Environment Variable \|
GROQ_API_KEY \|

------------------------------------------------------------------------

## Future Improvements

-   Implement true Retrieval-Augmented Generation (RAG)
-   Add embeddings and vector search with ChromaDB
-   Add CI/CD pipeline for automated Docker builds
-   Deploy to cloud platforms (AWS, Render, or GCP)

------------------------------------------------------------------------

## Author

Sai Manvija Cherukuri\
MS Computer Science -- NC State University
