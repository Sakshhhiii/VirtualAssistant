import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning boss ,rise and shine!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon guyss!")   

    else:
        speak("Good Evening fam!")  

    speak("hello I am chittin. Allow me to help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)  
         print("Say that again please...")  
         return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('def@gmail.com', 'def@1h')
    server.sendmail('def@gmail.com', to, content)
    server.close()
  
def  music():
    speak("which song you want to play")   
    musicName =takeCommand()
    
    if 'perfect' in musicName:
        os.startfile('C:\\Users\\saksh\\Downloads\\Perfect.mp3')
    else:
        pywhatkit.playonyt(musicName)
    speak("song is being played")   

if __name__ == "__main__":
    wishMe() 
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'hello' in query:
            speak("Hi there,i am your helper")
        elif 'how are you' in query:
            speak("i am good ,what about you?")    
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'music' in query:
              music()

        elif 'youtube search' in query :
            speak("i found this")
            query= query.replace("youtube search"," ")
            web='https://www.youtube.com/results?search_query'+query
            webbrowser.open(web)
            speak("it is opened")

        elif 'google search' in query :
            speak("i found this")
            query= query.replace("google search"," ")
            pywhatkit.search(query)
            speak("it is opened")   
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif ' Send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to ="AbC@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("apologies I am not able to send this email")
        elif 'stop' in query:
            speak("bye,Call me whenever you need me")
            exit()