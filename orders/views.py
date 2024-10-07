from django.shortcuts import render, redirect
from . models import*
from products.models import*
from customers.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.


def cart(request):
      
    return render(request, 'cart.html')

def view_cart(request):
   
    return render(request,'cart.html')



def checkout(request):
    return render(request, 'checkout.html')




