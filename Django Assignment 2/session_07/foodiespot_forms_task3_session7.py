# foodiespot/forms.py (Widget Customization)
from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine', 'rating', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Restaurant Name (e.g. Olive Garden)'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': '1.0', 'max': '5.0', 'step': '0.1'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City / Area Location'}),
        }