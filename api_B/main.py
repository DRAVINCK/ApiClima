from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()

weather_data = {
    "São Paulo": {"temp": 25, "unit": " Celsius"},
    "Curitiba": {"temp": 19, "unit": " Celsius"}
}

@app.get("/weather/{city}")
def get_weather(city: str):
    city_key = city.replace(" ", " ")
    if city_key not in weather_data:
        return JSONResponse(content={"error": "cidade n encontrada"}, status_code=404)
    
    data = weather_data[city_key]
    return {"city": city.replace(" ", " "), "temp": data["temp"], "unit": data["unit"]}

print("API B is running on port 8001")
