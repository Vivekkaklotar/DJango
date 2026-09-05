# Setup script (python manage.py shell)
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from movies.models import Review

content_type = ContentType.objects.get_for_model(Review)

# Permissions
can_add = Permission.objects.get(codename='add_review', content_type=content_type)
can_change = Permission.objects.get(codename='change_review', content_type=content_type)
can_view = Permission.objects.get(codename='view_review', content_type=content_type)

# Create Groups
critic_group, _ = Group.objects.get_or_create(name='MovieCritic')
critic_group.permissions.set([can_add, can_change, can_view])

fan_group, _ = Group.objects.get_or_create(name='MovieFan')
fan_group.permissions.set([can_view])