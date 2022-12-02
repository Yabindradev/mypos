from django.shortcuts import render, redirect
from .models import *
from .forms import AddtoCartForm
from .order import Order
from django.contrib import messages

# Create your views here.

def base(request):
    return render (request, 'base/base.html')




def home(request):
    return render (request, 'base/home.html')



def menu(request):
    order = Order(request)
    product = Products.objects.all()
    
    if request.method == 'POST':
        form = AddtoCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            order.add(product_id=id,
                     quantity=quantity, update_quantity=True)
            print(order)
            messages.success(request, 'The product was added to the cart')
            
            remove_from_cart = request.GET.get('remove_from_cart', '')
            change_quantity = request.GET.get('change_quantity', '')
            quantity = request.GET.get('quantity', 0)
            
            if remove_from_cart:
                order.remove(remove_from_cart)

    #     # return redirect('menu')

    # if change_quantity:
    #     order.add(change_quantity, quantity, True)

    return render(request, 'base/menu.html', {'product': product})


def setting(request):
    return render (request, 'base/setting.html')

