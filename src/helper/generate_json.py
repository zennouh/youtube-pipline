import datetime as dt
import json


def create_json(data_dict):
    now = dt.datetime.now()
    day = now.date()
    time = now.time().microsecond


    with open(f"./src/assets/{day}_{time}.json", "w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, indent=4)
