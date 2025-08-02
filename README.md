# 🤖 LLM Chatbot – FastAPI + Streamlit

This is a simple chatbot I built using the Groq LLM API. It uses **FastAPI** for the backend and **Streamlit** for the frontend. The idea was to create a lightweight, fully working chatbot that shows the full request/response cycle, including token usage and execution time.

It’s meant to be easy to run locally or deploy in a Docker container.

---

## What it Does

- Takes a user message and sends it to the Groq API (using the `llama3-8b-8192` model)
- Returns the chatbot's reply along with how long it took
- Stores the chat history in the UI session
- Lets you see the conversation and response time in real time
- All backend logs print to the terminal to help with debugging

---

## How to Run It

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/llm-chatbot-groq.git
cd llm-chatbot
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add your API key

Create a file named `.env` in the `backend/` folder:

```
GROQ_API_KEY=your_groq_api_key_here
```

You can get a free key from [Groq](https://console.groq.com/keys).

---

### 4. Run the backend

```bash
cd backend
uvicorn main:app --reload
```

This starts the FastAPI server on `http://localhost:8000`

---

### 5. Run the frontend (Streamlit)

In a separate terminal:

```bash
cd frontend
streamlit run app.py
```

Now open `http://localhost:8501` to chat with the bot.

---

## Docker (Optional)

If you prefer using Docker:

```bash
docker build -t llm-chatbot .
docker run -p 8000:8000 -p 8501:8501 llm-chatbot
```

Both the API and UI will be live inside the container.

---

## Logs & Errors

The backend logs each user message, the model’s response, and how long it took to get a reply. If something fails (e.g., bad API key, network error), it logs it too — so it’s easy to debug.


## Tech Stack

- FastAPI (Python backend)
- Groq LLM API
- Streamlit (Frontend UI)
- Docker (for container deployment)
- Requests + logging

