# foodiespot/admin.py
from django.contrib import admin
from .models import Restaurant, Cuisine

admin.site.register(Cuisine)
admin.site.register(Restaurant)