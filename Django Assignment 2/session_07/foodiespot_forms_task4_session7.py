# foodiespot/forms.py (Complete Validation)
from django import forms
from django.core.exceptions import ValidationError
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine', 'rating', 'location']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError("Restaurant name must contain at least 3 characters.")
        return name

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1.0 or rating > 5.0:
            raise ValidationError("Rating must be strictly between 1.0 and 5.0.")
        return rating