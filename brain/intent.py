# contains all the assistant's "knowledge" (what it can understand and what the response shuold be)
# it doesn't match or do anything but only acts as a database for which words to map to which responses

import datetime
import random
 
 
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
        "response": "I don't have live weather access yet, but you can ask me to add it!"
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