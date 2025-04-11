from fastapi import FastAPI
import requests

app = FastAPI()

API_URL = "http://localhost:8001/weather"

@app.get("/recommendation/{city}")
def get_recommendation(city: str):
    response = requests.get(f"{API_URL}/{city}")

    if response.status_code != 200:
        return {"error": "N foi possivel obter dados do clima"}

    data = response.json()
    temp = data["temp"]
    recommendation = ""

    if temp > 30:
        recommendation = "sugiro hidratação e protetor solar"
    elif 15 < temp <= 30:
        recommendation = "O clima está agradável"
    else:
        recommendation = "Ta frio, use um casaco"

    return {
        "city": data["city"],
        "temp": temp,
        "unit": data["unit"],
        "recommendation": recommendation
    }
