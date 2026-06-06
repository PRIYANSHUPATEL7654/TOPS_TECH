
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import google.generativeai as genai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyBhuxaikj74kHIV9fFCx9mZp5b7N8gZV38"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

df = pd.read_csv("animals_dataset.csv")

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Advanced AI CSV Chatbot Running"}


@app.post("/chat")
async def chat(data: ChatRequest):

    user_message = data.message

    # Dataset preview
    dataset_preview = df.head(20).to_string()

    # Column names
    columns = ", ".join(df.columns)

    prompt = f"""
You are a smart CSV dataset assistant.

Dataset Columns:
{columns}

Dataset Sample:
{dataset_preview}

User Question:
{user_message}

Rules:
1. Answer only from dataset.
2. Keep answers short and clean.
3. If numerical analysis is needed, estimate from sample.
4. If question is unrelated, say:
'I can answer only dataset-related questions.'
"""

    try:
        response = model.generate_content(prompt)

        return {
            "reply": response.text
        }

    except Exception as e:
        return {
            "reply": f"Error: {str(e)}"
        }
