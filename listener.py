import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("\nसुन रहा हूँ...")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        recognizer.pause_threshold = 1.0
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("पहचान रहा हूँ...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"[You]: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception:
            return ""