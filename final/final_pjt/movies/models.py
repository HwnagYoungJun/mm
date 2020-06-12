from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)


class Production_company(models.Model):
    name = models.CharField(max_length=100)


class Production_country(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    genre = models.ManyToManyField(Genre, related_name='movies')
    production_company = models.ManyToManyField(Production_company, related_name='movies')
    production_country = models.ManyToManyField(Production_country, related_name='movies')
    budget = models.FloatField()
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    production_companies = models.TextField()
    production_countries = models.TextField()
    release_date = models.CharField(max_length=30)
    revenue = models.FloatField()
    runtime = models.FloatField()
    spoken_language = models.CharField(max_length=30)
    tagline = models.TextField()
    title = models.TextField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()