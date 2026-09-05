# PythonAnywhere Deployment Walkthrough

1. Open PythonAnywhere Bash Console:
   $ git clone https://github.com/yourusername/MyPlaylistApp.git
   $ cd MyPlaylistApp
   $ mkvirtualenv --python=/usr/bin/python3.10 myenv
   $ pip install django

2. Configure Web Tab:
   - Source code path: /home/yourusername/MyPlaylistApp
   - Virtualenv path: /home/yourusername/.virtualenvs/myenv

3. Update WSGI Configuration File (/var/www/yourusername_pythonanywhere_com_wsgi.py):
   import os
   import sys
   path = '/home/yourusername/MyPlaylistApp'
   if path not in sys.path:
       sys.path.append(path)
   os.environ['DJANGO_SETTINGS_MODULE'] = 'foodiehub_project.settings'
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()