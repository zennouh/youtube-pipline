from sqlalchemy import Column, String, BigInteger, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Stage(Base):
    __tablename__ = "stage"

    video_id = Column(String(20), primary_key=True)
    title = Column(String(255))
    published_at = Column(String(30))
    duration = Column(String(20))
    views = Column(BigInteger)
    likes = Column(BigInteger)
    comments = Column(BigInteger)

class Core(Base):
    __tablename__ = "core"

    video_id = Column(String(20), primary_key=True)
    title = Column(String(255))
    published_at = Column(DateTime(timezone=True))
    duration = Column(Integer)
    views = Column(BigInteger)
    likes = Column(BigInteger)
    comments = Column(BigInteger)