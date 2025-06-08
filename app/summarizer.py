from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_id = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def generate_summary(transcript: str) -> str:
    if not transcript.strip():
        return "Transcript is empty. Cannot summarize."

    # Truncate to avoid token limit errors
    transcript = transcript[:3000]

    summary = summarizer(transcript, max_length=300, min_length=30, do_sample=False)
    return summary[0]["summary_text"]
