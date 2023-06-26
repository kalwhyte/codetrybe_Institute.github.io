from django import forms
from django.contrib.auth.forms import UserCreationForm


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
    

class StudentRegistrationForm(UserCreationForm):
    """
    Student registration form fields
    """
    phone_number = forms.CharField(max_length=11)
    email = forms.EmailField()
    address = forms.CharField(max_length=50)
    level = forms.CharField(max_length=50)
    optional_subject = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    dob = forms.DateField()
    gender = forms.CharField(max_length=50)