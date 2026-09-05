# foodiespot/models.py (Updated with Cuisine and ForeignKey)
from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    rating = models.FloatField()
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='restaurants', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.cuisine.name if self.cuisine else 'No Cuisine'}) - {self.rating}★" 