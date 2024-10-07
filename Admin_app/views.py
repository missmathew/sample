from django.shortcuts import render, redirect
from . models import*
from products.models import*
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from customers.models import *
# Create your views here.


def add_products(request):
    all_categories = Category.objects.all()
    
    if request.method =='POST':
        category_id=request.POST['category_id'] 
        title=request.POST['title']
        price=request.POST['price']
        description=request.POST['description']
        image=request.FILES['image']

        Product.objects.create(
          category_id=Category.objects.get(id=category_id),
          title=title,
          price=price,
          description=description,
          image=image  
        )

    return render(request, 'add_products.html', {'all_categories':all_categories})

def view_product_table(request):

    x=Product.objects.all()
    
    context={
        'table':x,
    }  
    

    return render (request, 'view_product_table.html', context)

def view_single_row(request, details):
    view_single=Product.objects.filter(id=details)
    context={
        'single':view_single,
    }
    return render(request,'view_single_row.html', context)



def view(request, view):
    details=Product.objects.filter(id=view)
    context={
        'view_edit':details,
    }
    return render(request, 'view.html', context) 

def update_details(request, datas):
    if request.method == 'POST':
        title=request.POST['title']
        price=request.POST['price']
        description=request.POST['description']
        image=request.FILES['image']
        

        Product.objects.filter(id=datas).update(
            title=title,
           price=price,
           description=description,
           image=image,
        )
        return redirect('view_product_table')
    return render(request, 'view.html')

def edit_product(request, edit):
    Product.objects.filter(id=edit).delete()
    return redirect('view_product_table')

def edit_product_image(request, product_image):

    if request.method=='POST':
        title=request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')

        

        try:
            image=request.FILES['image']
            fs = FileSystemStorage()
            file=fs.save(image.name, image)

        except MultiValueDictKeyError:
            file= Product.objects.get(id=product_image).image
        Product.objects.filter(id=product_image).update(
            title=title, price=price,
            description=description,
           
            image=file)
        
        return redirect('view_product_table')        

def category_list(request):

    if request.method =='POST':

        Category_Name=request.POST['Category_Name']
        Category.objects.create(
            Category_Name=Category_Name)
    return render(request, 'category_list.html')

def view_customer_details(request):

    y=Customer.objects.all()
    
    context={
        'customer_details':y,
    }  
    

    return render (request, 'view_customer_details.html', context)

def edit_customer_details(request, modify):
    Customer.objects.filter(id=modify).delete()
    return redirect('view_customer_details')


def table_data_table(request):
    return render(request, 'table_datatables.html')



    


        

