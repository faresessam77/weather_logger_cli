import requests
import os

class WeatherService:
    base_url =  "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENWEATHER_API_KEY not set")

    def get_weather(self, city : str) -> dict :
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        if response.status_code != 200:
            raise Exception(data.get("message", "API Error"))

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }