import sys

import speech_recognition as sr
import win32com.client
import webbrowser

import time
import os
from google import genai
from config import API_KEY


# engine = pyttsx3.init('sapi5')  # force Windows SAPI5
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)



speaker=win32com.client.Dispatch("SAPI.SpVoice")


chatHistory=""



def openMusic():
    music_path="C:/Users/ashwi/Desktop/Music"
    os.startfile(music_path)



def say(text):
    if text:
        speaker.Speak(text)

    else:
        speaker.Speak("Sorry, No text received.")




def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        # here there can be errors when we try to recognize the voice

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return None





def AI(prompt):

    global chatHistory
    instruction = (
        "You are a helpful assistant. Answer only the latest user query. "
        "Previous conversation is for context only.\n"
    )

    chatHistory+=instruction+ f"User said: {prompt}\nAI replied:"


    client = genai.Client(
        api_key=API_KEY
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= chatHistory
    )

    # response_text = response.candidates[0].content.parts[0].text
    # print(response_text)

    chatHistory+=f"{response.text}\n"

    say(response.text)
    print(chatHistory)

    client.close()


# def openApp(query):
#     for app in apps:
#         if f"open {app[0]}".lower() in query.lower():
#             say(f"Opening {app[0]}")
#             try:
#                 os.startfile(app[1])  # works for apps in PATH or full path
#             except:
#                 subprocess.Popen(app[1], shell=True)  # fallback
#
#     sys.exit()



say("Hello, I am a voice assistant")




while 1:

    query = takeCommand()
    # if "open youtube" in query.lower():
    #     say("Opening YouTube")
    #     webbrowser.open("youtube.com")
#todo find the websites
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["google", "https://www.google.com"],
        ["facebook", "https://www.facebook.com"],
        ["wikipedia", "https://www.wikipedia.org"],
        ["twitter", "https://www.twitter.com"],
        ["instagram", "https://www.instagram.com"],
        ["linkedin", "https://www.linkedin.com"],
        ["github", "https://www.github.com"],
        ["reddit", "https://www.reddit.com"],
        ["amazon", "https://www.amazon.com"]
    ]

    for s in sites:
        if f"Open {s[0]}".lower() in query.lower():
            say(f"Opening {s[0]}")
            webbrowser.open(s[0])

    # todo open apps
    apps = [
        ["notepad", "notepad.exe"],
        ["calculator", "calc.exe"],

    ]

    for a in apps:
        if f"Open {a[0]}".lower() in query.lower():
            say(f"Opening {a[0]}")
            os.startfile(a[1])

    #todo get the music
    if "open music".lower() in query.lower():
        say("Opening music")
        openMusic()

#todo get the time and date

    elif "time" in query.lower():
            current_time = time.localtime()
            say(f"The time is {current_time.tm_hour}:{current_time.tm_min}")

    elif "date" in query.lower():
            today = time.strftime("%d %B %Y")  # e.g., "02 October 2025"
            say(f"Today's date is {today}")




    elif "exit".lower() in query.lower():
        say("See ya")
        sys.exit()


    elif "Clear chat".lower() in query.lower():
        chatHistory=""

#todo if no above query pass it to AI
    else:
        print("AI is talking: ")
        AI(query)






