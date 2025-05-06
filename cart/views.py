from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def cart_view(request):
    return render(request, 'cart/cart.html')

