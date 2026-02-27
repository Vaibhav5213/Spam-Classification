from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI(title="Spam Classification API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../models/spam_classifier_model.pkl")
VECT_PATH = os.path.join(BASE_DIR, "../models/vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECT_PATH)

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_spam(request: TextRequest):
    vectorized_text = vectorizer.transform([request.text])
    prediction = model.predict(vectorized_text)[0]
    return {
        "text": request.text,
        "is_spam": bool(prediction == "spam") 
    }
