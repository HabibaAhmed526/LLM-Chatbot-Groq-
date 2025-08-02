# 🤖 LLM-Based Chatbot with API & Streamlit UI

This project is a simple chatbot built using an open-source Large Language Model (LLM) API (Groq), powered by FastAPI for the backend and Streamlit for the frontend UI. It allows users to chat with an AI agent and see token usage, response time, and a complete conversation history.

---

## 📌 Project Features

- API backend using FastAPI to handle user queries
- Integration with Groq LLM API
- Simple Streamlit UI to interact with the chatbot
- Displays conversation history
- Shows token usage and execution time
- Dockerized for easy deployment


## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/LLM-Chatbot-Groq-.git
cd llm_chatbot
```

---

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file in the `backend/` directory with:

```
GROQ_API_KEY=your_actual_groq_api_key
```

---

### 4. Run Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

It runs at: [http://localhost:8000](http://localhost:8000)

---

### 5. Run Frontend (Streamlit)

Open a new terminal:

```bash
cd frontend
streamlit run app.py
```

The UI will be at: [http://localhost:8501](http://localhost:8501)

---

## 🐳 Docker Deployment (Optional)

To containerize and run with Docker:

```bash
docker build -t llm-chatbot .
docker run -p 8000:8000 -p 8501:8501 llm-chatbot
```

---

## 📄 Logging & Error Handling

- The backend includes basic logging to track API errors and runtime issues.
- Logs are printed to the terminal for debugging.

---

## 🧠 Challenges Faced

- Handling async requests between FastAPI and the LLM API.
- Ensuring token usage and time tracking were accurately displayed in the UI.
- Fixing CORS and connection issues between backend and frontend.
- Docker networking setup between Streamlit and FastAPI inside the container.
