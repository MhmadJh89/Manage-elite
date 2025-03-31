from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    if request.method == 'POST':
        add_device = DeviceForm(request.POST, request.FILES)
        if add_device.is_valid():
            add_device.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
            
    context = {
        'devices': Device.objects.all(),
        'category': Category.objects.all(),
        'form': DeviceForm(),
        'formcat': CategoryForm(),
        'alldevices': Device.objects.filter(active=True).count(),
        'allsold': Device.objects.filter(status='sold').count(),
        'allrental': Device.objects.filter(status='rental').count(),
        'allavailable': Device.objects.filter(status='available').count(),
    }
    
    return render(request, 'pages/index.html', context)

def devices(request):
    search = Device.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
        
    context = {
        'devices': search,
        'cat': Category.objects.all(),
        'formcat': CategoryForm(),
    }
    
    return render(request, 'pages/devices.html', context)

def update(request, id):
    device_id = Device.objects.get(id=id)
    if request.method == 'POST':
        device_save = DeviceForm(request.POST, request.FILES, instance=device_id)
        if device_save.is_valid():
            device_save.save()
            return redirect('/')
    else:
        device_save = DeviceForm(instance=device_id)
    context = {
        'form':device_save,
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    device_delete = Device.objects.get(id=id)
    if request.method == 'POST':
        device_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')