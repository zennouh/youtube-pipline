import src.helper as hl
from src.database.connection import engine
from src.database.models import Stage, Core
from sqlalchemy import select, func, delete
from sqlalchemy.orm import sessionmaker


def save_in_stage_db(videos):

    Session = sessionmaker(bind=engine)

    with Session() as session:
        total_videos = session.scalar(select(func.count(Stage.video_id)))

        if total_videos != len(videos):
            ids = list(map(lambda v: v["video_id"], videos))

            missed_ids = found_missed_ids_in_stage(ids, session)

            for i in missed_ids:
                stmt = delete(Stage).where(Stage.video_id == i)
                session.execute(stmt)
            session.commit()

        for video in videos:
            session.merge(Stage(**video))

        session.commit()

    print(f"Inserted {len(videos)} videos into stage")


def save_in_core_from_stage():
    Session = sessionmaker(engine)
    with Session() as se:

        stmt = select(Stage)
        videos = se.execute(stmt).scalars()

        total_videos_core = se.scalar(select(func.count(Core.video_id)))
        total_videos_stage = se.scalar(select(func.count(Stage.video_id)))

        if total_videos_core > total_videos_stage:
            stmt_stage = select(Stage.video_id)
            ids_stage = se.scalars(stmt_stage).all()

            stmt_core = select(Core.video_id)
            ids_core = se.scalars(stmt_core).all()

            missed_ids = list(set(ids_core) - set(ids_stage))
            

            for i in missed_ids:
                stmt_delete = delete(Core).where(i == Core.video_id)
                se.execute(stmt_delete)

            se.commit()

        for v in videos:
            video_dict = stage_to_dict(v)
            clv = cleaned_video(video_dict)
            se.merge(Core(**clv))
        se.commit()

    print(f"Inserted videos into core")


def cleaned_video(video):
    clean_serie = hl.clean_data(video)
    return clean_serie


def stage_to_dict(stage: Stage):
    return {
        "video_id": stage.video_id,
        "title": stage.title,
        "published_at": stage.published_at,
        "duration": stage.duration,
        "views": stage.views,
        "likes": stage.likes,
        "comments": stage.comments,
    }


def found_missed_ids_in_stage(ids, session):
    stmt = select(Stage.video_id)
    existing_ids = session.scalars(stmt).all()

    missing_ids = list(set(existing_ids) - set(ids))

    return missing_ids
