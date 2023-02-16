from django.db import models
from django.contrib.auth.models import User



class EventAttendees(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)