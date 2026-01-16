from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os

# =========================
# APP CONFIG
# =========================
app = FastAPI(
    title="Learna-like AI Backend",
    description="25 Language Translation + Learning AI Backend",
    version="1.0.0"
)

# =========================
# SUPPORTED LANGUAGES
# =========================
SUPPORTED_LANGUAGES = [
    "English", "Urdu", "Hindi", "Arabic", "French", "Spanish",
    "German", "Italian", "Portuguese", "Russian", "Chinese",
    "Japanese", "Korean", "Turkish", "Indonesian", "Bengali",
    "Punjabi", "Persian", "Vietnamese", "Thai", "Malay",
    "Dutch", "Swedish", "Polish", "Greek"
]

# =========================
# REQUEST MODELS
# =========================
class TranslateRequest(BaseModel):
    source_language: str
    target_language: str
    text: str
    explain: Optional[bool] = False


class LearnRequest(BaseModel):
    language: str
    user_message: str
    level: Optional[str] = "Beginner"


class VoiceRequest(BaseModel):
    language: str
    text: str


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def health_check():
    return {
        "status": "running",
        "app": "Learna-like AI Backend",
        "languages_supported": len(SUPPORTED_LANGUAGES)
    }


# =========================
# LANGUAGE LIST
# =========================
@app.get("/languages")
def get_languages():
    return {
        "languages": SUPPORTED_LANGUAGES
    }


# =========================
# TRANSLATION ENDPOINT
# =========================
@app.post("/translate")
def translate(req: TranslateRequest):
    if req.source_language not in SUPPORTED_LANGUAGES:
        return {"error": "Source language not supported"}

    if req.target_language not in SUPPORTED_LANGUAGES:
        return {"error": "Target language not supported"}

    # ---- AI TRANSLATION PLACEHOLDER ----
    translated_text = f"[Translated to {req.target_language}]: {req.text}"

    response = {
        "source_language": req.source_language,
        "target_language": req.target_language,
        "original_text": req.text,
        "translated_text": translated_text
    }

    if req.explain:
        response["explanation"] = (
            f"This sentence was translated from {req.source_language} "
            f"to {req.target_language} using AI contextual understanding."
        )

    return response


# =========================
# LEARNING MODE (AI TEACHER)
# =========================
@app.post("/learn")
def learn_language(req: LearnRequest):
    if req.language not in SUPPORTED_LANGUAGES:
        return {"error": "Language not supported"}

    ai_reply = (
        f"You are learning {req.language} at {req.level} level. "
        f"You said: '{req.user_message}'. "
        f"Here is a corrected and improved version."
    )

    return {
        "language": req.language,
        "level": req.level,
        "user_input": req.user_message,
        "ai_reply": ai_reply,
        "tip": "Practice daily by speaking full sentences."
    }


# =========================
# TEXT TO SPEECH (HOOK)
# =========================
@app.post("/tts")
def text_to_speech(req: VoiceRequest):
    if req.language not in SUPPORTED_LANGUAGES:
        return {"error": "Language not supported"}

    return {
        "message": "TTS generated successfully",
        "language": req.language,
        "audio_url": "https://audio-service/voice-output.mp3"
    }


# =========================
# SPEECH TO TEXT (HOOK)
# =========================
@app.post("/stt")
def speech_to_text():
    return {
        "message": "Speech converted to text",
        "text": "Recognized speech will appear here"
    }
