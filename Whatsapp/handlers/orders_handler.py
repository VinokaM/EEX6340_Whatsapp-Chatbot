import json

from models.allModels import Orders
from models.allModels import AllProducts

def handle_orders(phone_number):
    orders = Orders.query.filter_by(phone_number=phone_number).all()

    if not orders:
        return "You have no previous orders."

    reply = "🧾 *Your Previous Orders*\n\n"

    for o in orders:
        reply += f"📌 *Order #{o.id}* – {o.status}\n"

        try:
            product_list = json.loads(o.products)
        except:
            reply += "  ⚠️ Error reading product list\n\n"
            continue
        
        for item in product_list:
            product = AllProducts.query.get(item["product_id"])
            if product:
                reply += f"   • {product.product_name} × {item['qty']} (Rs.{product.price})\n"
            else:
                reply += f"   • Unknown product (ID {item['product_id']})\n"

        reply += f"   💰 *Total:* Rs.{o.total_price}\n\n"

    return reply
