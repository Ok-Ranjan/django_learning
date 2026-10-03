from django.shortcuts import render

def shop_home(request):
    return render(request, "shop/home_page.html")

def shop_products(request):
    return render(request, "shop/products.html")