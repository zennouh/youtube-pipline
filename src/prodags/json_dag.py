
from datetime import datetime
from airflow.decorators import dag, task
import app 
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


class JsonDag:
    def __init__(self, application: app.Application):
        self.application =application

    @task
    def extract(self):
       return self.application.get_all_videos()

    @task
    def to_json(self, videos):
        self.application.save_in_json(videos)



@dag(
    dag_id="json_dag",
    schedule="0 8 * * *",
    start_date=datetime(2026, 9, 15),
    catchup=False
)

def youtube_json_dag(json_dag):
    # json_dag = JsonDag()
    extracted = json_dag.extract()
    to_json =json_dag.to_json(extracted)

    trigger_stoke_dag = TriggerDagRunOperator(
        task_id="trigger_stoke_dag",
        trigger_dag_id="save_data",
        wait_for_completion=True,
    )

    to_json >> trigger_stoke_dag


youtube_json_dag()