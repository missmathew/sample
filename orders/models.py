from django.db import models
from products.models import*
from customers.models import*
# Create your models order.


    

# class Order(models.Model):
#     product_id=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     quantity=models.IntegerField(default=0)
#     user_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)
   