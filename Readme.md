# RAG-Based AI Teaching Assistant

An intelligent lecture search and question-answering system that helps students quickly find relevant content from recorded lectures without re-watching entire videos.

## 🎯 Overview

Students spend hours re-watching lecture videos to find specific topics. This project builds a fully local RAG pipeline that enables instant, timestamp-accurate retrieval of lecture content with zero cloud dependency.

## ✨ Key Features

- **Audio Extraction**: Extracts audio from lecture videos using ffmpeg
- **Accurate Transcription**: OpenAI Whisper (large-v2) for high-quality speech-to-text
- **Time-Aligned Segments**: JSON-formatted transcripts with precise timestamps
- **Local Embeddings**: Uses Ollama's bge-m3 for completely offline operation
- **Semantic Search**: Cosine similarity for finding relevant lecture moments
- **LLM-Powered Answers**: Llama 3.2 via Ollama for context-aware responses
- **No Data Leaving Device**: Fully local pipeline—no cloud APIs or data transmission

## 🛠️ Tech Stack

- **Language**: Python
- **Audio Processing**: ffmpeg
- **Speech-to-Text**: OpenAI Whisper (large-v2)
- **Embeddings**: Ollama (bge-m3)
- **LLM**: Llama 3.2 (Ollama)
- **Search**: Cosine Similarity
- **Output Format**: JSON with timestamps

## 📋 System Architecture

1. **Video Input**: Accepts lecture recordings
2. **Audio Extraction**: ffmpeg extracts audio streams
3. **Transcription**: Whisper converts speech to text
4. **Chunking**: Transcripts split into time-aligned segments (JSON format)
5. **Embedding Generation**: bge-m3 creates vector representations
6. **Semantic Retrieval**: Cosine similarity finds relevant chunks
7. **Response Generation**: Llama 3.2 generates context-aware answers with video timestamp

## 🚀 Results

- **Fully local RAG pipeline** with no cloud dependencies
- **Exact video and timestamp retrieval** for any queried topic
- **Zero data privacy concerns**—all processing happens locally
- **Fast inference** using Ollama's optimized models

## 🔧 Installation

```bash
# Install dependencies
pip install openai-whisper ollama

# Install Ollama
# Download from https://ollama.ai

# Pull required models
ollama pull llama2
ollama pull bge-m3

# Install ffmpeg
# macOS: brew install ffmpeg
# Ubuntu: sudo apt-get install ffmpeg
# Windows: Download from https://ffmpeg.org/download.html
```

## 📖 Usage

```python
import ffmpeg
import whisper
from ollama import Client
import json

# Extract audio
ffmpeg.input("lecture.mp4").audio.output("lecture.wav").run()

# Transcribe
model = whisper.load_model("large-v2")
result = model.transcribe("lecture.wav")

# Create time-aligned segments
segments = [
    {"timestamp": item["start"], "text": item["text"]}
    for item in result["segments"]
]
with open("transcript.json", "w") as f:
    json.dump(segments, f)

# Embed and search
client = Client()
query = "What is quantum computing?"
# Generate embedding for query
# Find similar segments using cosine similarity
# Generate answer with Llama 3.2
```

## 📊 Pipeline Benefits

- **Speed**: Instant retrieval vs. hours of re-watching
- **Accuracy**: Direct timestamps for lecture moments
- **Privacy**: No data sent to cloud services
- **Cost**: No API fees for embeddings or LLM inference
- **Accessibility**: Works offline after initial setup

## 🎓 Use Cases

- Student lecture review and study
- Teaching assistant support
- Lecture content indexing
- Educational video management
- Accessible learning for students with different needs


## 🔗 Connect

- GitHub: [codewithjaywardhan](https://github.com/codewithjaywardhan)
- LinkedIn: [jaywardhanpagar](https://linkedin.com/in/jaywardhanpagar)
