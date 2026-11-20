"""Session 6 Task 2 - Customer Support Chatbot flow for a food delivery app (if-else logic)."""


def support_bot(message: str) -> str:
    m = message.lower()
    if "refund" in m or "money back" in m or "cancel" in m:
        return ("Refund request: I'm sorry about that! Please share your order ID. Eligible refunds are credited to your "
                "original payment method within 5-7 working days.")
    elif "late" in m or "delay" in m or "taking too long" in m or "not arrived" in m:
        return ("Delivery delay: Sorry for the wait! Your partner is on the way and the live ETA is shown on the tracking "
                "screen. If it is 20+ minutes late you can claim a discount coupon.")
    elif "order" in m or "status" in m or "track" in m or "where" in m:
        return "Order status: Your order is being prepared / is out for delivery. Tap 'Track Order' for the live location."
    else:
        return "Sorry, I can help with order status, refund requests and delivery delays. Which one do you need?"


if __name__ == "__main__":
    tests = ["Where is my order?", "I want a refund for my cold pizza", "My food is very late, why the delay?", "Do you have coupons?"]
    for t in tests:
        print("User: %s\nBot : %s\n" % (t, support_bot(t)))
