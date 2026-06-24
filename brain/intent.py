# contains all the assistant's "knowledge" (what it can understand and what the response shuold be)
# it doesn't match or do anything but only acts as a database for which words to map to which responses

import datetime
import random
import requests
from urllib.parse import quote_plus
 
 
# ── Response functions ──────────────────────────────────────────
# These are used instead of static strings when the response needs to
# be computed dynamically (e.g. the actual current time), rather than
# being the same every time.
 
def get_time(_user_text: str) -> str:
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."
 
 
def get_date(_user_text: str) -> str:
    today = datetime.date.today()
    return f"Today is {today.strftime('%A, %B %d, %Y')}."
 
 
def tell_joke(_user_text: str) -> str:
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
        "Why did the neural network break up with the decision tree? Too many branches.",
    ]
    return random.choice(jokes)
 

def extract_weather_location(user_text: str) -> str | None:
    lower_text = user_text.lower()
    for keyword in [" in ", " at ", " for "]:
        if keyword in lower_text:
            location = lower_text.split(keyword, 1)[1].strip()
            if location:
                for stop in ["?", ".", "!", ","]:
                    location = location.split(stop, 1)[0].strip()
                return location
    return None


def get_weather(user_text: str) -> str:
    location = extract_weather_location(user_text) or ""
    query = quote_plus(location) if location else ""
    url = f"https://wttr.in/{query}?format=j1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data["current_condition"][0]
        area = data.get("nearest_area", [{}])[0].get("areaName", [{}])[0].get("value", "your location")
        temp_c = current.get("temp_C", "unknown")
        description = current.get("weatherDesc", [{"value": "unknown"}])[0].get("value", "unknown")
        feels_like = current.get("FeelsLikeC", "unknown")
        return f"The weather in {area} is {description} with a temperature of {temp_c}°C and it feels like {feels_like}°C."
    except Exception:
        return "I couldn't fetch the weather right now. Please try again in a moment."


def say_goodbye(_user_text: str) -> str:
    return "Goodbye! Have a great day."


def repeat_user_text(_user_text: str) -> str:
    return extract_repeat_text(_user_text)
# ->
def extract_repeat_text(user_text: str) -> str:
    trigger_phrases = INTENTS[-1]["keywords"]

    text = user_text.strip()
    normalized = text.lower().strip()

    for phrase in trigger_phrases:
        if normalized.startswith(phrase):
            text = text[len(phrase):].lstrip(" ,.!?")
            break

    return text or "Please tell me what to repeat."



# ── Intent definitions ──────────────────────────────────────────

INTENTS = [
    {
        "name": "greet",
        "keywords": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "greetings", "what's up", "how are you", "how's it going", "sup", "yo"],
        "response": "Hello! How can I help you today?"
    },
    {
        "name": "time",
        "keywords": ["time", "what time", "current time", "what's the time", "tell me the time", "what time is it", "current hour"],
        "response": get_time
    },
    {
        "name": "date",
        "keywords": ["date", "what day", "today's date", "what's today", "today", "what date is it", "current date", "what day is today"],
        "response": get_date
    },
    {
        "name": "joke",
        "keywords": ["joke", "funny", "make me laugh", "tell me a joke", "tell a joke", "make me smile", "something funny", "crack a joke"],
        "response": tell_joke
    },
    {
        "name": "name",
        "keywords": ["your name", "who are you", "what are you called", "what's your name", "introduce yourself", "what do you call yourself"],
        "response": "I'm Jarvis, your personal voice assistant."
    },
    {
        "name": "weather",
        "keywords": ["weather", "temperature", "forecast", "raining", "is it raining", "how's the weather", "what's the temperature", "what's the forecast"],
        "response": get_weather
    },
    {
        "name": "farewell",
        "keywords": ["bye", "goodbye", "see you", "exit", "quit", "stop", "see you later", "later", "cya", "talk to you later", "have a good day"],
        "response": say_goodbye
    },
    {
        "name": "repeat",
        "keywords": [
        "repeat after me",
        "repeat after me please",
        "repeat",
        "say",
        "tell me",
        "can you repeat",
        "please repeat",
        ],
        "response": repeat_user_text
    },
]


FALLBACK_RESPONSE = "I'm not sure I understood that. Could you rephrase?"

# same as farewell keywords but will get checked after the farewell response is given
# to terminate the app after the goodbye is said not before
EXIT_KEYWORDS = ["bye", "goodbye", "see you", "exit", "quit", "stop"]