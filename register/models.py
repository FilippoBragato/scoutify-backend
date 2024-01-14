from django.db import models
from django.utils import timezone

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)
    location = models.CharField(max_length=100)
    terminated = models.BooleanField(default=False)
    
class ScoutPartecipation(models.Model):
    scout = models.ForeignKey("scout.Scout", on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    justification = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now, blank=True)
