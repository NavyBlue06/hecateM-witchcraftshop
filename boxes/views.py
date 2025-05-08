from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def all_products(request):
    return render(request, 'boxes/all_products.html')  # make sure this template exists
