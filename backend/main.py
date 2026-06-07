from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import numpy as np
import joblib


# =========================
# Load Model Files
# =========================

model = joblib.load("models/crop_model.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


# =========================
# FastAPI App
# =========================

app = FastAPI(
    title="Crop Recommendation API",
    description="Predicts the best crop and second best crop",
    version="1.0"
)

# Allow frontend requests

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# Input Schema
# =========================

class CropInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float


# =========================
# Home Route
# =========================

@app.get("/")
def home():
    return {
        "message": "Crop Recommendation API Running"
    }


# =========================
# Prediction Route
# =========================

@app.post("/predict")
def predict_crop(data: CropInput):

    input_data = np.array([
        [
            data.N,
            data.P,
            data.K,
            data.temperature,
            data.humidity,
            data.ph,
            data.rainfall
        ]
    ])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Get probabilities
    probabilities = model.predict_proba(input_scaled)[0]

    # Top 2 crops
    top2_indices = np.argsort(probabilities)[-2:][::-1]

    best_crop = label_encoder.inverse_transform(
        [top2_indices[0]]
    )[0]

    second_crop = label_encoder.inverse_transform(
        [top2_indices[1]]
    )[0]

    best_probability = round(
        float(probabilities[top2_indices[0]]) * 100,
        2
    )

    second_probability = round(
        float(probabilities[top2_indices[1]]) * 100,
        2
    )
    if second_probability >= 2:
        second_crop_result = second_crop
        second_probability_result = second_probability
    else:
        second_crop_result = "Not Recommended"
        second_probability_result = None

    return {
        "best_crop": best_crop,
        "best_crop_probability": best_probability,

        "second_crop": second_crop_result,
        "second_crop_probability": second_probability_result
    }