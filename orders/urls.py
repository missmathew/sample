from django.urls import path
from orders import views

urlpatterns=[
    
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    
    

     
]