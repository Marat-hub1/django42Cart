from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *

def index (request):
    items=Tovar.objects.all()
    data={'items':items}
    return render(request, 'index.html', data)

def catalog (request,cat):
    items=Tovar.objects.filter(category__name=cat)
    data={'items':items}
    return render(request, 'index.html', data)
def cart(request):
    return render(request,'cart.html')

def cabinet(request):
    return render(request,'cabinet.html')