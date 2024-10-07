from django.urls import path
from customers import views

urlpatterns=[
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('my_cart', views.my_cart, name='my_cart'),
    path('remove_from_cart/<int:remove>', views.remove_from_cart, name='remove_from_cart'),
    path('view_order', views.view_order, name='view_order'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('user_cartclear', views.user_cartclear, name='user_cartclear'),
    path('number', views.number, name='number'),
]