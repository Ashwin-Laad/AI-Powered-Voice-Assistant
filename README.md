# AI-Powered-Voice-Assistant



# Description:
Here is a Python-based desktop voice assistant that integrates speech recognition, text-to-speech, and AI-powered conversation to automate tasks and interact naturally with users. It leverages the Gemini AI API to answer user queries dynamically while maintaining persistent chat history, enabling context-aware responses.

# Features

Voice Interaction: Real-time speech recognition using speech_recognition and spoken responses via Windows SAPI (win32com.client).

AI Responses: Integrates Gemini 2.5 API to answer user queries while keeping track of conversation context.

Task Automation: Launch applications, open websites, play music, and report the current time/date.

Persistent Chat History: Maintains multi-turn conversation context for more natural interactions.

Error Handling: Gracefully handles speech recognition errors, missing apps, and API failures.

# Tech Stack

Python 3.x

speech_recognition

win32com.client (Text-to-Speech)

webbrowser, os, subprocess (Task automation)

Gemini AI API (google.genai)
