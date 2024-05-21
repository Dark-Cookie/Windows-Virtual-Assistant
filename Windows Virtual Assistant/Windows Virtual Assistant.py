import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import random
import subprocess
import google.generativeai as genai
import requests
import newsapi
import time
from newsapi import NewsApiClient



engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Q5Q6GX-3UAGKW253J')

newsapi = NewsApiClient(api_key='***')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Assistant: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 17:
        speak('Good Afternoon!')

    if currentH >= 17 and currentH !=0:
        speak('Good Evening!')

greetMe()
speak('I am your personal assistant, i am designed specifically for Microsoft Windows :)')
speak('How may I help you?')


def get_news(query):
    try:
        # Get top headlines
        top_headlines = newsapi.get_top_headlines(q=query,
                                                  language='en',
                                                  country="us")

        # Extract the relevant information from the response
        articles = top_headlines['articles']
        news_response = ""
        for article in articles:
            news_response += f"{article['title']}\n\n"

        if news_response:
            speak(f"Here are the latest news:")
            speak(news_response)
        else:
            speak(f"Sorry, I couldn't find any news.")
    except Exception as e:
        speak("Sorry, I encountered an error while fetching the news.")
        print(f"Error: {e}")


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
        # Check if the query is news-related
        if 'news' in query.lower():
            get_news(query)
        else:
            return query
    except sr.UnknownValueError:
        speak("i'm Sorry! I didn't get that! Please type the command!")
        query = str(input('Command: '))

    return query


def ai(prompt):
    genai.configure(api_key="***")
    text = f"OpenAI response for prompt: {prompt} \n ******************************************************************************************************************************************************************************************************\n\n"

    # Set up the model
    generation_config = {
      "temperature": 0.9,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 2048,
    }

    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[ ])

    convo.send_message(prompt)
    print(convo.last.text)
    speak(f"{convo.last.text}")



if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('Okay')
            webbrowser.open('https://www.youtube.com')

        elif 'open Microsoft Word'.lower() in query.lower():
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        elif 'open reddit' in query:
            speak('Okay')
            webbrowser.open('https://www.reddit.com')

        elif 'open amazon' in query:
            speak('Okay')
            webbrowser.open('https://www.amazon.com')

        elif 'open twitter' in query:
            speak('Okay')
            webbrowser.open('https://www.twitter.com')

        elif 'open facebook' in query:
            speak('Okay')
            webbrowser.open('https://www.facebook.com')


        elif 'open stack overflow wikipedia and github' in query:
            speak('Opening Stack Overflow, Wikipedia, and Github')
            webbrowser.open('https://stackoverflow.com')
            time.sleep(1)
            webbrowser.open('https://www.wikipedia.org/')
            time.sleep(1)
            webbrowser.open('https://github.com')
            time.sleep(2)

            
        elif 'open instagram' in query:
            speak('Okay')
            webbrowser.open('https://www.instagram.com')

        elif 'open linkedin' in query:
            speak('Okay')
            webbrowser.open('https://www.linkedin.com')

        elif 'open netflix' in query:
            speak('Okay')
            webbrowser.open('https://www.netflix.com')

        elif 'open medium' in query:
            speak('Okay')
            webbrowser.open('https://medium.com')

        elif 'open microsoft' in query:
            speak('Okay')
            webbrowser.open('https://www.microsoft.com')

        elif 'open apple' in query:
            speak('Okay')
            webbrowser.open('https://www.apple.com')

        elif 'open spotify' in query:
            speak('Okay')
            webbrowser.open('https://www.spotify.com')

        elif 'open dropbox' in query:
            speak('Okay')
            webbrowser.open('https://www.dropbox.com')

        elif 'open tumblr' in query:
            speak('Okay')
            webbrowser.open('https://www.tumblr.com')

        elif 'open pinterest' in query:
            speak('Okay')
            webbrowser.open('https://www.pinterest.com')
        
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        
        elif 'open yahoo' in query:
            speak('okay')
            webbrowser.open('www.yahoo.com')
        

        elif "date and time" in query:
            strTimeDate = datetime.datetime.now().strftime("%H:%M:%S")
            strDateTime = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"The date is {strDateTime} and the time is, {strTimeDate}")

        elif "time and date" in query:
            strTimeDate = datetime.datetime.now().strftime("%H:%M:%S")
            strDateTime = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"The Time is {strTimeDate} and the Date is, {strDateTime}")
     
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is, {strTime}")
        
        elif "what is the date" in query:
            strDate = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"The Date is, {strDate}")


        elif 'open VLC Media Player'.lower() in query.lower():
            codePath = "C:/Program Files/VideoLAN//VLC/VLC.exe"
            os.startfile(codePath)
        
        elif 'open This PC'.lower() in query.lower():
            codePath = "C:/Windows/explorer.exe"
            os.startfile(codePath)
        
        elif 'open AnyDesk'.lower() in query.lower():
            codePath = "C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"
            os.startfile(codePath)

        elif 'open Bandicam'.lower() in query.lower():
            codePath = "C:\\Program Files\\Bandicam\\bdcam.exe"
            os.startfile(codePath)
        
        elif 'open Camtasia'.lower() in query.lower():
            codePath = "C:\\Program Files\\TechSmith\\Camtasia 2022\\CamtasiaStudio.exe"
            os.startfile(codePath)

        elif 'open Core Temp'.lower() in query.lower():
            codePath = "C:\\Program Files\\Core Temp\\Core Temp.exe"
            os.startfile(codePath)

        elif 'open Google Chrome'.lower() in query.lower():
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open Nitro Pro'.lower() in query.lower():
            codePath = "C:\\Program Files\\Nitro\\Pro\\13\\NitroPDF.exe"
            os.startfile(codePath)

        elif 'open TeamViewer'.lower() in query.lower():
            codePath = "C:\\Program Files\\TeamViewer\\TeamViewer.exe"
            os.startfile(codePath)

        elif 'open Winamp'.lower() in query.lower():
            codePath = "C:\\Program Files (x86)\\Winamp\\winamp.exe"
            os.startfile(codePath)

        elif 'open Bittorrent'.lower() in query.lower():
            codePath = "C:\\Users\\asif0\\AppData\\Roaming\\bittorrent\\BitTorrent.exe"
            os.startfile(codePath)

        elif 'open Internet Download Manager'.lower() in query.lower():
            codePath = "C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe"
            os.startfile(codePath)

        elif 'open Vegas Pro'.lower() in query.lower():
            codePath = "C:\\Program Files\\VEGAS\\VEGAS Pro 18.0\\vegas180.exe"
            os.startfile(codePath)

        elif 'open Rename my TV Series'.lower() in query.lower():
            codePath = "C:\\Program Files (x86)\\Rename My TV Series\\RenameMyTVSeries.exe"
            os.startfile(codePath)

        elif 'open Filezilla'.lower() in query.lower():
            codePath = "C:\\Program Files\\FileZilla FTP Client\\filezilla.exe"
            os.startfile(codePath)

        elif 'open JDownloader'.lower() in query.lower():
            codePath = "C:\\Users\\asif0\\AppData\\Local\\JDownloader 2.0\\JDownloader2.exe"
            os.startfile(codePath)

        

        elif 'open Microsoft Excel'.lower() in query.lower():
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)

        elif 'open Microsoft Powerpoint'.lower() in query.lower():
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)

        elif 'open Notepad'.lower() in query.lower():
            codePath = "C:\\Windows\\notepad.exe"
            os.startfile(codePath)

        elif "hii" in query or 'how are you' in query or 'hi' in query:
            stMsgs = ["Just here to assist you!", "Hi! Just here, doing my digital thing, how can i help you?", "All good on this end!", "Hey! Feeling great and ready to help!", "Hi! I'm here and excited to assist you!", "Hello! I'm here, fully charged and ready to assist!"]
            speak(random.choice(stMsgs))

        elif "using Generative AI".lower() in query.lower():
            ai(prompt=query)

        elif 'news' in query.lower():
            get_news(query)

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()
            
#sending an email using https://mailtrap.io/home
            
            if 'me' in recipient:
                try:
                    speak('What should I say?')
                    content = myCommand()
                    sender = "***"
                    receiver = "***"
                    subject = 'Hi Mailtrap'
                    message = f"Subject: {subject}\nTo: {receiver}\nFrom: {sender}\n\n{content}"

                    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
                        server.login("***", "***")
                        server.sendmail(sender, receiver, message)
                        server.close()
                        speak('Email sent!')

                except:
                    speak("I'm sorry! I am unable to send your email at this moment!")


        elif 'nothing' in query or 'quit' in query or 'stop' in query or 'exit' in query:
            speak('okay')
            speak('Bye, have a nice day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello, How may i help you')

        elif 'bye' in query:
            speak('Bye-bye, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_dir = 'D:\\Music Favourites'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Completed. What else can i do?')