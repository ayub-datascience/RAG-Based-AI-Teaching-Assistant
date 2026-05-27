# 🤖 RAG Based AI Teaching Assistant

An AI-powered Teaching Assistant built using Retrieval-Augmented Generation (RAG), semantic search, vector embeddings, and Large Language Model (LLM).

This project converts educational videos into text, generates embeddings, performs semantic search using cosine similarity, and answers user questions using a local LLM.

---

# ✨ Features

- 🎥 Convert video lectures into audio
- 🎙️ Convert audio into English text using Whisper
- 🧠 Generate embeddings using bge-m3
- 📦 Store and manage vector embeddings using Pandas and Joblib
- 🔍 Semantic search using cosine similarity
- 💬 Context-aware answer generation using LLM
- 💻 Fully local pipeline using Ollama

---

# ⚙️ Project Workflow

## 🎥 Step 1: Video to Audio

Educational videos (.mp4) are converted into audio (.mp3) using ffmpeg.

## 🎙️ Step 2: Audio to Text

Audio files are transcribed using OpenAI Whisper.

- 🗣️ Spoken language: Hindi
- 🌍 Output language: English
- ✂️ Text is stored in chunks with timestamps

## 🧠 Step 3: Embedding Generation

Text chunks are converted into vector embeddings using:

- 🤖 Model: bge-m3
- 💻 Running locally via Ollama API

## 🔍 Step 4: Semantic Search

User query embeddings are compared with stored embeddings using cosine similarity.

Top relevant chunks are retrieved.

## 💬 Step 5: Response Generation

User query and Top Relevant chunks are sent to the LLM as context.

The LLM generates answers based only on retrieved context.

---

# 🛠️ Technologies Used

- 🐍 Python
- 🦙 Ollama
- 🎙️ Whisper
- 🎬 ffmpeg
- 🐼 Pandas
- 🔢 NumPy
- 📊 scikit-learn
- 💾 Joblib

---

# 🤖 Models Used

## 🧠 Embedding Model
- bge-m3

## 💬 LLM
- llama3

## 🎙️ Speech-to-Text Model
- Whisper Base Model

---

# 📁 Folder Structure

```text
RAG Based AI Teaching Assistant/
│
├── 01_video_to_audio.py
├── 02_audio_to_text_in_the_form_of_chunks.py
├── 03_Vector_Embeddings_of_chunked_texts.py
├── 04_Getting_Response_from_LLM.py
│
├── videos/                # Add your own educational video files in this folder
├── audios/                # Generated audio files
├── jsons/                 # Transcribed text chunks
├── Vector_Embeddings.joblib
│

```

---

# 🚀 Setup Instructions

## 1. Install Dependencies

```bash
pip install pandas numpy scikit-learn openai-whisper joblib requests
```

---

## 2. Install ffmpeg

Download and install ffmpeg:

https://ffmpeg.org/download.html

Add ffmpeg to system PATH.

---

## 3. Install Ollama

Download Ollama:

https://ollama.com

Pull required models:

```bash
ollama pull llama3
ollama pull bge-m3
```

---

# ▶️ How to Run

## 🎥 Step 1: Convert Videos to Audio

```bash
python 01_video_to_audio.py
```

---

## 🎙️ Step 2: Convert Audio to Text

```bash
python 02_audio_to_text_in_the_form_of_chunks.py
```

---

## 🧠 Step 3: Create Embeddings

```bash
python 03_Vector_Embeddings_of_chunked_texts.py
```

---

## 💬 Step 4: Run AI Teaching Assistant

```bash
python 04_Getting_Response_from_LLM.py
```

---

# 💡 Example

## ❓ User Question

```text
What are inline and block elements?
```

## 🤖 AI Response

The AI retrieves the most relevant lecture chunks using semantic search and generates an answer using the provided context.

---

# 📌 Important Notes

- 📂 Videos are not uploaded to GitHub.
- ⬇️ Download them separately and place them inside the required folder.
- 🛠️ Create these folders manually before running the scripts:
  - videos
  - audios
  - jsons

---

# 🔮 Future Improvements

- 🌐 Add Streamlit UI
- 🗣️ Add multilingual support
- 🧠 Use vector databases like FAISS or ChromaDB
- 💾 Add chat history memory
- 🎯 Improve retrieval accuracy
- 📄 Add PDF support

---

# 👨‍💻 Author

Ayyub

🎓 Engineering Student
