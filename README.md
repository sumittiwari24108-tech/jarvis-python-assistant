# Jarvis – AI-Powered Desktop Voice Assistant

Jarvis is an AI-powered, voice-controlled desktop assistant built with Python. It can automate common operating system tasks, perform web searches, control audio, open applications, provide news updates, play music, and use Google's Gemini API for natural conversational interactions.

---

## Key Features

* **Wake Word Detection:** Continuously listens in the background for the "Jarvis" trigger word.
* **System Automation:** Controls master volume using Windows APIs (`pycaw`), captures screenshots (`pyautogui`), checks battery percentage (`psutil`), and handles clipboard operations (`pyperclip`).
* **Application Launcher:** Opens native system apps such as VS Code, Notepad, Command Prompt, and Calculator, along with system settings.
* **Web & Media Control:** Executes Google and YouTube queries automatically, reads live top news headlines, and streams music tracks from a custom library dictionary.
* **Generative AI Integration:** Uses Google's `gemini-2.5-flash` model through the `google-genai` SDK to answer complex queries and provide conversational responses.
* **Asynchronous Audio Output:** Uses multi-threaded speech playback to keep the assistant responsive without freezing the main application loop.

---

## Tech Stack

* **Language:** Python 3.x
* **AI Engine:** Google Gemini API (`google-genai`)
* **Speech Recognition:** `SpeechRecognition`
* **Text-to-Speech (TTS):** `gTTS`, `pyttsx3`, `pygame`
* **System Automation:** `pycaw`, `psutil`, `pyautogui`, `comtypes`, `pyperclip`
* **Utilities:** `python-dotenv`, `requests`

---

## Project Structure

```text
├── main.py              # Main execution loop and voice command routing
├── client.py            # Gemini API integration and system prompt configuration
├── music_library.py     # Track mapping dictionary for web/media playback
├── .env.example         # Example environment variables
├── .gitignore           # Excludes sensitive keys and temporary files
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

> **Note:** The actual `.env` file is not included in the repository because it contains your API key.

---

## Requirements

Before running Jarvis, make sure you have:

* Windows 10 or Windows 11
* Python 3.x
* A working microphone
* An internet connection
* A Google Gemini API key

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sumittiwari24108-tech/jarvis-python-assistant.git
cd jarvis-python-assistant
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

> **Note:** Jarvis currently uses Windows-specific features such as `pycaw` and Windows system applications.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> **Security:** Never upload or share your `.env` file or your Gemini API key publicly.

### 5. Run the Assistant

```bash
python main.py
```

Once started, Jarvis will listen for the **"Jarvis"** wake word and respond to supported voice commands.

---

## Example Commands

Some example commands you can try:

* "Jarvis, open VS Code"
* "Jarvis, open Calculator"
* "Jarvis, take a screenshot"
* "Jarvis, increase the volume"
* "Jarvis, what's my battery percentage?"
* "Jarvis, search Google for Python tutorials"
* "Jarvis, search YouTube for music"
* "Jarvis, what's in the news?"
* "Jarvis, play sapphire"

The available commands depend on the functionality implemented in the project.

---

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
 ┌───────────────────────┐
 │                       │
 ▼                       ▼
System / Web Commands   Gemini AI
 │                       │
 └───────────┬───────────┘
             ↓
       Generate Response
             ↓
        Text-to-Speech
             ↓
        Audio Response
```

Jarvis first listens for the wake word **"Jarvis"**. After detecting it, the assistant processes the user's voice command and either performs a predefined action or sends the query to Gemini for a conversational response.

---

## Troubleshooting

### Gemini API is not responding

Make sure:

* Your `.env` file exists in the project folder.
* The `GEMINI_API_KEY` is entered correctly.
* Your internet connection is working.
* The required dependencies are installed.

### Microphone is not working

Check that:

* Your microphone is connected and working.
* Windows has microphone access enabled.
* Python is using the correct input device.

### Jarvis is not speaking

Make sure your system audio is working and the required audio libraries have been installed correctly.

---

## Security

Keep your Gemini API key private.

Do not commit your `.env` file to GitHub. Make sure your `.gitignore` contains:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

## Future Improvements

Some possible improvements for future versions include:

* Better wake-word detection
* More system automation commands
* Improved natural-language command understanding
* More application integrations
* Better error handling
* A graphical user interface (GUI)
* Custom voice responses
* More advanced Gemini-powered interactions
