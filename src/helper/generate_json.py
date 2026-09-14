import datetime as dt
import json


def create_json(data_dict):
    now = dt.datetime.now().date()

    with open(f"./src/assets/{now}.json", "w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, indent=4)
