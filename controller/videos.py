import requests as req


def get_videos(playlist_id, url, api_key):
    params = {
        "key": api_key,
        "part": "snippet,contentDetails",
        "playlistId": playlist_id,
        "order": "date",
        "type": "video",
        "maxResults": 10,
    }
    response: req.Response = req.get(url, params=params)
    if response.status_code != 200:
        raise Exception("Something worng: ", response.status_code)

    data = response.json()
    video_id = data["items"][0]["contentDetails"]["videoId"]
    return video_id
