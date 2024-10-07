from django.db import models

# Create your models here.
class Category(models.Model):
    Category_Name=models.CharField(max_length=200)
    