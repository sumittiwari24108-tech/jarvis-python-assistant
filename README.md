# Jarvis – Desktop Voice Assistant

An intelligent voice-controlled desktop assistant built with Python and integrated with Google's Gemini API.

## Features
- **Wake Word Detection:** Responds to the "Jarvis" wake word.
- **System Control:** Manage Windows volume, take screenshots, check battery status, and access clipboard.
- **Application Automation:** Open apps like VS Code, Calculator, Notepad, CMD, and system settings.
- **Web & API Integration:** Perform Google/YouTube searches, read top headlines, and stream music.
- **Generative AI Fallback:** Powered by `gemini-2.5-flash` to handle conversational queries naturally.

## Tech Stack
- **Language:** Python
- **AI Model:** Google Gemini API (`google-genai`)
- **Speech Recognition:** `SpeechRecognition`
- **Audio Output:** `gTTS`, `pygame`, `pyttsx3`
- **System APIs:** `pycaw`, `psutil`, `pyautogui`, `subprocess`

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME