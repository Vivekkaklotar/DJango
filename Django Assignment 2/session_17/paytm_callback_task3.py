@app.route('/payment-callback', methods=['POST'])
def payment_callback():
    callback_data = request.form.to_dict()
    # verify signature logic
    if callback_data.get('RESPCODE') == '01':
        return "<h1>Payment Successful! Ticket Confirmed.</h1>"
    else:
        return "<h1>Payment Failed or Cancelled.</h1>", 400