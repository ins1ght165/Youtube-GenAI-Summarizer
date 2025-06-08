from app.transcript import get_transcript_text

# Example YouTube video with captions
videoURL = "https://www.youtube.com/watch?v=LKBiHbU63UE"

result = get_transcript_text(videoURL)
print(result)
