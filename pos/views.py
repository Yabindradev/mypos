from django.shortcuts import render

# Create your views here.

def base(request):
    return render (request, 'base/base.html')




def home(request):
    return render (request, 'base/home.html')



def menu(request):
    return render (request, 'base/menu.html')


def setting(request):
    return render (request, 'base/setting.html')

