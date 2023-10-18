from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse as urlparse

import json


def video_id(value):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse.urlparse(value)
    if query.hostname == "youtu.be":
        return query.path[1:]
    if query.hostname in ("www.youtube.com", "youtube.com"):
        if query.path == "/watch":
            p = urlparse.parse_qs(query.query)
            return p["v"][0]
        if query.path[:7] == "/embed/":
            return query.path.split("/")[2]
        if query.path[:3] == "/v/":
            return query.path.split("/")[2]
    # fail?
    return None


def get_transcript(url):
    get_video_id = video_id(url)
    raw_transcript = YouTubeTranscriptApi.get_transcript(
        get_video_id, languages=["id", "en"]
    )
    cooked_transcript = ""

    for text in raw_transcript:
        cooked_transcript += text["text"] + "\n"
    return cooked_transcript
