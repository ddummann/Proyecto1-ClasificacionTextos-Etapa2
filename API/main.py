from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text: str
    

class PredictionOut(BaseModel):
    prediction: str

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/predict", response_model=PredictionOut, status_code=200)
def predict(text_in: TextIn):
    result = predict_pipeline(text_in.text)
    return {"prediction": result, "model_version": model_version}
    