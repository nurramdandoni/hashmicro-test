from django.shortcuts import render, redirect
from .models import Module
from django.contrib import messages
from django.http import JsonResponse

def module_list(request):
    modules = Module.objects.all()
    # Module.objects.create(name="product", installed=True)
    # Module.objects.get(name="example_module").delete()
    # return JsonResponse({'modules': list(modules.values())})
    return render(request, 'engine/module_list.html', {'modules': modules})

def install_module(request, module_name):
    module, created = Module.objects.get_or_create(name=module_name)
    module.installed = True
    module.save()
    messages.success(request, f'Module {module_name} installed successfully!')
    return redirect('module_list')

def uninstall_module(request, module_name):
    module = Module.objects.get(name=module_name)
    module.installed = False
    module.save()
    messages.success(request, f'Module {module_name} uninstalled successfully!')
    return redirect('module_list')
