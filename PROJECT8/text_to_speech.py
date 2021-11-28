import pyttsx3

data = input("Enter text to be read: ")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()
