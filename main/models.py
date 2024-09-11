from django.db import models

# Create your models here.
class MoodEntry(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()