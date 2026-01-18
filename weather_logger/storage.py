import  json
import csv
from datetime import datetime
from typing import Dict

class Storage:

    def _timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save_json(self, filename : str, data : Dict) -> None:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                records = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            records = []

        record = data.copy()
        record["datetime"] = self._timestamp()
        records.append(record)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4, ensure_ascii=False)


    def save_csv(self, filename: str, data: Dict) -> None:

        record = data.copy()
        record["datetime"] = self._timestamp()

        file_exists = False
        try:
            with open(filename, "r", encoding="utf-8"):
                file_exists = True
        except FileNotFoundError:
            pass

        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=record.keys())

            if not file_exists:
                writer.writeheader()
            writer.writerow(record)
