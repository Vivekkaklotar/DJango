# PayPal Flask Integration (Prompt & Code)
# Prompt: "Generate Flask code for PayPal REST SDK checkout flow"
import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox", # sandbox or live
    "client_id": "YOUR_PAYPAL_CLIENT_ID",
    "client_secret": "YOUR_PAYPAL_CLIENT_SECRET"
})

@app.route('/paypal-pay', methods=['POST'])
def paypal_pay():
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:5000/paypal-success",
            "cancel_url": "http://localhost:5000/paypal-cancel"
        },
        "transactions": [{
            "amount": {"total": "10.00", "currency": "USD"},
            "description": "IPL Ticket Booking Payment"
        }]
    })
    
    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    return "Error creating PayPal payment", 500