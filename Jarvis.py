# This is a tts python program, called Jarvis
import pyttsx3 # pip install pyttsx3: text to speech package
import datetime
import speech_recognition as sr # speech from mic input
import smtplib
# from secrets import senderemail, epwd, to
import wikipedia

engine = pyttsx3.init()


myname = 'Jay'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Change voices from male to female
def getVoices(voice):
    voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(voice)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak(f'hello {myname}, I am Jarvis')
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak(f'hello {myname}, I am Friday')
    

    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # Hour, Minutes, Seconds
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
        speak(f'Good morning {myname}')
    elif hour >= 12 and hour < 18:
        speak(f'Good afternoon {myname}')
    elif hour >= 18 and hour < 24:
        speak(f'Good evening {myname}')
    else:
        speak(f'Good night {myname}')


def intro():
    greeting()
    speak(f'Welcome back')
    time()
    date()
    speak('Jarvis at your service, please tell me how I can assist you')
# while True:
#     voice = int(input("Press 1 for male voice\nPress 2 for female voice\n"))
#     #speak(audio)
#     getVoices(voice)


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
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)