from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

def extractVideoID(URL: str) -> str:
    parsedURL = urlparse(URL)
    queryParams = parse_qs(parsedURL.query)

    if "v" in queryParams:
        return queryParams["v"][0]
    else:
        raise ValueError("Invalid or unsupported Youtube URL fromat.")

def getTranscriptText(videoURL: str) -> str:
    videoID = extractVideoID(videoURL)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoID)
        Text = " ".join([entry["text"] for entry in transcript])
        return Text
    except (TranscriptsDisabled, NoTranscriptFound):
        return "No transcript available for this video."
    except VideoUnavailable:
        return "The video is unavailable."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
