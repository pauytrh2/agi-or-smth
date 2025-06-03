import speech_recognition as sr
from tts import speak

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("No speech detected within timeout")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
    # return input("What is your prompt?: ")

if __name__ == "__main__":
    while True:
        command = listen()
        print("Recognized:", command)
        speak("I did not understand that")