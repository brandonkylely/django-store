from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    # tags to be added later
