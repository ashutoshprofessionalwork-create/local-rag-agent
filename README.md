# 🎙️ SARA - Local Voice AI Assistant

A privacy-focused, offline local AI desktop assistant powered by **Llama 3.2 (1B)** via Ollama. It listens for its wake word, executes system tasks, and talks back in real time—with zero cloud dependencies.

---

## ⚡ Key Features

- **🗣️ Custom Wake Word & Voice Engine:** Listens locally and responds with realistic Text-to-Speech (TTS).
- **🔒 100% Offline & Private:** Runs entirely on your hardware using Ollama (`llama3.2:1b`). No API keys, no data leaks.
- **💻 Desktop OS Automation:** Executes native system tasks (app launching, volume/media controls, file management, automation scripts).
- **⚡ Ultralight & Fast:** Optimized for low latency and minimal RAM usage.

---

## 🛠️ Architecture & Tech Stack

| Layer | Tool / Tech |
| :--- | :--- |
| **LLM Brain** | Ollama (`llama3.2:1b`) |
| **Speech-to-Text (STT)** | Faster-Whisper / SpeechRecognition |
| **Text-to-Speech (TTS)** | pyttsx3 / Edge-TTS |
| **OS Automation** | Python (`os`, `subprocess`, `pyautogui`) |

---

## 🚀 Quickstart

### 1. Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed and running

```bash
ollama pull llama3.2:1b
