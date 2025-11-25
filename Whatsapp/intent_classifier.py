


def classify_intent(user_message):
    msg = user_message.lower()

    if "all product" in msg or "products" in msg or "show products" in msg:
        return "view_products"

    if "my orders" in msg or "previous order" in msg or "order history" in msg:
        return "view_orders"

    if "return policy" in msg or "refund" in msg or "can i return" in msg:
        return "return_policy"

    if "order" in msg and ("buy" in msg or "purchase" in msg):
        return "make_order"

    return "fallback"
