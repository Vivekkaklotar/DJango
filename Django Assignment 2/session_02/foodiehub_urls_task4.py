# foodiehub_project/urls.py
from django.contrib import admin
from django.urls import path
from playlists.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', home, name='music_home'),
]