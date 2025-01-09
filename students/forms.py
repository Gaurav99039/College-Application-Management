from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class StudentRegistrationFrom(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone', 'gpa', 'extracurriculars', 'personal_essay']