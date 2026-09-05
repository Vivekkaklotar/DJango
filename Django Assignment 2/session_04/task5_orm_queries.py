# Django Shell ORM Script (python manage.py shell)
from foodiespot.models import Restaurant, Cuisine

# Step 1: Create Cuisine objects
chinese = Cuisine.objects.create(name="Chinese", description="Delicious noodles, dim sums, and spicy manchurian")
italian = Cuisine.objects.create(name="Italian", description="Authentic pizzas and handcrafted pastas")

# Step 2: Create Restaurant objects
r1 = Restaurant.objects.create(name="Mainland China", location="MG Road, Bangalore", rating=4.5, cuisine=chinese)
r2 = Restaurant.objects.create(name="Toscano", location="UB City, Bangalore", rating=4.2, cuisine=italian)
r3 = Restaurant.objects.create(name="Fast Noodle Bar", location="Indiranagar", rating=3.8, cuisine=chinese)

# Step 3: Query restaurants with rating > 4.0
high_rated = Restaurant.objects.filter(rating__gt=4.0)

print("--- Restaurants Rated Above 4.0 ---")
for r in high_rated:
    print(f"Name: {r.name} | Rating: {r.rating} | Cuisine: {r.cuisine.name}")