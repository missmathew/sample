from django.db import models
from Admin_app.models import *

# Create your models product.
class Product(models.Model):
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='image')
    
