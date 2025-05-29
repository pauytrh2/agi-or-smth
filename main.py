#!/bin/python
from google import genai
import threading
from os import system as run_command
from imports.key import API_KEY
from imports.prompt import prompt
from imports.functions import write_file, open_url
from imports.parser import parse
from speech.stt import listen
from speech.tts import speak

client = genai.Client(api_key=API_KEY)

def run():
    while True:
        try:
            user_input = listen()
            print(f"Recognized: {user_input}")

            if "exit" in user_input:
                exit()

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=(prompt, user_input),
            ).text.strip()

            print(response, end="\n\n")
            human_text, action_code = parse(response)

            print({human_text, action_code})

            if action_code != "0":
                speak_thread = threading.Thread(target=speak, args=(human_text,))
                eval_thread = threading.Thread(target=eval, args=(action_code,))
                
                speak_thread.start()
                eval_thread.start()

                speak_thread.join()
                eval_thread.join()
            else:
                speak(human_text)

        except Exception as e:
            print(f"Error: {e}")
            speak("An error occurred.")

if __name__ == "__main__":
    run()