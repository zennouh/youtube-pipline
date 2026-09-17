from datetime import datetime
from dotenv import load_dotenv
# import src.database as db
from src.database import create_tables


from airflow.decorators import dag, task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from src.app import Application
from src.models import Config
import os

@dag(
    dag_id="json_dag",
    schedule="* 8 * * *",
    start_date=datetime(2026, 9, 15),
    catchup=False,
)
def youtube_json_dag():
    create_tables()
    load_dotenv()
    config = Config.create(
            os.getenv("URL_CHANNEL"),
            os.getenv("URL_VIDEOS"),
            os.getenv("URL_VIDEO_INFO"),
            os.getenv("API_KEY"),
        )

    application = Application("@MrBeast", config)

    @task
    def extract():
        return application.get_all_videos()

    @task
    def to_json(videos):
        application.save_in_json(videos)

    videos = extract()
    json_file = to_json(videos)

    trigger_stoke_dag = TriggerDagRunOperator(
        task_id="trigger_stoke_dag",
        trigger_dag_id="save_data",
        wait_for_completion=True,
    )

    json_file >> trigger_stoke_dag


youtube_json_dag()