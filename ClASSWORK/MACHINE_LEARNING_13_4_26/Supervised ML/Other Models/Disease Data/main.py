from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import pickle
import numpy as np

# =========================================
# FASTAPI APP
# =========================================

app = FastAPI()

# =========================================
# SERVE REACT BUILD FILES
# =========================================

app.mount(
    "/assets",
    StaticFiles(directory="disease-react-ui/dist/assets"),
    name="assets"
)

# =========================================
# CORS
# =========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================
# LOAD MODEL & SCALER
# =========================================

model = pickle.load(open("disease_predictor.pkl", "rb"))

scaler = pickle.load(open("scaler.pkl", "rb"))

# =========================================
# INPUT SCHEMA
# =========================================

class DiseaseData(BaseModel):
    age: float
    bp: float
    sugar: float

# =========================================
# FRONTEND ROUTE
# =========================================

@app.get("/")
def serve_frontend():
    return FileResponse("disease-react-ui/dist/index.html")

# =========================================
# PREDICTION ROUTE
# =========================================

@app.post("/predict")
def predict(data: DiseaseData):

    features = np.array([[
        data.age,
        data.bp,
        data.sugar
    ]])

    # Scale input
    scaled_data = scaler.transform(features)

    # Prediction
    prediction = model.predict(scaled_data)

    # Probability
    probability = model.predict_proba(scaled_data)

    confidence = float(probability[0][1]) * 100

    return {
        "prediction": int(prediction[0]),
        "result":
            "Disease Detected"
            if prediction[0] == 1
            else "No Disease Detected",

        "confidence": round(confidence, 2)
    }