from django.urls import path
from .views import product_list,product_add,product_edit,product_delete, product_create,product_update

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/add', product_add, name='product_add'),
    path('products/delete/<str:id>/', product_delete, name='product_delete'),
    path('products/edit/<str:id>/', product_edit, name='product_edit'),
    path('products/create/', product_create, name='product_create'),
    path('products/update/', product_update, name='product_update'),
]
