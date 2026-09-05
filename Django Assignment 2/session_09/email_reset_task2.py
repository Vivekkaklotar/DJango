# views.py
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse

def send_password_reset_email(request, user_email):
    reset_url = f"http://127.0.0.1:8000/accounts/reset/token12345/"
    subject = "Password Reset Request - Paytm Clone"
    message = f"Hello,\n\nYou requested a password reset. Click link below to reset:\n{reset_url}\n\nIf you did not request this, please ignore."
    
    send_mail(subject, message, 'noreply@paytm.com', [user_email])
    return HttpResponse("Password reset email sent successfully!")