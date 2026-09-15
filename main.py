import os
from dotenv import load_dotenv
import src.app as app
import src.models as md
import src.database as db


def main(username):
    db.create_tables()
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    CHANNEL_URL = os.getenv("URL_CHANNEL")
    Videos_URL = os.getenv("URL_VIDEOS")
    videoInfoUrl = os.getenv("URL_VIDEO_INFO")

    config = md.Config.create(CHANNEL_URL, Videos_URL, videoInfoUrl, API_KEY)

    application = app.Application()
    application.start(username, config)


main("@MrBeast")
