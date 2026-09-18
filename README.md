# Jarvis – AI-Powered Desktop Voice Assistant

Jarvis is an AI-powered, voice-controlled desktop assistant built with Python. It can automate common Windows tasks, control system volume, open applications and folders, perform web searches, provide news updates, play music, manage notes and clipboard content, and use Google's Gemini API for conversational responses.

## Key Features

* **Wake Word Detection:** Listens for the **"Jarvis"** wake word before accepting voice commands.
* **System Automation:** Controls master volume, checks battery percentage, takes screenshots, and manages clipboard content.
* **Application Launcher:** Opens VS Code, Calculator, Notepad, Paint, Command Prompt, File Explorer, and Windows Settings.
* **Folder Access:** Opens common folders such as Downloads, Documents, Pictures, Music, and Desktop.
* **Web Search:** Searches Google and YouTube using voice commands.
* **Websites:** Quickly opens Google, YouTube, LinkedIn, Instagram, GitHub, and ChatGPT.
* **News Updates:** Fetches live top headlines from India using NewsAPI.
* **Music Playback:** Streams music tracks from a custom library dictionary.
* **Notes:** Saves and reads simple text notes using voice commands.
* **Generative AI:** Uses Google's Gemini API for conversational responses when a command does not match a predefined action.
* **Text Mode:** Supports text-based interaction using the `--text` command-line option.
* **Voice Responses:** Uses text-to-speech to respond to the user.

## Tech Stack

* **Language:** Python 3.x
* **AI:** Google Gemini API (`google-genai`)
* **Speech Recognition:** `SpeechRecognition`
* **Text-to-Speech:** `gTTS`, `pyttsx3`
* **Audio Playback:** `pygame`
* **System Automation:** `pycaw`, `psutil`, `pyautogui`, `comtypes`, `pyperclip`
* **Web Requests:** `requests`
* **Environment Variables:** `python-dotenv`

## Project Structure

```text
├── main.py              # Main execution loop and voice command processing
├── client.py            # Gemini API integration
├── music_library.py     # Music track mapping dictionary
├── .env.example         # Example environment variables
├── .gitignore           # Excludes sensitive and temporary files
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

> **Note:** The actual `.env` file is not included in the repository because it contains API keys.

## Requirements

Before running Jarvis, make sure you have:

* Windows 10 or Windows 11
* Python 3.x
* A working microphone
* An internet connection
* A Google Gemini API key
* A NewsAPI key

> **Note:** Jarvis currently uses Windows-specific features such as `pycaw`, Windows system applications, and Windows audio APIs.

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sumittiwari24108-tech/jarvis-python-assistant.git
cd jarvis-python-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_newsapi_key
```

> **Security:** Never upload or share your `.env` file or your API keys publicly.

### 5. Run Jarvis

For voice mode:

```bash
python main.py
```

For text mode:

```bash
python main.py --text
```

Once started, Jarvis will listen for the **"Jarvis"** wake word and respond to supported commands.

## Example Commands

You can try commands such as:

* "Jarvis, open VS Code"
* "Jarvis, open Calculator"
* "Jarvis, open Notepad"
* "Jarvis, open Paint"
* "Jarvis, open Downloads"
* "Jarvis, open Documents"
* "Jarvis, increase volume"
* "Jarvis, decrease volume"
* "Jarvis, mute"
* "Jarvis, unmute"
* "Jarvis, what's the time?"
* "Jarvis, what's the date?"
* "Jarvis, what's my battery percentage?"
* "Jarvis, take a screenshot"
* "Jarvis, search Python tutorials"
* "Jarvis, search YouTube music"
* "Jarvis, open GitHub"
* "Jarvis, what's in the news?"
* "Jarvis, play [song name]"
* "Jarvis, write note [your note]"
* "Jarvis, read notes"
* "Jarvis, read clipboard"

The available commands depend on the functionality implemented in the project.

## How It Works

```text
User speaks
     ↓
Microphone
     ↓
Speech Recognition
     ↓
Wake Word Detection
     ↓
Command Processing
     ↓
 ┌─────────────────────────┐
 │                         │
 ▼                         ▼
Predefined Commands     Gemini AI
 │                         │
 └────────────┬────────────┘
              ↓
       Generate Response
              ↓
       Text-to-Speech
              ↓
        Audio Response
```

Jarvis first listens for the **"Jarvis"** wake word. After detecting it, the assistant listens for a command and processes it.

If the command matches a predefined function, Jarvis performs the requested action. Otherwise, the query is sent to Gemini for a conversational response.

## Troubleshooting

### Gemini is not responding

Check that:

* Your `.env` file exists in the project folder.
* `GEMINI_API_KEY` is correct.
* Your internet connection is working.
* All dependencies are installed.

### News is not working

Check that:

* `NEWS_API_KEY` is correctly added to `.env`.
* Your internet connection is working.
* Your NewsAPI key is valid.

### Microphone is not working

Check that:

* Your microphone is connected and working.
* Windows microphone permissions are enabled.
* Python is using the correct microphone device.

### Jarvis is not speaking

Make sure:

* Your system audio is working.
* `gTTS`, `pygame`, and `pyttsx3` are installed correctly.
* Your internet connection is available for `gTTS`.

## Security

Keep your API keys private.

Make sure `.env` is included in `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

Never commit API keys directly into your Python files or GitHub repository.

## Future Improvements

Some possible improvements for future versions include:

* Better wake-word detection
* More system automation commands
* Improved natural-language command understanding
* More application integrations
* Better error handling
* Graphical user interface (GUI)
* Custom voice responses
* More advanced Gemini-powered interactions
* Additional APIs and online services

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


