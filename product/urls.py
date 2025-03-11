from django.urls import path
from .views import product_list,product_add,product_edit,product_delete, product_create,product_update

urlpatterns = [
    path('product/', product_list, name='product_list'),
    path('product/add', product_add, name='product_add'),
    path('product/delete/<str:id>/', product_delete, name='product_delete'),
    path('product/edit/<str:id>/', product_edit, name='product_edit'),
    path('product/create/', product_create, name='product_create'),
    path('product/update/', product_update, name='product_update'),
]
