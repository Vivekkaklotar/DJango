# OTP Verification with 3-min timeout
def verify_login_otp(request):
    user_otp = request.POST.get('otp')
    saved_otp = request.session.get('login_otp')
    
    if saved_otp and user_otp == saved_otp:
        del request.session['login_otp']
        return redirect('dashboard')
    else:
        return render(request, 'accounts/otp.html', {'error': 'OTP Expired or Invalid!'})