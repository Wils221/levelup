from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    organizer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='events_created_by_user')
    name = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    attendees = models.ManyToManyField('Gamer', through='EventAttendees')

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value