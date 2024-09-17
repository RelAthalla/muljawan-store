from django.db import models
import uuid

# Create your models here.
class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    time = models.DateField(auto_now_add=True)
    