#TODO startup: stuff that needs to be initialized once before the main event loop since they don't need to/shouldn't be repeated
    # 1- initialize stt
    # 2- intialize tts
    # 3- calibrate sst for room's noise 
    # 4- say greeting to notify user of app's start

#TODO loop: keeps repeating to capture used input until explicitly told to exit
    # 1- use the sst start listening (detecting sound then translating it to text)
    # 2- check if the input text is empty (means that the user didn't say anything) to skip this iteration and start listening again
    # 3- if it's not (means user actually said something), pass the processed input input to the brain to translate that into a response
    # 4- send the response to the sst to speak it out
    # 5- check if the user's input contained an exit word to terminate loop (done before reponse so it doesn't terminate abruptly)

from tts import init_tts, speak
from brain.intent import INTENTS
import random

rand_index = random.randint(0, len(INTENTS) - 1)
intent = INTENTS[rand_index]
# intent = INTENTS[-1]  # to try the repeat intent 
response = intent["response"]

# Handle both static strings and callable functions
if callable(response):
    response_text = response("repeat after me, i am a robot")
else:
    response_text = response

engine = init_tts()
speak(engine, response_text)