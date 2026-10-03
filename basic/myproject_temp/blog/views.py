from django.shortcuts import render
from datetime import datetime


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
def home(request):
    context = {
        "name": "Ranjan Kaumr",
        "age": 21,
        "skills": ["Python", "django", "c++", "Machine Learning", "AI"],
        "user": User("Nikhil", 30),
        "blog": {
            "title": "django Template Intro",
            "author": {
                "name": "Mohit Sinha",
                "address": "Bhopal-MP-462023"
            },
            "content": "<b> this is blod <b>",
            "created_at": datetime(2026, 4, 22, 21, 22)
        },
        "empty_value": None,
    }

    return render(request, "home.html", context)