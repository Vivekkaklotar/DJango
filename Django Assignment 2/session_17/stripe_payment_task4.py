import stripe
from flask import Flask, jsonify, request

stripe.api_key = "sk_test_YOUR_STRIPE_TEST_KEY"

@app.route('/create-stripe-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = request.json
        intent = stripe.PaymentIntent.create(
            amount=int(data['amount']) * 100, # Amount in paise/cents
            currency='inr',
            payment_method_types=['card'],
        )
        return jsonify({'clientSecret': intent['client_secret']})
    except Exception as e:
        return jsonify({'error': str(e)}), 400