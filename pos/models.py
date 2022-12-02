from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField()
    refrence = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now=True)
    
    
       
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']

class Order_products(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    sell_time = models.DateTimeField(auto_now=True)
    
    
    
       
    def __str__(self):
        return str(self.id)
    