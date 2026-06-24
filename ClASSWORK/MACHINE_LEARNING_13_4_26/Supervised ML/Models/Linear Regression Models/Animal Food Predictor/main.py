from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import numpy as np
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))

class AnimalInput(BaseModel):
    animal: str
    weight: float
    height: float
    age: int

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

@app.get("/animals")
def get_animals():
    return {
        "animals": encoder.classes_.tolist()
    }

@app.post("/predict")
def predict(data: AnimalInput):

    if data.animal not in encoder.classes_:
        return {"error": "Unknown Animal"}

    encoded_animal = encoder.transform([data.animal])[0]

    input_data = np.array([[
        encoded_animal,
        data.weight,
        data.height,
        data.age
    ]])

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)

    return {
        "prediction": round(float(prediction[0]), 2)
    }

app.mount(
    "/assets",
    StaticFiles(directory="frontend/assets"),
    name="assets"
)
