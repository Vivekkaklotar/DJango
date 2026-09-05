# middleware.py
from django.shortcuts import redirect

class BlockExpiredOTPAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Intercept access to OTP verification page
        if request.path == '/accounts/verify-otp/':
            if 'otp' not in request.session:
                return redirect('forgot_password') # Redirect if expired or missing
                
        response = self.get_response(request)
        return response