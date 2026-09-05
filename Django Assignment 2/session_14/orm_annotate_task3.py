from django.db.models import Count
from movies.models import Movie

movies_with_counts = Movie.objects.annotate(num_reviews=Count('reviews'))
for movie in movies_with_counts:
    print(f"Movie: {movie.title} | Total Reviews: {movie.num_reviews}")