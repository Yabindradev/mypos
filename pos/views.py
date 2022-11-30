from django.shortcuts import render
from .models import *

# Create your views here.

def base(request):
    return render (request, 'base/base.html')




def home(request):
    return render (request, 'base/home.html')



def menu(request):
    product = Products.objects.all()
    return render (request, 'base/menu.html', {'product':product})


def setting(request):
    return render (request, 'base/setting.html')

