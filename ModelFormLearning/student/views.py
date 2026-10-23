from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# Create your views here.

def list_of_students(request):
    students = Student.objects.all()

    return render(request, 'list_of_students.html', {'students': students})

def create_student(request):
    form = None
    error=None

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student:list_of_students")
        else:
            error = "validation error: form is not valid"
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form, 'error': error})

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    error = None
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:list_of_students')
        error = "form is unvaild"

    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {'form': form, 'error': error})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('student:list_of_students')

    return render(request, 'conform_delete_student.html', {'student': student})