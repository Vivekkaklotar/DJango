# foodiespot/admin.py
from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'rating', 'location')
    search_fields = ('name', 'cuisine__name', 'location')