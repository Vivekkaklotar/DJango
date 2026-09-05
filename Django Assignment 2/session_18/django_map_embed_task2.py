# views.py
from django.shortcuts import render

def show_restaurant_location(request):
    context = {
        'restaurant_name': 'Toscano - UB City',
        'lat': 12.9716,
        'lng': 77.5946,
        'api_key': 'YOUR_GOOGLE_MAPS_API_KEY'
    }
    return render(request, 'maps/restaurant_map.html', context)

<!-- templates/maps/restaurant_map.html -->
<h3>{{ restaurant_name }} Location</h3>
<iframe
  width="600"
  height="450"
  style="border:0"
  loading="lazy"
  allowfullscreen
  src="https://www.google.com/maps/embed/v1/place?key={{ api_key }}&q={{ lat }},{{ lng }}">
</iframe>