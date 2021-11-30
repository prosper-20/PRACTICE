import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("Welcome Back!")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak(f'The current time is {Time}')


def wiki():
    query = ("Iphone")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    print(results)
    speak(results)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"Prosper said {query}\n")

    except Exception as e:
        print(e)
        print("Say that again.....")
        speak("Say that again.....")
        return "None"
    return query

takecommand()


