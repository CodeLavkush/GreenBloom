from django.db import models
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    PLANT_CATEGORY = [
        ('HP', 'Highted Pot'),
        ('SM', 'Small Pot'),
        ('FP', 'Fat Pot'),
    ]
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/")
    desc = models.TextField(max_length=400)
    category = models.CharField(max_length=2, choices=PLANT_CATEGORY)
    stock = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name