from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.list_of_students, name='list_of_students'),
    path('create/', views.create_student, name='create_student'),
    path('update/<int:student_id>', views.update_student, name='update_student'),
    path('delete/<int:student_id>', views.delete_student, name='delete_student'),
]