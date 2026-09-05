# foodiehub_project/__init__.py
import pymysql
pymysql.install_as_MySQLdb()

# foodiehub_project/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'foodiespot_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}