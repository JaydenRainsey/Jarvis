# This is a tts python program
import pyttsx3 # pip install pyttsx3: text to speech package
import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getVoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)

    if voice == 2:
        engine.setProperty('voice', voices[1].id)
    speak("hello I am Jarvis")

    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # Hour, Minutes, Seconds
    speak("The current time is: ")
    speak(Time)

# while True:
#     voice = int(input("Press 1 for male voice\nPress 2 for female voice\n"))
#     #speak(audio)
#     getVoices(voice)
time()