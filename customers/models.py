from django.db import models
from products.models import *


# Create your models customer.
class Customer(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200, null=True)
    password=models.CharField(max_length=200)
    confirmpassword=models.CharField(max_length=200,null=True)
    address=models.TextField()
    phone=models.IntegerField(default=0)


class Cart(models.Model):
    userid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    total_price=models.FloatField(default=0)
    status=models.BooleanField(default=False)


class Order(models.Model):
    
    address=models.TextField()
    phone=models.IntegerField(default=0)
    email=models.CharField(max_length=200, null=True)
    fname=models.CharField(max_length=200,null=True)
    lname=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    country=models.CharField(max_length=200,null=True)
    pin=models.IntegerField(default=0)
  
    
   
    
    


     


