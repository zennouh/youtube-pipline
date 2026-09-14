

from dataclasses import dataclass


@dataclass
class Video:
    video_id: str
    title: str
    published_at: str
    duration: str
    views: int
    likes: int
    comments: int
