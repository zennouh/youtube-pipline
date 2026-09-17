import src.helper as hl
import datetime as dt


# python -m pytest tests/clean_test.py
def test_clean_data():
    test_data = {
        "video_id": "Qtl8lJwbd4g",
        "title": "Escape 100 Cops, Win $500,000",
        "published_at": "2026-08-22T16:00:05Z",
        "duration": "PT20M29S",
        "views": "105996816",
        "likes": "2030512",
        "comments": "92517",
    }

    expected_data = {
        "video_id": "Qtl8lJwbd4g",
        "title": "Escape 100 Cops, Win $500,000",
        "published_at": dt.datetime.fromisoformat("2026-08-22T16:00:05Z"),
        "duration": 1229,
        "views": 105996816,
        "likes": 2030512,
        "comments": 92517,
    }

    cleaned_data = hl.clean_data(test_data)
    print("cleaned_data: ", cleaned_data)

    assert cleaned_data == expected_data