import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis, Your Personal assitance AI. Tell me what can I do for you")


def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language=='en-in')
        print(f"User Said : {query}\n")
    except Exception as e:
        print("Say That again please....")
        return "None"
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('surenaman9@gmail.com','password')
    server.sendemail('surenaman9@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishme()
    query=command().lower()
    while query!="stop" or query !="quit":
    #while 1:   
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir="D:\\akku"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(muisc_dir,songs[0]))
        
        elif 'current time'in query or 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif 'open v s code' in query:
            path="C:\\Users\\sure_\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.exe"
            os.startfile(path)
        
        elif 'send an email' in query:
            try:
                speak("What should I say ?")
                content=command()
                speak("what is the  email username")
                to=command()
                to+="@gmail.com"
                sendemail(to,content)
                speak("Email has been sent")
            
            except Exception as e:
                print("Sorry, I can't able to send the mail please try again later or diagnose the problem")
    query = takeCommand().lower()
