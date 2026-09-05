import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0 # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c # Distance in km

def find_nearby_cafes(user_lat, user_lng, cafes):
    nearby = []
    for cafe in cafes:
        dist = haversine(user_lat, user_lng, cafe['lat'], cafe['lng'])
        if dist <= 3.0: # Within 3 km
            cafe['distance_km'] = round(dist, 2)
            nearby.append(cafe)
    return sorted(nearby, key=lambda x: x['distance_km'])

# Test Sample
cafes_list = [
    {'name': 'Cafe Coffee Day', 'lat': 12.972, 'lng': 77.595},
    {'name': 'Starbucks', 'lat': 12.980, 'lng': 77.600},
    {'name': 'Far Away Cafe', 'lat': 13.100, 'lng': 77.800},
]
print("Nearby Cafes:", find_nearby_cafes(12.9716, 77.5946, cafes_list))