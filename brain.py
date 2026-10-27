from google import genai
import config

client = genai.Client(api_key=config.GEMINI_API_KEY)

def ask_ai(prompt):
    try:
        system_instruction = (
            "You are a helpful personal voice assistant. "
            "Give very concise, natural, and friendly spoken answers in 1-2 sentences."
        )
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{system_instruction}\nUser: {prompt}"
        )
        return response.text
    except Exception:
        return "Sorry, I am facing an issue connecting to the AI server."