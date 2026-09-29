from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Welcome to Blog Home Page <h1>")

def about(request):
    a = 10**2
    return HttpResponse(f"<h3> About Page = {a} <h3>")