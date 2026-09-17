
from datetime import datetime
from airflow.decorators import dag, task
import app 




class StokeDag: 

    def __init__(self, application: app.Application):
        self.application = application

    @task    
    def read_json(self)-> list:
        return self.application.read_from_json()

    @task
    def save_in_stage(self, videos):
        self.application.save_in_stage(videos)

    @task
    def save_in_core(self):
        self.application.save_in_core()


@dag(
        dag_id= "save_data",
        schedule=None,
        start_date=datetime(2026, 9, 15),
        catchup=False,
)
def stoke_videos(st):
    # st = StokeDag()
    videos = st.read_json()
    stage = st.save_in_stage(videos)
    core = st.save_in_core()
    stage >> core


stoke_videos()