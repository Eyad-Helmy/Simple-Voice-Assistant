# output

import pyttsx3
import time

def init_tts(rate: int = 150, volume: float = 1.0):
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    # Longer delay to let engine fully initialize before first use
    time.sleep(0.5)
    return engine

def speak(engine, text: str, ) -> None:
    print(f"[ASSISTANT] {text}")
    engine.say(text)
    engine.runAndWait()
