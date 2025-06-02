from gtts import gTTS
from playsound import playsound
from os import mkdir

try:
    mkdir("tmpaudio")
except OSError: # dir already exists
    pass

def speak(text):
    print(f"Jarvis: {text}")
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("tmpaudio/tmp.mp3")
    playsound("tmpaudio/tmp.mp3")