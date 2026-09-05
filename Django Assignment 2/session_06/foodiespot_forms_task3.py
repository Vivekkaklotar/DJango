# foodiespot/forms.py (With Validation)
from django import forms
from django.core.exceptions import ValidationError

class AddRestaurantForm(forms.Form):
    restaurant_name = forms.CharField(label="Restaurant Name", max_length=100)
    cuisine_type = forms.CharField(label="Cuisine Type", max_length=50)
    contact_email = forms.EmailField(label="Contact Email")

    def clean_restaurant_name(self):
        name = self.cleaned_data.get('restaurant_name')
        if len(name) < 3:
            raise ValidationError("Restaurant name must be at least 3 characters long.")
        return name