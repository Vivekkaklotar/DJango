# AI-Drafted & Verified OTP Model & Logic
from django.db import models
from django.utils import timezone
import datetime

class SMSOTPVerification(models.Model):
    phone_number = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_valid(self):
        # Expiry set to 3 minutes (180 seconds)
        now = timezone.now()
        return not self.is_verified and (now - self.created_at) < datetime.timedelta(minutes=3)