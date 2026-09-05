# playlists/views.py (Updated with Name)
from django.http import HttpResponse

def home(request):
    user_name = "Alex"
    return HttpResponse(f"<h1>Welcome to My Spotify Playlists, created by {user_name}!</h1>")