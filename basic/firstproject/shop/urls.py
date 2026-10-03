from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop_home, name="shop-home"),
    path("products", views.shop_products, name="shop-products")
]