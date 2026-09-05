# Paytm Initiate Route
@app.route('/paytm-initiate', methods=['POST'])
def paytm_initiate():
    paytm_params = {
        "MID": "YOUR_MID_HERE",
        "ORDER_ID": "ORDER_1001",
        "CUST_ID": request.form['email'],
        "TXN_AMOUNT": request.form['amount'],
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        "CALLBACK_URL": "http://127.0.0.1:5000/payment-callback",
    }
    # Checksum generation using PaytmChecksum library
    # checksum = PaytmChecksum.generateSignature(paytm_params, "YOUR_MERCHANT_KEY")
    return f"Redirecting to Paytm Sandbox with Order ID: {paytm_params['ORDER_ID']}..." 