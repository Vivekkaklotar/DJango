# foodiespot/admin.py
from django.contrib import admin
from .models import Restaurant, Cuisine

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'rating', 'location')