from django.shortcuts import render
from django.http import HttpResponse

def base_page(request):
    return render(request, "base.html")

def home(request):
    return render(request, "blog/home.html")

def about(request):
    return HttpResponse("Blog <b>About<b> Page")

def user_profile(request, username):
    return HttpResponse(f"Username = {username}")

def post_details(request, post_id=1):
    posts = [("Ranjan", "djnedwemssd"), ("Nikhil", "jnciwksmdcldk"), ("Banti", "dnwxmwkmwkem"), ("Golu", "dsvnsdc kjc cks"), ("Mukesh", "Sdwikmfrpwrfv dc,wl"), ("NandJi", "kfvfnjdnc sdjcnwlmsxs")]  
    
    post_showing = None

    if(post_id <= len(posts)):
        return HttpResponse(f"Post details: <br> username={posts[post_id-1][0]} <br> content={posts[post_id-1][1]}")

    return HttpResponse(f"Post-Id is worng")
        

def article_by_year(request, year):
    return HttpResponse(f"Year = {year}")

def article_by_date(request, date):
    return HttpResponse(f"Year = {date}")

def article_details(request, **kwargs):
    return HttpResponse(f"<h1> Articles from Date: {kwargs}")