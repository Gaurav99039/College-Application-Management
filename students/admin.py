from django.contrib import admin
from .models import Student,StudentGrade,Subject
# Register your models here.

admin.site.register(Student)
admin.site.register(StudentGrade)
admin.site.register(Subject)