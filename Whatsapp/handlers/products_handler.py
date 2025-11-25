from models.allModels import AllProducts

def handle_products():
    products = AllProducts.query.all()

    if not products:
        return "No products available."

    reply = "📦 *Available Products*\n\n"
    for p in products:
        reply += f"🔸 {p.product_name} – Rs.{p.price}\n"

    return reply
