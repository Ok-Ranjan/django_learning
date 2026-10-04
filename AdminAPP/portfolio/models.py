from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    bio = models.TextField()
    location = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return str(self.location)