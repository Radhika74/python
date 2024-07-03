
from gtts import gTTS
from playsound import playsound
import os

names = ["Ram", "Rohan", "Rohit", "Raj", "Rajat"]

for name in names:
    text = f"Shoutout to {name}"
    tts = gTTS(text=text, lang='en')
    filename = f"{name}.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)  # Clean up the file after playing
