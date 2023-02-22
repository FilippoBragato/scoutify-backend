from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    authors = models.ManyToManyField("scout.Scout", blank=True)