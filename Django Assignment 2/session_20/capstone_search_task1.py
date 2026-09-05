# views.py
from django.shortcuts import render
from .models import Restaurant

def search_restaurants(request):
    cuisine = request.GET.get('cuisine', '')
    location = request.GET.get('location', '')
    
    results = Restaurant.objects.all()
    if cuisine:
        results = results.filter(cuisine__name__icontains=cuisine)
    if location:
        results = results.filter(location__icontains=location)
        
    return render(request, 'capstone/search_results.html', {'results': results})