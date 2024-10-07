from django.shortcuts import render, redirect
from . models import*
from Admin_app.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def index(request):
    
    return render(request, 'menu.html')

def view_products(request):
    username = request.session.get('username')
    get_products=Product.objects.all()
    context={

        'get_my_products':get_products,
        'username':username
        
    }

    return render(request, 'products.html',context)    



def sample(request):
 
    username = request.session.get('username')

    list = Category.objects.all()
    get_products=Product.objects.all()

    context={
        'username':username,
        'items':list,
        'get_products':get_products
    }
    
    return render(request, 'sample.html',context) 

def stand(request):
    
    return render(request, 'stand.html')


