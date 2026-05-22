import ollama

from app.config.settings import CHAT_MODEL

def generate_response(prompt: str):

    response = ollama.chat(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]