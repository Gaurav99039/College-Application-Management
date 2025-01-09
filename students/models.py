from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class StudentGrade(models.Model):
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    subject  = models.ForeignKey('Subject',on_delete=models.CASCADE)
    grade = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.grade}'

class Student(models.Model):
    #Personal information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
   

    extracurriculars_heading = models.CharField(max_length=100)
    extracurriculars_description = models.TextField()
    personal_essay = models.TextField()

    enrollment_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


