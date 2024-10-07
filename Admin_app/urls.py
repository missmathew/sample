from django.urls import path
from Admin_app import views

urlpatterns=[
    
    path('add_products', views.add_products, name='add_products'),
    path('view_product_table', views.view_product_table, name='view_product_table'),
    path('view/<int:view>', views.view, name='view'),
    path('edit_product/<int:edit>', views.edit_product, name='edit_product'),
    path('edit_product_image/<int:product_image>', views.edit_product_image, name='edit_product_image'),
    path('view_single_row/<int:details>', views.view_single_row, name='view_single_row'),
    path('update_details/<int:datas>', views.update_details, name='update_details'),
    path('category_list', views.category_list, name='category_list'),
    path('view_customer_details', views.view_customer_details, name='view_customer_details'),
    path('edit_customer_details/<int:modify>', views.edit_customer_details, name='edit_customer_details'),
    path('table_data_table', views.table_data_table, name='table_data_table')
    ]