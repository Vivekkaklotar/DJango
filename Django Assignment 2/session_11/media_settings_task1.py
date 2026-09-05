# settings.py
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'user_uploads')

# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... existing routes
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)