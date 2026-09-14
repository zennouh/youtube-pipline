import os
from dotenv import load_dotenv
import app


def main(username):
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    URL = os.getenv("URL_CHANNEL")

    app.Application(username, api_key=API_KEY, url=URL)


main("@MrBeast")
