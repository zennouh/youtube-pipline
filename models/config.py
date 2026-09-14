class Config:
    def __init__(self, channelUrl, videoUrl, videoInfoUrl, apiKey):
        self.channelUrl = channelUrl
        self.videoUrl = videoUrl
        self.videoInfoUrl = videoInfoUrl
        self.apiKey = apiKey

    @classmethod
    def create(cls, channelUrl, videoUrl, videoInfoUrl, apiKey):
        return cls(channelUrl, videoUrl, videoInfoUrl, apiKey)
