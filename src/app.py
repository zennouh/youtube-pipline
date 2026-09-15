import src.controller as clt
import src.models as md
import traceback
import src.helper as hl
from pathlib import Path
import glob
import json
import datetime as dt


class Application:

    def read_from_json(self):
        json_name = dt.datetime.now().date()
        path = Path(f"./src/assets/{json_name}.json")
        with path.open(encoding="utf-8") as file:
            videos = json.load(file)
        return videos

    def save_in_stage(self, vs):
        hl.save_in_stage_db(vs)
        return True

    def save_in_core(self):
        hl.save_in_core_from_stage()
        pass

    def save_in_json(self, videos_list):
        hl.create_json(videos_list)

    def start(self, username, config: md.Config):
        json_name = dt.datetime.now().date()
        path = Path(f"./src/assets/{json_name}.json")
        if path.exists:
            videos = self.read_from_json()
            self.save_in_stage(videos)
            self.save_in_core()
        else:
            self.get_all_videos(username, config)
            videos = self.read_from_json()
            self.save_in_json(videos)
            self.save_in_stage(videos)
            self.save_in_core()

    def get_all_videos(self, username, config: md.Config):
        try:
            videos_list = []
            play_list_id = clt.channel_id(
                username, api_key=config.apiKey, url=config.channelUrl
            )
            ids = clt.get_videos_ids(
                play_list_id,
                config.videoUrl,
                config.apiKey,
            )
            print("Start loading informations")
            for id in ids:
                try:
                    video = clt.get_video_info(id, config.videoInfoUrl, config.apiKey)
                    videos_list.append(video)

                    total = len(ids)
                    current = len(videos_list)
                    bar_length = 30
                    progress = int((current / total) * bar_length)
                    print(
                        f"[{'-' * progress}{' ' * (bar_length - progress)}] {current}/{total}",
                        end="\r",
                    )
                except:
                    traceback.print_exc()
                    continue
            # hl.create_json(videos_list)
            print("Done")
            # return videos_list

        except Exception as e:
            print("error is: ", e)
