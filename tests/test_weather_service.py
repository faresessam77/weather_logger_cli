from weather_logger.weather_service import WeatherService

def test_get_weather_success(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "fake-key")

    class MockResponse:
        status_code = 200

        def json(self):
            return {
                "name": "Cairo",
                "main": {"temp": 25, "humidity": 50},
                "weather": [{"description": "clear sky"}]
            }


    def mock_get(*args ,**kwargs):
        return MockResponse()

    monkeypatch.setattr( "weather_logger.weather_service.requests.get",mock_get)

    service = WeatherService()
    weather = service.get_weather("Cairo")

    assert weather["city"] == "Cairo"
    assert weather["temperature"] == 25
    assert weather["humidity"] == 50
    assert weather["weather"] == "clear sky"