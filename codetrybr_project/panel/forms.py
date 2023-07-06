from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Teacher, Admin, Subject, StdClass
from django.db import models





class AdminRegistrationForm(UserCreationForm):
    """
    adding extra field to the User created form
    to create a User named Admin
    admin registration form 
    """
    phone_number = forms.CharField(max_length=11)
    email = forms.EmailField()
    address = forms.CharField(max_length=50)


class TeacherRegistrationForm(UserCreationForm):
    """
    Teacher registration form fields
    """
    phone_number = forms.CharField(max_length=11)
    email = forms.EmailField()
    address = forms.CharField(max_length=50)
    
GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]
class StudentRegistrationForm(UserCreationForm):
    """
    Student registration form fields
    """
    class Meta:
        model = Student
        fields = '__all__'

class ClassRegistrationForm(forms.ModelForm):
    """
    Class registration form fields
    """
    class Meta:
        model = StdClass
        fields = '__all__'

class SubjectRegistrationForm(forms.ModelForm):
    """
    Subject registration form fields
    """
    class Meta:
        model = Subject
        fields = '__all__'