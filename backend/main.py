from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv
import time
import logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    # filename="chatbot.log",  # Optional logging to file
    # filemode="a"
)

app = FastAPI()

class Query(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "LLM Chatbot API is running"}

@app.post("/chat")
def chat(query: Query):
    start_time = time.time()
    logging.info(f"Received user query: {query.message}")

    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": query.message}
        ]
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        data = response.json()

        reply = data["choices"][0]["message"]["content"]
        exec_time = round(time.time() - start_time, 2)

        usage = data.get("usage", {})

        return {
            "response": reply,
            "execution_time": exec_time,
            "model_total_time": usage.get("total_time", "N/A"),
            "token_usage": {
                "prompt_tokens": usage.get("prompt_tokens", "N/A"),
                "completion_tokens": usage.get("completion_tokens", "N/A"),
                "total_tokens": usage.get("total_tokens", "N/A")
            }
        }

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {str(e)}")
        return {"error": f"API request failed: {str(e)}"}

    except Exception as e:
        logging.exception("Unexpected error occurred")
        return {"error": f"Unexpected error: {str(e)}"}
