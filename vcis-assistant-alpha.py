from re import search
from numpy import r_
import pyttsx3                        ##text to speech library
import datetime                       ##for date & time
import speech_recognition as sr       ##for getting input voices, speech to text library
import wikipedia                      ##for surfing Wikipedia
import os                             ##for opening local files
import webbrowser                     ## for surfing the internet



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate",175)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning participants and judges! Welcome to HackVCIS 2022!")
    elif hour>=12 and hour<18:
        speak("Good afternoon participants and judges! Welcome to HackVCIS 2022!")   
    else:
        speak("Good evening everyone! Welcome to HackVCIS 2022!")  
    speak("I'm your personel assistant Vcis! How can I help you")
    
def command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.3
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}\n")

    except Exception as e:
        return "None"
    return query





if __name__ == "__main__":
    greet()
    #while True:
    if 1:
        query = command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(f'{query}', sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open hackVCIS' in query:
            speak("Here is the hackVCIS website\n")
            webbrowser.open("hackvcis.com")
        
        elif 'open youtube' in query:
            speak("Here is the youtube\n")
            webbrowser.open("https://www.youtube.com")

        elif 'open github' in query:
            speak("Here is the github\n")
            speak("please enjoy coding")
            webbrowser.open("https://www.github.com")

        elif 'open microsoft' in query:
            speak("Here is the microsoft website\n")
            webbrowser.open("https://www.microsoft.com") 
            
        elif 'what is the weather' in query or "the weather" in query:
            speak("Here is the weather in your location from google")
            url = "https://www.google.com/search?q=weather"
            webbrowser.get().open(url)  

        elif 'open google' in query:
            speak("Here is the google\n")
            webbrowser.open("https://www.google.com") 

        elif 'play music' in query:
            speak("Here you go\n")
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
            
        elif 'javascript beginner' in query or "javascript video" in query:
            speak("Here is the playlist of javascript for beginners\n")
            webbrowser.open("https://www.youtube.com/playlist?list=PLlrxD0HtieHhW0NCG7M536uHGOtJ95Ut2")

        elif 'web devlopment' in query or "web devlopment video" in query:
            speak("Here is the playlist of web devlopment workshop\n")
            webbrowser.open("https://bit.ly/3HQQ3xK")

        elif 'the time' in query or "what time is it" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Time is",strTime)    
            speak(f"Now the time is {strTime}")

        elif 'open anaconda' in query:
            condapath = "C:\\Users\\Tor\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)"
            os.startfile(condapath) 
        
        elif 'discord' in query:
            calpath = "C:\\Users\\Tor\\AppData\\Local\\Discord\\app-1.0.9003"
            os.startfile(calpath)       
       
        elif "how are you" in query:
            print("I'm fine, glad you asked.")
            speak("I'm fine, glad you asked")

        elif "what's your name" in query:
            print("My name is Vcis. I was created in HackVCIS hackathon.")
            speak("My name is Vcis. I was created in HackVCIS hackathon")
        
        elif "who created you" in query:
            print("I was created by many people on internet. But DuoDev team in HackVCIS hackathon are adding codes modifiying and improving me to be better!")
            speak("I was created by many people on internet. But DuoDev team in HackVCIS hackathon are adding codes modifiying and improving me to be better!")
        
        else:
            print("Sorry! We can't do that or please try again.")
            speak("Sorry! We can't do that or please try again")
