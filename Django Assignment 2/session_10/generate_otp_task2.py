# views.py
import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail

def send_otp_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = str(random.randint(100000, 999999))
        
        # Save OTP in session
        request.session['otp'] = otp
        request.session['reset_email'] = email
        request.session.set_expiry(300) # 5 minutes expiry
        
        # Send Email
        send_mail(
            'Your Password Reset OTP',
            f'Your 6-digit OTP for password reset is: {otp}. Valid for 5 minutes.',
            'auth@app.com',
            [email]
        )
        return redirect('verify_otp')
    return render(request, 'accounts/forgot_password.html')