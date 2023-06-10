from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    author = models.CharField(max_length=100)