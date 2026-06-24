from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = pickle.load(open("salary_api.pkl", "rb"))

# Request body structure
class InputData(BaseModel):
    experience: float

@app.get("/")
def home():
    return {"message": "All OK"}

@app.get("/predict")
def predict(experience: float):
    result = model.predict([[experience]])
    return {
        "experience": experience,
        "predicted_salary": float(result[0])
    }