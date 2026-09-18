import speech_recognition as sr
import webbrowser
import pyttsx3 
import time 
import music_library
import requests
from client import ask_gemini 
import pygame
from gtts import gTTS
import os
from dotenv import load_dotenv
import subprocess
import datetime
import psutil
import pyautogui
from pathlib import Path
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from urllib.parse import quote
import json
import pyperclip 
import sys

# Config and Initialization
load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")
JARVIS_PATH = r"D:\IITM BS\code\Mega Project 1-Jarvis"

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 1.3
recognizer.phrase_threshold = 0.2
recognizer.non_speaking_duration = 0.8

engine = pyttsx3.init()
pygame.mixer.init()


def speak_old(text):
    print("Jarvis:", text)
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    # engine.stop()

# def speak_old(text):
#     print("Jarvis:", text)
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()

def speak(text):
    print("Jarvis:", text)

    if os.path.exists("temp.mp3"):
        try:
            os.remove("temp.mp3")
        except PermissionError:
            pass

    tts = gTTS(text)
    tts.save("temp.mp3")

    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.stop()

    # ab file unlock ho jayegi
    pygame.mixer.music.unload()
    time.sleep(0.2)
    os.remove("temp.mp3")
    
def change_volume(action):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )

    volume = cast(interface, POINTER(IAudioEndpointVolume))

    if action == "up":
        for _ in range(6):
            volume.VolumeStepUp(None)

    elif action == "down":
        for _ in range(6):
            volume.VolumeStepDown(None)

    elif action == "mute":
        volume.SetMute(1, None)

    elif action == "unmute":
        volume.SetMute(0, None)  

def processCommand(c):
    c = c.lower().strip()

    # ---------- OPEN APPLICATIONS ----------

    if "vs code" in c or "visual studio code" in c:
        speak("Opening VS Code.")
        subprocess.Popen("code")
        return

    elif "calculator" in c:
        speak("Opening Calculator.")
        subprocess.Popen("calc.exe")
        return
    
    elif "increase volume" in c or "volume up" in c:
        change_volume("up")
        speak("Increasing volume.")
        return

    elif "decrease volume" in c or "volume down" in c:
        change_volume("down")
        speak("Decreasing volume.")
        return

    elif "mute" in c:
        change_volume("mute")
        speak("Volume muted.")
        return

    elif "unmute" in c:
        change_volume("unmute")
        speak("Volume restored.")
        return

    elif c.startswith("write note"):
        note = c.replace("write note", "").strip()

        with open("notes.txt", "a") as f:
            f.write(note + "\n")

        speak("Note saved.")
        return

    elif "read notes" in c:
        if os.path.exists("notes.txt"):
            with open("notes.txt") as f:
                notes = f.read()
            speak(notes)
        else:
            speak("No notes found.")


    elif "jarvis project" in c:
        speak("Opening Jarvis project.")
        os.startfile(JARVIS_PATH)
        return        

    # ---------- FOLDERS ----------

    elif "downloads" in c:
        speak("Opening Downloads.")
        os.startfile(str(Path.home() / "Downloads"))
        return

    elif "documents" in c:
        speak("Opening Documents.")
        os.startfile(str(Path.home() / "Documents"))
        return

    elif "desktop" in c:
        speak("Opening IITM BS.")
        os.startfile(str(Path.home() / "IITM BS"))
        return

    elif "pictures" in c:
        speak("Opening Pictures.")
        os.startfile(str(Path.home() / "Pictures"))
        return

    elif "music folder" in c:
        speak("Opening Music folder.")
        os.startfile(str(Path.home() / "Music"))
        return

    elif "notepad" in c:
        speak("Opening Notepad.")
        subprocess.Popen("notepad.exe")
        return

    elif "paint" in c:
        speak("Opening Paint.")
        subprocess.Popen("mspaint.exe")
        return

    elif "command prompt" in c or "cmd" in c:
        speak("Opening Command Prompt.")
        subprocess.Popen("cmd.exe")
        return

    elif "file explorer" in c or "explorer" in c:
        speak("Opening File Explorer.")
        subprocess.Popen("explorer.exe")
        return

    elif "settings" in c:
        speak("Opening Settings.")
        os.system("start ms-settings:")
        return

    # ---------- TIME ----------

    elif "time" in c:
        current = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current}")
        return

    # ---------- DATE ----------

    elif "date" in c:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {today}")
        return

    # ---------- BATTERY ----------

    elif "battery" in c:
        battery = psutil.sensors_battery()

        if battery:
            speak(f"Battery is at {battery.percent} percent.")
        else:
            speak("Battery information is unavailable.")

        return

    # ---------- SCREENSHOT ----------

    elif "screenshot" in c:
        filename = f"screenshot_{int(time.time())}.png"
        pyautogui.screenshot(filename)
        speak("Screenshot taken.")
        return
    
    # ---------- YOUTUBE SEARCH ----------

    elif c.startswith("search youtube"):
        query = c.replace("search youtube", "").strip()

        if query:
            speak(f"Searching YouTube for {query}")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={query}"
            )

        else:
            speak("What should I search on YouTube?")    

        return
    # ---------- GOOGLE SEARCH ----------

    elif c.startswith("search "):

        query = c.replace("search ", "").strip()

        if query:
            speak(f"Searching Google for {query}")
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

        else:
            speak("What should I search?")    

        return


    elif "google" in c:
        speak("Opening Google.")
        webbrowser.open("http://google.com")
        return

    elif "youtube" in c:
        speak("Opening youtube.")
        webbrowser.open("http://youtube.com")
        return

    elif "linkedin" in c:
        speak("Opening linkedin.")
        webbrowser.open("http://linkedin.com")
        return

    elif "instagram" in c:
        speak("Opening instagram.")
        webbrowser.open("http://instagram.com")
        return

    elif "github" in c:
        speak("Opening github.")
        webbrowser.open("http://github.com")
        return

    elif "chatgpt" in c:
        speak("Opening ChatGPT.")
        webbrowser.open("https://chat.openai.com/")
        return

    elif c.startswith("play"):
        song = c.replace("play ", "") 
        link = music_library.music.get(song)
        if link:
            webbrowser.open(link)
        else:
                speak("Song not found.")
                return

    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}", timeout= 10)    
            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()

                # Extract the articles
                articles = data.get('articles', [])

                # Print the headlines
                for article in articles:
                    speak(article['title'])

        except requests.exceptions.Timeout: 
            speak("News server is taking too long to respond.") 

        except requests.exceptions.RequestException as e:
            print(e)
            speak("Sorry, I couldn't fetch the news.")
            return

    elif c.startswith("copy"):
        text = c.replace("copy", "").strip()
        pyperclip.copy(text)
        speak("Copied.")
        return    

    elif "clipboard" in c:
        text = pyperclip.paste()
        if text:
            speak(text)
        else:
            speak("Clipboard is empty.")
            return   

    else:
        try:
            response = ask_gemini(c)
            speak(response)
        except Exception as e:
            speak("Sorry, I couldn't reach Gemini right now")          

def run_text_mode():
    speak("Text mode ready, Sir.")

    while True:
        try:
            command = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not command:
            continue

        if command.lower() in [
            "stop",
            "sleep",
            "go to sleep",
            "exit",
            "bye",
            "stop listening",
            "shutup",
        ]:
            speak("Going to sleep.")
            break

        processCommand(command)

if __name__ == "__main__":

    if "--text" in sys.argv:
        run_text_mode()
        raise SystemExit

    print("Calibrating microphone...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Calibration Complete.") 

    speak("Initializing Jarvis....")


    while True: 
        # Listen for the wake word Jarvis
        # Obtain audio from the microphone

        print("Waiting for wake word...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            word = recognizer.recognize_google(audio)
            if "jarvis" in word.lower(): 
                speak("Ready Sir.")

                while True:

                    try:
                        with sr.Microphone() as source: 
                            print("-" * 40) 
                            print("Listening for command...") 

                            audio = recognizer.listen(
                                source,
                                timeout=5,
                                phrase_time_limit=8
                            )

                        command = recognizer.recognize_google(audio)

                        print(f"You : {command}")

                        # Exit Continuous Mode
                        if command.lower() in [
                            "stop",
                            "sleep",
                            "go to sleep",
                            "exit",
                            "bye",
                            "stop listening"
                            "shutup"
                        ]:
                            speak("Going to sleep.")
                            break

                        command = command.lower().strip()
                        # Ignore wake word during continuous mode
                        if command == "jarvis":
                            speak("I'm already listening.")
                            continue
                        processCommand(command)

                    except sr.UnknownValueError:
                        print("Please repeat.")
                        continue

                    except sr.WaitTimeoutError:
                        speak("Going to sleep.")
                        break

        except Exception as e:
            print("Error {0}".format(e))            



