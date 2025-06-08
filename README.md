# YouTube Transcript Summarizer with GenAI

A Python tool that extracts transcripts from YouTube videos and generates smart, concise summaries using a local LLM. It also includes a lightweight Streamlit-based web interface for ease of use.

---

## Features

- Input a YouTube video URL
- Automatically extracts transcript (if available)
- Summarizes content using a locally run transformer model
- Clean and simple web interface via Streamlit
- Runs offline with GPU acceleration support

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/youtube-genai-summarizer.git
cd youtube-genai-summarizer
python -m venv .venv
.venv\Scripts\activate   

pip install -r requirements.txt

Run a CLI Test
python test_summarizer.py
This script extracts the transcript of a sample video and prints a summary.

Launch the Web Interface
streamlit run interface/app.py
Once running, visit: http://localhost:8501

Project Structure

youtube-genai-summarizer/
├── app/
│   ├── summarizer.py         
│   ├── transcript.py         
│   └── __init__.py
├── interface/
│   └── app.py                
├── test_summarizer.py        
├── requirements.txt
└── README.md
Model Used
facebook/bart-large-cnn
Loaded via Hugging Face transformers library.
Runs locally with no external API required.

```
---

## Notes
Works with videos that have publicly available transcripts.

GPU acceleration is supported automatically by PyTorch.

Handles long transcripts and outputs refined summaries.

---
