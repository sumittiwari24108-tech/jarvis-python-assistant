# Jarvis – AI-Powered Desktop Voice Assistant

Jarvis is an intelligent, voice-controlled desktop assistant built with Python. It automates daily operating system tasks, executes web searches, manages audio, and seamlessly falls back on Google's Gemini API for natural conversational interactions.

---

## Key Features

- **Wake Word Detection:** Continuously listens in the background for the "Jarvis" trigger word.
- **System Automation:** Controls master volume via Windows APIs (`pycaw`), captures screenshots (`pyautogui`), checks battery percentage (`psutil`), and handles clipboard operations (`pyperclip`).
- **Application Launcher:** Opens native system apps (VS Code, Notepad, Command Prompt, Calculator) and system settings via subprocesses.
- **Web & Media Control:** Executes Google and YouTube queries automatically, reads live top news headlines, and streams music tracks from a custom library dictionary.
- **Generative AI Integration:** Uses Google's `gemini-2.5-flash` model (`google-genai`) to answer complex queries, governed by custom system instructions and length constraints.
- **Asynchronous Audio Output:** Multi-threaded speech playback to ensure the assistant remains responsive without freezing the main application loop.

---

## Tech Stack

- **Language:** Python 3.x
- **AI Engine:** Google Gemini API (`google-genai`)
- **Speech Recognition:** `SpeechRecognition`
- **Text-to-Speech (TTS):** `gTTS`, `pyttsx3`, `pygame`
- **System Automation:** `pycaw`, `psutil`, `pyautogui`, `comtypes`, `pyperclip`
- **Utilities:** `python-dotenv`, `requests`

---

## Project Structure

```text
├── main.py              # Main execution loop and voice command routing
├── client.py            # Gemini API integration and system prompt configuration
├── music_library.py     # Track mapping dictionary for web/media playback
├── .env                 # API keys (hidden via .gitignore)     
├── .gitignore           # Excludes sensitive keys and temporary files
├── requirements.txt     # Clean project dependencies
└── README.md            # Project documentation

## Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/sumittiwari24108-tech/jarvis-python-assistant.git
cd jarvis-python-assistant