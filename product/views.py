from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages
from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all()
    # return JsonResponse({'products': list(products.values())})
    return render(request, 'product/product_list.html', {'products': products})

def product_add(request):
    return render(request, 'product/product_form.html')

def product_delete(request,id):
    Product.objects.get(id=id).delete()
    return redirect('product_list')

def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        barcode = request.POST['barcode']
        price = request.POST['price']
        stock = request.POST['stock']
        # Cek apakah barcode sudah ada
        if Product.objects.filter(barcode=barcode).exists():
            messages.error(request, 'Barcode sudah digunakan, gunakan barcode lain.')
            return render(request, 'product/product_form.html', {'name': name, 'barcode': barcode, 'price': price, 'stock': stock})

        # Jika barcode unik, buat produk baru
        Product.objects.create(name=name, barcode=barcode, price=price, stock=stock)
        messages.success(request, 'Product created successfully!')
        
        return redirect('product_list')
    return render(request, 'product/product_form.html')
