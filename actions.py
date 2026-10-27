import os
import webbrowser
import datetime
import pywhatkit
import wikipedia
from speaker import speak

def execute_action(command):
    if "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
        return True

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Current time is {current_time}")
        return True

    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        pywhatkit.search(query)
        return True

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
        return True

    elif "open chrome" in command:
        speak("Opening Chrome")
        webbrowser.open("https://www.google.com")
        return True

    elif "who is" in command or "what is" in command:
        query = command.replace("who is", "").replace("what is", "").strip()
        try:
            info = wikipedia.summary(query, sentences=2)
            speak(info)
            return True
        except Exception:
            return False

    return False