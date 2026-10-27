from listener import listen
from speaker import speak
from actions import execute_action
from brain import ask_ai
import config

def start_assistant():
    speak(f"Hello {config.USER_NAME}, I am {config.ASSISTANT_NAME}. How can I help you today?")

    while True:
        query = listen()

        if not query:
            continue

        if any(word in query for word in ["exit", "quit", "stop", "bye"]):
            speak(f"Goodbye {config.USER_NAME}! Have a great day.")
            break

        action_done = execute_action(query)

        if not action_done:
            answer = ask_ai(query)
            speak(answer)

if __name__ == "__main__":
    start_assistant()