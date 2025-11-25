
from Whatsapp.llm_service import get_llama_response

def classify_intent(user_message):

    prompt = f"""
    You are an intent detection AI for an e-commerce WhatsApp chatbot.

    User message: "{user_message}"

    Classify the message into ONLY ONE of the following intents:

    1. view_products — user wants to see available products
    2. view_orders — user wants to check previous or current orders
    3. return_policy — user asks about refund, returns, or exchanges
    4. make_order — user wants to buy or order a product
    5. fallback — anything else

    Respond only with the intent name (for example: view_products).
    """

    intent = get_llama_response(prompt).lower().strip()

    
    if "product" in intent:
        return "view_products"
    if "order" in intent:
        return "view_orders"
    if "return" in intent or "refund" in intent:
        return "return_policy"
    if "buy" in intent or "purchase" in intent or "make" in intent:
        return "make_order"

    return "fallback"

