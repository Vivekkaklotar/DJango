# Excluding gmail users
non_gmail_users = User.objects.exclude(email__icontains='gmail.com')