from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Mood(models.Model):
    mood = models.CharField(max_length=100)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(default=date.today)
    streak = models.SmallIntegerField(null = True)

