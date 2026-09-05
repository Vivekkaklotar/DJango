# Step 1: Generate migration files
python manage.py makemigrations foodiespot

# Output:
# Migrations for 'foodiespot':
#   foodiespot/migrations/0001_initial.py
#     - Create model Cuisine
#     - Create model Restaurant

# Step 2: Apply migrations to create DB tables
python manage.py migrate

# Output:
# Running migrations:
#   Applying foodiespot.0001_initial... OK