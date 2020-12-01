import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Naman, I am your personal assistant AI')
speak('How may I help you?')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry Naman! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand().lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the sender? ')
            sender = myCommand()

            if 'I am' in sender:
                try:
                    speak("Please Enter Email address of Recipient.")
                    Recipient_user = input("User: ")
                    speak('What should I say? ')
                    content = myCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("surenaman9@gmail.com", 'password')
                    server.sendmail('surenaman9@gmail.com', Recipient_user, content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Naman! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query:
            speak('okay')
            speak('Bye Naman, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Naman')


        elif 'play music' in query:
            music_folder = "D:\\jarvis\\music\\"
            music = ["music1", "music2", "music3", "music4", "music5"]
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            os.system(random_music)
            #os.startfile(random_music)
            


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Naman!')
