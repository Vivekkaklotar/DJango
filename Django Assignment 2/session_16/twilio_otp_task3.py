from twilio.rest import Client
import random
from django.shortcuts import render, HttpResponse

def send_twilio_otp(request):
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    twilio_number = '+1234567890'
    
    user_phone = '+919876543210' # Target user mobile number
    otp = str(random.randint(100000, 999999))
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your Verification OTP is: {otp}",
        from_=twilio_number,
        to=user_phone
    )
    
    return HttpResponse(f"OTP sent successfully via Twilio! SID: {message.sid}")