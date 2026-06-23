# output

import pyttsx3

def init_tts(rate: int = 150, volume: float = 1.0):
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    return engine

def speak(engine, text: str, ) -> None:
    print(f"[ASSISTANT] {text}")
    engine.say(text)
    engine.runAndWait()
