from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'age', 'email']

        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Enter your name"}
            ),
            "age": forms.NumberInput(
                attrs={"min": 1}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Enter your email"}
            ),
        }

        labels = {
            "name": "Full Name",
            "Age": "Your Age",
            "Email": "Email Address",
        }

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 16:
            raise forms.ValidationError(
                "Student must be at least 16 years old."
            )

        return age