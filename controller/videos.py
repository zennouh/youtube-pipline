import requests as req


def get_videos_ids(playlist_id, url, api_key) -> list[str]:
    vidoes_ids = []
    token = None
    while True:
        params = {
            "key": api_key,
            "part": "snippet,contentDetails",
            "playlistId": playlist_id,
            "maxResults": 50,
        }
        if token:
            params["pageToken"] = token

        response: req.Response = req.get(url, params=params)
        if response.status_code != 200:
            raise Exception("Something worng: ", response.status_code)

        data = response.json()
        vidoes_ids.extend([i["contentDetails"]["videoId"] for i in data["items"]])
        token = data.get("nextPageToken")
        if not token:
            break

    return vidoes_ids
