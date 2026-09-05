# foodiespot/forms.py
from django import forms

class AddRestaurantForm(forms.Form):
    restaurant_name = forms.CharField(label="Restaurant Name", max_length=100)
    cuisine_type = forms.CharField(label="Cuisine Type", max_length=50)
    contact_email = forms.EmailField(label="Contact Email")