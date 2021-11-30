import speech_recognition as sr
import pyttsx3
import datetime

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
    speak('The current time is {Time}')


time()
