import controller as clt
import models as md


def Application(username, config: md.Config):
    try:
        # channel_id = clt.channel_id(username, api_key=config.apiKey, url=config.channelUrl)
        # videos_ids = 
        # print(channel_id)
        # clt.get_videos(
        #     "UU7bySWyW6_dUOyopqSQk1Hg",
        #     config.videoUrl,
        #     config.apiKey,
        # )


        clt.get_video_info("mB2ZMTaj5S8", config.videoInfoUrl, config.apiKey)
        # print("hello")
    except Exception as e:
        print(e)
