# foodiespot/views.py
from django.shortcuts import render, redirect
from .forms import RestaurantForm

def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save() # Saves object to database
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'foodiespot/restaurant_form.html', {'form': form})