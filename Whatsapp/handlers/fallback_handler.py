from Whatsapp.llm_service import get_llama_response

def handle_fallback(user_message):
    return get_llama_response(user_message)
