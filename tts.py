# output

import pyttsx3

def speak(text: str, rate: int = 150, volume: float = 1.0) -> None:

    print(f"[ASSISTANT] {text}")
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    
    engine.say(text)
    engine.runAndWait()

