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
- Reply in under 40 words.
- Never use markdown (no asterisks, hash tags, or bold text).
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
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.7,
                max_output_tokens=100  # Enforces brief voice responses
            )
        )
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry Sir, I encountered an error connecting to my servers."