from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
