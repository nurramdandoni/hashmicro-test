from django.shortcuts import redirect
from django.urls import resolve
from .models import Module

class ModuleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url_name = resolve(request.path_info).url_name

        # cek apakah modul example_module sudah di-install
        if url_name in ['product_list', 'product_create']:
            module = Module.objects.filter(name="product", installed=True).first()
            if not module:
                return redirect('/module/')  # Redirect ke halaman module

        response = self.get_response(request)
        return response
