from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_FORM = '''
<h2>IPL Match Ticket Booking</h2>
<form action="/paytm-initiate" method="POST">
    <input type="text" name="name" placeholder="Full Name" required><br><br>
    <input type="email" name="email" placeholder="Email" required><br><br>
    <input type="number" name="amount" value="500" readonly><br><br>
    <button type="submit">Pay Now with Paytm</button>
</form>
'''

@app.route('/pay')
def pay_route():
    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    app.run(debug=True)