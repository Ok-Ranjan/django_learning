from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post = {
        "title": "My Second Templates Post",
        "descriptions": "Django is a high-level Python web framwork",
        "author": "Ranjan Khuswaha",
        "created_at": datetime(2026, 4, 22, 23, 31),
        "comments_count": 5,
        "tags": ["Dajngo", "Python", "Web Development"],
    }

    return render(request, "blog/blog_details.html", {"post": post})
