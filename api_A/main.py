from fastapi import FastAPI
import requests

app = FastAPI()


API_URL = "http://api_b:8001/weather"

@app.get("/recommendation/{city}")
def get_recommendation(city: str):
    response = requests.get(f"{API_URL}/{city}")

    if response.status_code != 200:
        return {"error": "Não foi possível obter dados do clima"}

    data = response.json()
    temp = data["temp"]
    
    if temp > 30:
        recommendation = "Sugiro hidratação e protetor solar"
    elif 15 < temp <= 30:
        recommendation = "O clima está agradável"
    else:
        recommendation = "Está frio, use um casaco"

    return {
        "city": data["city"],
        "temp": temp,
        "unit": data["unit"],
        "recommendation": recommendation
    }
