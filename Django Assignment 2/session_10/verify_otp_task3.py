# views.py
from django.shortcuts import render, redirect
from django.contrib import messages

def verify_otp_view(request):
    if request.method == 'POST':
        user_otp = request.POST['otp']
        session_otp = request.session.get('otp')
        
        if session_otp and user_otp == session_otp:
            messages.success(request, "OTP Verified! Enter new password.")
            return redirect('reset_password_page')
        else:
            messages.error(request, "Invalid or expired OTP. Please try again.")
            return render(request, 'accounts/verify_otp.html')
            
    return render(request, 'accounts/verify_otp.html')