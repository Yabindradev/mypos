from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    pass

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Products(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField()
    refrence = models.TextField(blank = True)


class Order_products(models.Model):
    pass