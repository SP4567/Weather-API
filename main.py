import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel
from dicttoxml import dicttoxml

app = FastAPI(title="Weather API using RapidAPI")

RAPID_API_KEY = "69ecb9aaefmshdc348cfda885ac1p18b9d7jsn8a16d0072e1f"
RAPID_API_HOST = "weatherapi-com.p.rapidapi.com"
WEATHER_URL = "https://weatherapi-com.p.rapidapi.com/current.json"

HEADERS = {
    "x-rapidapi-key": RAPID_API_KEY,
    "x-rapidapi-host": RAPID_API_HOST,
}

class WeatherRequest(BaseModel):
    """Request body schema for weather endpoint."""

    city: str
    output_format: str  # json | xml

@app.get("/")
def home() -> dict:
    """Health check endpoint."""
    return {
        "message": "Weather API is running",
        "usage": "POST /weather with city and output_format",
    }

@app.post("/weather")
def get_weather(data: WeatherRequest):
    """Fetch current weather details for a city."""
    params = {"q": data.city}

    try:
        response = requests.get(
            WEATHER_URL,
            headers=HEADERS,
            params=params,
            timeout=10,
        )
    except requests.exceptions.RequestException as exc:
        raise HTTPException(
            status_code=500,
            detail="Weather service unavailable",
        ) from exc

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found")

    weather_data = response.json()

    result = {
        "city": weather_data["location"]["name"],
        "temperature_celsius": weather_data["current"]["temp_c"],
        "condition": weather_data["current"]["condition"]["text"],
        "latitude": weather_data["location"]["lat"],
        "longitude": weather_data["location"]["lon"],
    }

    if data.output_format.lower() == "json":
        return JSONResponse(content=result)

    if data.output_format.lower() == "xml":
        xml_data = dicttoxml(
            result,
            custom_root="weather",
            attr_type=False,
        )
        return Response(
            content=xml_data,
            media_type="application/xml",
        )

    raise HTTPException(
        status_code=400,
        detail="output_format must be 'json' or 'xml'",
    )
