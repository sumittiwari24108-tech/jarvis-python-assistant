import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Automatically reads GEMINI_API_KEY from .env
client = genai.Client()

SYSTEM_INSTRUCTION = """
You are Jarvis, an intelligent desktop voice assistant created by Sumit.

Rules:
- Keep responses under 40 words.
- For factual questions, give a useful answer in 2-4 short sentences.
- Never use markdown.
- Never use bullet points unless explicitly asked.
- Speak naturally like a real human assistant.
- Be concise, direct, and helpful.
- If the user asks to open, search, play, or perform a system task that isn't handled, politely state you cannot perform it yet.
- Never say you are Gemini or an AI language model.
- Address the user as "Sir" occasionally, but do not overuse it.
"""

def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                thinking_config=types.ThinkingConfig(
                    thinking_level="low"
                )
            )
        )

        return response.text

    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry Sir, I encountered an error connecting to my servers."