# foodiespot/views.py
from django.shortcuts import render
from .forms import AddRestaurantForm

def add_restaurant_view(request):
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST)
        if form.is_valid():
            # Process cleaned data
            data = form.cleaned_data
            return render(request, 'foodiespot/success.html', {'data': data})
    else:
        form = AddRestaurantForm()
        
    return render(request, 'foodiespot/add_restaurant.html', {'form': form})