# model/fastapi_app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# 모델 로드
model_sk = joblib.load('sk_preprocessed_data_fin.pkl')
model_skhynix = joblib.load('sk_preprocessed_data.pkl')

class PredictionRequest(BaseModel):
    features: list

@app.post("/predict_model_sk")
async def predict_model_sk(request: PredictionRequest):
    prediction = model_sk.predict([request.features])
    return {"prediction": prediction[0]}

@app.post("/predict_model_skhynix")
async def predict_model_skhynix(request: PredictionRequest):
    prediction = model_skhynix.predict([request.features])
    return {"prediction": prediction[0]}
