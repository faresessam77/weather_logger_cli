import argparse
import logging

from weather_logger.weather_service import WeatherService
from weather_logger.storage import Storage
from weather_logger.logger_config import setup_logger


def main():
    setup_logger()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Weather Data Logger CLI")
    parser.add_argument("city", help="City name")
    args = parser.parse_args()

    try:
        service = WeatherService()
        storage = Storage()

        weather = service.get_weather(args.city)

        logger.info("Weather Report")
        for key, value in weather.items():
            logger.info(f"{key.capitalize():12}: {value}")

        storage.save_json("weather_data.json", weather)
        storage.save_csv("weather_data.csv", weather)

        logger.info("Data saved successfully")

    except Exception:
        logger.exception("Unhandled error")

if __name__ == "__main__":
    main()


