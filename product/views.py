from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        barcode = request.POST['barcode']
        price = request.POST['price']
        stock = request.POST['stock']
        Product.objects.create(name=name, barcode=barcode, price=price, stock=stock)
        messages.success(request, 'Product created successfully!')
        return redirect('product_list')
    return render(request, 'product/product_form.html')
