from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL

# Create your models here.
class Scout(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, default=None, null=True, blank=True)
    name = models.CharField(max_length=20)
    birthday = models.DateField()
    patrol = models.ForeignKey("scout.Patrol", blank=True, null=True, on_delete=models.SET_NULL)
    verified = models.BooleanField(default=False)

class Patrol(models.Model):
    name = models.CharField(max_length=20)
    urlo = models.CharField(max_length=100)