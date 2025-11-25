from Whatsapp.intent_classifier import classify_intent
from Whatsapp.handlers.products_handler import handle_products
from Whatsapp.handlers.orders_handler import handle_orders
from Whatsapp.handlers.policy_handler import handle_policy
from Whatsapp.handlers.fallback_handler import handle_fallback

def route_intent(user_message, phone_number):
    intent = classify_intent(user_message)

    if intent == "view_products":
        return handle_products()

    if intent == "view_orders":
        return handle_orders(phone_number)

    if intent == "return_policy":
        return handle_policy()

    if intent == "make_order":
        return "To place an order, send product name + quantity."

    return handle_fallback(user_message)
