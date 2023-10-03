from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField(default=1) 
    price = models.IntegerField()
    description = models.TextField()
    category = models.TextField()
    image = models.ImageField(upload_to='product_images/')