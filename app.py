import controller as clt


def Application(username, api_key, url):
    channel_id = clt.channel_id(username, api_key=api_key, url=url)
