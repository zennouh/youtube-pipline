import requests as req


def channel_id(username: str, api_key, url) -> str:

    params = {
        "key": api_key,
        "part": "contentDetails",
        "forUsername": username.replace("@", ""),
        "maxResults": 1,
    }

    response: req.Response = req.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["pageInfo"]["totalResults"] == 0:
            print("no channels")
        else:
            channel_id = data["items"][0]["id"]
            return channel_id
    else:
        raise Exception("Something wrong: ")
