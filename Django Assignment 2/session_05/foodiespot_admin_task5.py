# foodiespot/admin.py (Complete Customization)
from django.contrib import admin
from .models import Restaurant, Cuisine

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'rating', 'location')
    search_fields = ('name', 'cuisine__name', 'location')
    list_filter = ('cuisine', 'rating')
    list_per_page = 10

@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')