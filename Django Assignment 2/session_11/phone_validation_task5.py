# forms.py
from django import forms
from django.core.exceptions import ValidationError
import re

class ProfileForm(forms.ModelForm):
    class Meta:
        model = InfluencerProfile
        fields = ['display_name', 'bio', 'profile_pic', 'phone_number']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone:
            if not re.match(r'^\d{10}$', phone):
                raise ValidationError("Phone number must be exactly 10 numeric digits.")
        return phone