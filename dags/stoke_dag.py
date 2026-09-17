from datetime import datetime
import json
import glob

from pathlib import Path
from airflow.decorators import dag, task


@dag(
    dag_id="save_data",
    schedule=None,
    start_date=datetime(2026, 9, 15),
    catchup=False,
)
def stoke_videos():

    @task
    def read_json():
        path = Path(f"/opt/airflow/src/assets")
        json_files = list(path.glob("*.json"))
        jfile = max(json_files, key=lambda file: file.stat().st_mtime)
        with jfile.open(encoding="utf-8") as file:
            videos = json.load(file)
        return videos
    

    @task
    def save_in_stage(videos):
        import src.helper as hl
        hl.save_in_stage_db(videos)

    @task
    def save_in_core():
        import src.helper as hl
        hl.save_in_core_from_stage()

    videos = read_json()
    stage = save_in_stage(videos)
    core = save_in_core()

    stage >> core


stoke_videos()