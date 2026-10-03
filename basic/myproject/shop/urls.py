from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="shop_home"),
    path('products', views.product, name="shop_prodcuts")

]