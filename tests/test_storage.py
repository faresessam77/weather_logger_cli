import csv
import json

from weather_logger.storage import Storage

def test_save_json(tmp_path):
    storage = Storage()
    file_path = tmp_path / "test.json"

    data = {
        "city": "Cairo",
        "temperature": 20,
        "humidity": 60,
        "weather": "clear sky"
    }

    storage.save_json(file_path, data)

    assert file_path.exists()

    with open(file_path, "r", encoding="utf-8") as file:
        records = json.load(file)

    assert len(records) == 1
    assert records[0]["city"] == "Cairo"
    assert records[0]["temperature"] == 20

def test_save_csv(tmp_path):
    storage = Storage()
    file_path = tmp_path / "test.csv"

    data = {
        "city": "Cairo",
        "temperature": 20,
        "humidity": 60,
        "weather": "clear sky"
    }

    storage.save_csv(file_path, data)

    assert file_path.exists()

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0]["city"] == "Cairo"
    assert rows[0]["temperature"] == "20"  #CSV = Strings
