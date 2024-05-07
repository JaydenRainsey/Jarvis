# This is a tts python program, called Jarvis
import pyttsx3  # pip install pyttsx3: text to speech package
import datetime
import speech_recognition as sr  # speech from mic input
import smtplib
# from secrets import senderemail, epwd, to
import wikipedia
import webbrowser as wb
import pywhatkit
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


myname = 'Jayden'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Change voices from male to female


def getVoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[2].id)
    if voice == 1:
        engine.setProperty('voice', voices[2].id)
        speak(f'hello, I am Jarvis')
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak(f'hello, I am Friday')


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  # Hour, Minutes, Seconds
    speak("The current time is: ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('The current date is: ')
    speak(day)
    speak(month)
    speak(year)

# Greets according to the time


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak(f'Good morning mister {myname}')
    elif hour >= 12 and hour < 18:
        speak(f'Good afternoon mister {myname}')
    elif hour >= 18 and hour < 24:
        speak(f'Good evening mister {myname}')
    else:
        speak(f'Good night mister {myname}')


def intro():
    greeting()
    speak(f'Welcome back')
    time()
    date()
    speak('Jarvis at your service, please tell me how I can assist you')


def takeCommandCMD():
    query = input("How can I assit you? ")
    return query


def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query


# def sendEmail():
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(senderemail, epwd)
#     server.sendemail(senderemail, to, 'hello, this is Jarvis')
#     server.close()


def searchGoogle():
    speak(f'what should I search for on google')
    search = input("What to search on google? ")
    wb.open('https://www.google.com/search?q='+search)


if __name__ == "__main__":
    getVoices(1)
    intro()
    while True:
        query = takeCommandCMD().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak(f'searching topic on wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'search' in query:
            searchGoogle()

        elif 'youtube' in query:
            speak('What should I search for on youtube?')
            topic = input("What to search for on youtube? ")
            pywhatkit.playonyt(topic)

        elif 'offline' in query:
            speak('Now going offline')
            quit()
