import src.controller as clt
import src.models as md
import traceback
import src.helper as hl
from pathlib import Path
import glob


class Application:

    def handle_json_file(self):
        print("in file")

    def start(self, username, config: md.Config):
        if any(glob.iglob("./src/assets/*.json")):
            self.handle_json_file()
            return
        else:
            # self.get_all_videos(username, config)
            self.handle_json_file()

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
            hl.create_json(videos_list)
            print("Done")

        except Exception as e:
            print("error is: ", e)
