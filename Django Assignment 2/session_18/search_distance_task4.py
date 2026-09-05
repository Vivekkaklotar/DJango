# views.py
from django.shortcuts import render
from .haversine import find_nearby_cafes

PICKUP_POINTS = [
    {'name': 'Flipkart Hub Indiranagar', 'lat': 12.9784, 'lng': 77.6408},
    {'name': 'Flipkart Hub Koramangala', 'lat': 12.9352, 'lng': 77.6245},
    {'name': 'Flipkart Hub MG Road', 'lat': 12.9756, 'lng': 77.6066},
    {'name': 'Flipkart Hub Whitefield', 'lat': 12.9698, 'lng': 77.7500},
    {'name': 'Flipkart Hub Jayanagar', 'lat': 12.9250, 'lng': 77.5938},
]

def search_by_distance(request):
    user_lat = float(request.GET.get('lat', 12.9716))
    user_lng = float(request.GET.get('lng', 77.5946))
    
    sorted_points = find_nearby_cafes(user_lat, user_lng, PICKUP_POINTS)
    return render(request, 'maps/pickup_points.html', {'points': sorted_points})