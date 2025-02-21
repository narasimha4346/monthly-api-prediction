from fastapi import FastAPI
import json
import pandas as pd
import random

app = FastAPI()

# Load the JSON data
with open("test_reports.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)  # Convert JSON data to Pandas DataFrame

@app.get("/")
def home():
    return {"message": "Welcome to the AI Prediction API"}

@app.get("/get-sample")
def get_sample():
    """Return a random test report entry"""
    return random.choice(data)

@app.get("/predict-next-month")
def predict_next_month():
    """Simulate next month's prediction using a simple model"""
    predictions = {
        "totalTestsByApplication": int(df["totalTestsByApplication"].mean() * 1.1),
        "storyPassed": int(df["storyPassed"].mean() * 1.1),
        "arPassed": int(df["arPassed"].mean() * 1.1),
        "mrPassed": int(df["mrPassed"].mean() * 1.1),
    }
    return {"predictions": predictions} 
