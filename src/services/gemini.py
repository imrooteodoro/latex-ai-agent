import os
import google.generativeai as genai
from auth.auth import authentication

class BotService:
    def __init__(self):
        pass

    def connect_agent(system_context, user_message):
        genai.configure(api_key=authentication())

        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        system_instruction=f"{system_context}",
        )

        chat_session = model.start_chat(
        history=[
        ]
        )

        response = chat_session.send_message(f"{user_message}")

        return response.text