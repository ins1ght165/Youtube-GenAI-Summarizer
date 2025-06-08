from app.summarizer import generate_summary
from app.transcript import get_transcript_text
import traceback

def test_summary():
    url = "https://www.youtube.com/watch?v=LKBiHbU63UE"  
    try:
        transcript = get_transcript_text(url)
        
        if "An unexpected error occurred" in transcript or len(transcript.strip()) < 100:
            print("Transcript is too short or failed to fetch. Try a different video.")
            return

        print("\n--- TRANSCRIPT SAMPLE ---")
        print(transcript[:500])

        summary = generate_summary(transcript)
        print("\n--- SUMMARY ---")
        print(summary)
    except Exception as e:    
        traceback.print_exc()
        raise


if __name__ == "__main__":
    test_summary()
