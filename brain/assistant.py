# controls matching the actual user text into one of the stored intenions in a slightly intelligent way
# the logic that the data in intent is processed by

from brain.intent import INTENTS, FALLBACK_RESPONSE
import re

def match_intent(user_text: str) -> dict | None:
    user_text = user_text.lower()
    
    best_score = 0
    best_intent = None

    for intent in INTENTS:
        score = 0
        for keyword in intent["keywords"]:
            pattern = r"\b" + re.escape(keyword) + r"\b"
            if re.search(pattern, user_text):
                score += len(keyword)
                # if user_text = "hello and welcome"
                # and keyword = "hello"
                # then it would find hello and increase greet intent's score by 5
            
        # after all of the keywords for the intents were looked for check its score compared to the last best
        if score > best_score:
            best_score = score
            best_intent = intent

    
    if best_score == 0:
        return None

    return best_intent


def get_response(user_text: str) -> str:

    intent= match_intent(user_text)
    
    if intent == None:
        return FALLBACK_RESPONSE
    
    response = intent["response"]

    if callable(response):
        return response(user_text)  # pass user_text incase its a function that takes user text as an argument
    
    return response

