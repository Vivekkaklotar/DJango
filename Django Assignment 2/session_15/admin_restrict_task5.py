# admin.py
from django.contrib import admin
from .models import Playlist

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.groups.filter(name='Admin').exists() or request.user.is_superuser