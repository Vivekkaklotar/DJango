# foodiespot/models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.name} - ({self.rating}★)" 