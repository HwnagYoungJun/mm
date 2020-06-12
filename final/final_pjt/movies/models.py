from django.db import models

# Create your models here.
class Genres(models.Model):
    title = models.TextField()

class Movies(models.Model):
    budget = models.FloatField()
    genre = models.ManyToMany(Genres, related_name='movie')
    movie_id = models.IntegerField()
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    production_companies = models.TextField()
    production_countries = models.TextField()
    release_date = models.CharField(max_length=30)
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    spoken_language = models.CharField(max_length=30)
    tagline = models.TextField()
    title = models.TextField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()