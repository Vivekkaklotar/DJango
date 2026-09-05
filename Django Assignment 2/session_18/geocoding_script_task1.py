import requests

def geocode_address(address, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url).json()
    
    if response['status'] == 'OK':
        location = response['results'][0]['geometry']['location']
        print(f"Address: {address}")
        print(f"Latitude: {location['lat']}")
        print(f"Longitude: {location['lng']}")
        return location['lat'], location['lng']
    else:
        print("Geocoding failed:", response['status'])
        return None, None

# Example Usage:
# geocode_address("IIM Ahmedabad, Gujarat", "YOUR_API_KEY")