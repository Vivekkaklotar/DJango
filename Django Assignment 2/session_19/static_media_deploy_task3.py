# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Run in PythonAnywhere console:
python manage.py collectstatic --noinput

# In PythonAnywhere Static Files Section:
# URL: /static/ -> Directory: /home/yourusername/MyPlaylistApp/staticfiles
# URL: /media/  -> Directory: /home/yourusername/MyPlaylistApp/media