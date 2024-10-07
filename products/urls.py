from django.urls import path
from products import views
urlpatterns=[
    path('index', views.index, name='index' ),
    path('view_products', views.view_products, name='view_products' ),
    path('sample', views.sample, name='sample' ),
    path('stand', views.stand, name='stand' )
]
