import speech_recognition as sr
import time

def init_stt() -> sr.Recognizer:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.8
    return recognizer


def calibrate(recognizer: sr.Recognizer, duration: float = 1.0) -> None:
    
    with sr.Microphone() as source:
        print("[INFO] Calibrating for background noise... please stay quiet.")
        recognizer.adjust_for_ambient_noise(source, duration)
        print("[INFO] Calibration complete.")

    
def listen(recognizer: sr.Recognizer) -> str | None:

    with sr.Microphone() as source:
        print("[LISTENING] Speak now...")

        # this block is inside here because listen() needs an audio source open
        try:
            # AudioData instance, not actual text
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            print("[INFO] No Audio Detected(timed out)")
            return None

    # Give the microphone a short moment to release before speaking.
    time.sleep(0.1)
    try:
        text = recognizer.recognize_whisper(audio, model="base", language="en").lower()
    except Exception as e:
        print(f"[ERROR] Whisper transcription failed: {e}")
        return None
    
    if not text:
        print("[INFO] Could not understand the audio.")
        return None

    print(f"[YOU] {text}")
    return text