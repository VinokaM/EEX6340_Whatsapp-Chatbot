# from models.orders import Orders

# def handle_orders(phone_number):
#     orders = Orders.query.filter_by(user_phone=phone_number).all()

#     if not orders:
#         return "You have no previous orders."

#     reply = "🧾 *Your Previous Orders*\n\n"
#     for o in orders:
#         reply += f"Order #{o.id} – {o.status}\n"

#     return reply
