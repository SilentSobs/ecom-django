from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, default="Unnamed Product")

    description = models.TextField(max_length=200, default="No description provided")

    
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.CharField(max_length=200, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.name
    
