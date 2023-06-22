from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()



    

