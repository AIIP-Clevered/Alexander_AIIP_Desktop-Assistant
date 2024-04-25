import pyaudio
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import tkinter
from tkinter import*

root=Tk()



def speechText(command):
    bot=pyttsx3.init()
    bot.say(command)
    bot.runAndWait()

r=sr.Recognizer()
def getSpeech():
    global speech
    with sr.Microphone() as source:
        print("listening")
        audio=r.listen(source)
        print("processing")
        try:
            speech=r.recognize_google(audio)
        except:
            speech="voice error"
            speechText("voice error")
        print(" ")
        print(speech)

def voiceAssist():
    while True:
        getSpeech()
        if "hello" in speech:
            print("hello")
            speechText("hello")
        elif ("open" in speech) or ("Open" in speech): 
            if "calculator" in speech:
                print("Opening calculator")
                speechText("opening calculator")
                webbrowser.open('https://www.google.com/search?q=calculator&oq=calculator&gs_lcrp=EgZjaHJvbWUyDggAEEUYJxg5GIAEGIoFMgoIARAAGLEDGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgYIBxBFGEHSAQgzMDQ5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8')
            elif ("google" in speech) or ("Google" in speech):
                print("Opening Google")
                speechText("opening google")
                webbrowser.open('https://www.google.co.in/search?q=')
            elif ("youtube" in speech) or ("YouTube" in speech):
                print("Opening YouTube")
                speechText("opening youtube")
                webbrowser.open('https://www.youtube.com')
            elif "camera" in speech:
                print("Opening Camera")
                speechText("opening camera")
                webbrowser.open('microsoft.windows.camera:')
            else:
                print("Error")
                speechText("error")
        elif "search" in speech:
            search=speech.replace("search ","")
            stext="searching"+search
            print(stext)
            speechText(stext)
            webbrowser.open("google.com/search?q="+search)
            
    print(" ")

def main():
    voiceAssist()
def end():
    print("Ending program")
    speechText("ending program")
    root.destroy()
canvas1 = Canvas(root, width = 500, height = 300,bg = "black")
canvas1.pack()
button1 = Button (root, text="Let's have a conversation",command = main)
canvas1.create_window(250, 190, window=button1)
button2 = Button (root, text="Close",command = end)
canvas1.create_window(250, 250, window=button2)

label1 = Label(root, text='DESKTOP ASSISTANT')

canvas1.create_window(250, 50, window=label1)
root.mainloop()

