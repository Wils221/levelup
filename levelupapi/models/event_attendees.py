from django.db import models
from django.contrib.auth.models import User



class Event_Attendees(models.Model):

    gamer = models.ForeignKey("Game", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)