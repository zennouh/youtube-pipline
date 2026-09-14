import requests as req
import models as md


# mB2ZMTaj5S8
def get_video_info(video_id, url, api_key):
    params = {
        "part": "snippet,statistics,contentDetails",  # Information groups to fetch
        "id": video_id,  # Your YouTube video ID
        "key": api_key,
    }
    response: req.Response = req.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    video = data["items"][0]


    video_info = {
        "video_id": video.get("id"),
        "title": video.get("snippet", {}).get("title"),
        "published_at": video.get("snippet", {}).get("publishedAt"),
        "duration": video.get("contentDetails", {}).get("duration"),
        "views": int(video.get("statistics", {}).get("viewCount", 0)),
        "likes": int(video.get("statistics", {}).get("likeCount", 0)),
        "comments": int(video.get("statistics", {}).get("commentCount", 0)),
    }


    # video_obj = md.Video(**video_info)
    return video_info
