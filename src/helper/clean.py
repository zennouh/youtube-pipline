import pandas as pd


def clean_data(data):
    df: pd.DataFrame = pd.DataFrame([data])
    df["video_id"] = df["video_id"].str.strip()
    df["title"] = df["title"].str.strip()
    df["published_at"] = pd.to_datetime(df["published_at"])
    df["duration"] = df["duration"].apply(correct_duration)

    df["views"] = pd.to_numeric(df["views"], errors="coerce")
    df["likes"] = pd.to_numeric(df["likes"], errors="coerce")
    df["comments"] = pd.to_numeric(df["comments"], errors="coerce")
    return df.to_dict(orient="records")[0]


def correct_duration(dur: str):
    dur = dur.replace("PT", "")
    seconds = 0
    if dur.find("H") != -1:
        hours = int(dur.split("H")[0])
        seconds = hours * 60 * 60
        dur = dur.replace(f"{hours}H", "")
    if dur.find("M") != -1:
        minute = int(dur.split("M")[0])
        seconds += minute * 60
        dur = dur.replace(f"{minute}M", "")
    if dur.find("S") != -1:
        seconds += int(dur.replace("S", ""))
    return seconds
