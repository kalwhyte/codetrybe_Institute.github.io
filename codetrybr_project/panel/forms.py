from django import forms
from django.contrib.auth.forms import UserCreationForm


class AdminRegistrationForm(UserCreationForm):
    """
    adding extra field to the User created form
    to create a User named Admin
    admin registration form 
    """
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=50)


class TeacherRegistrationForm(UserCreationForm):
    """
    adding extra field to the User created form
    to create a User named Admin
    Teacher registration form 
    """
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=50)
    

class StudentRegistrationForm(UserCreationForm):
    """
    adding extra field to the User created form
    to create a User named Admin
    Student registration form 
    """
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=50)



