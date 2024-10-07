from django.shortcuts import  render, redirect
from . models import*
from products.models import*
from orders.models import*
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def login(request):
     
    if request.method =='POST':
        
        username = request.POST['username']
        password = request.POST['password']
        if Customer.objects.filter(username=username, password=password).exists():
            data = Customer.objects.filter(username=username, password=password).values('id','username','email','phone').first()
            request.session['u_id']=data['id']
            request.session['username']=data['username']
            request.session['email']=data['email']
            request.session['phone']=data['phone']
            return redirect('sample')
                    
        else:
            print('----------')
        
    return render(request, 'login.html')


def register(request):

    if request.method =='POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        address = request.POST['address']
        phone = request.POST['phone']


        if Customer.objects.filter(password=password,email=email).exists():
            
                Customer.objects.create(
                    username=username,
                    email=email,
                    password=password,
                    confirmpassword=confirmpassword,
                    address=address,
                    phone = phone

                )
        else:
            return redirect('login')
            
    return render(request, 'register.html')

def logout(request):
     if 'username' in request.session:
         request.session.flush()
     return redirect('sample')

def add_to_cart(request):
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
     
    if request.method=='POST':
         print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
         product_id=request.POST['product_id']
         quantity=request.POST['quantity']
         userid=request.session.get('u_id')
         total_price=Product.objects.get(id=product_id).price
    
         if not Cart.objects.filter(product_id=product_id, userid=userid, status=True).exists():
            print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
            Cart.objects.create(
                    product_id=Product.objects.get(id=product_id),
                    userid=Customer.objects.get(id=userid),
                    quantity=quantity,
                    total_price=float(total_price) * int(quantity)     
            )
            
         else:
            print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
            item=Cart.objects.get(product_id=product_id, userid=userid)

            item.quantity+=1
            item.save()
    
         return redirect ('my_cart')
    return render(request, 'product.html')


def my_cart(request):
     
     user_id=request.session.get('u_id')
     cart_details=Cart.objects.filter(userid=user_id, status=False)
     
     sub_total=sum(m.product_id.price * m.quantity for m in cart_details)
     
     context={
          'cart_details':cart_details,
          'sub_total' : sub_total,   
          'user_id':user_id
     }
     return render(request, 'cart.html', context)
      

def remove_from_cart(request,remove):
    Cart.objects.filter(id=remove).delete()
    return redirect('my_cart')

  
def view_order(request):

     if request.method=='POST':
         email = request.POST['email']
         address = request.POST['address']
         phone = request.POST['phone']
         fname=request.POST['fname']
         lname=request.POST['lname']
         city=request.POST['city']
         country=request.POST['country']
         pin=request.POST['pin']

     
         Order.objects.create(
              
                    email=email,
                    address=address,
                    phone=phone,
                    fname=fname,
                    lname=lname,    
                    city=city,
                    country=country,
                    pin=pin

            )
     customer_id=request.session.get('u_id')
     cart_order=Cart.objects.filter(userid=customer_id, status=False)
     cart_order_two=Cart.objects.filter(userid=customer_id, status=False)
     total=sum(m.product_id.price * m.quantity for m in cart_order)
     cart_order_two.update(status=True)
     context={
        'customer_id':customer_id,
        'cart_order':cart_order,
        'total':total,
        
    }
    
     return render(request, 'checkout.html', context)


def my_orders(request):
    view_orders=Order.objects.all()
    context={
        'view_orders':view_orders
    }
    return render(request,'myorders.html', context)

def user_cartclear(request):
    user_id=request.session.get('u_id')
    Cart.objects.filter(userid=user_id).update()
    messages.success(request, 'your order has been placed successfully')
    return redirect('sample')

def number(request):
    number = 20
    if number>=0:
        return HttpResponse('positive')
    else:
        return HttpResponse('negative')


 
    


    
     