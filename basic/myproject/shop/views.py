from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "shop/home.html")

def product(request):
    products = ["Laptop", "Charger", "Phone", "Book", "Pen", "Battery", "Clean kit", "etc.."]

    return render(request, "shop/products.html", {'products': products})
 