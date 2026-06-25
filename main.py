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
from stt import init_stt, calibrate, listen
from brain.assistant import get_response
from brain.intent import EXIT_KEYWORDS

def main():

    print("=== Voice Assistant Starting ===")
    
    recognizer = init_stt()
    engine = init_tts()

    calibrate(recognizer)
    speak(engine, "Hello! I'm Jarvis. How can I help you?")

    while True:

        user_text = listen(recognizer)
        if user_text is None:
            continue    #skip this iteration if any of the cases that result in none text occur

        respone = get_response(user_text)
        speak(engine, respone)

        if any(keyword in user_text for keyword in EXIT_KEYWORDS):
            print("[INFO] Exit keyword detected. Shutting down.")
            break
    
    print("=== Assistant stopped ===")


if __name__ == "__main__":
    main()