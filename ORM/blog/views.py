from django.shortcuts import render
from .models import Student

# Create your views here.

def blog(request):
    return render(request, 'blog/blog.html')

def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'blog/student_list.html', context)
