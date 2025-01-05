from services.gemini import BotService
from services.generate import generate_latex_with_ai
from system_context.context import system_context


def generate_content(user_prompt):
    final_content = BotService.connect_agent(system_context(), user_prompt)
    return final_content

def generate_latex_ai(app):
    return generate_latex_with_ai(app)
    
