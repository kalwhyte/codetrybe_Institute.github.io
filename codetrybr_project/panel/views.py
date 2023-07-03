from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.admin import User
from .models import Admin, Teacher, Student, Subject
from .forms import AdminRegistrationForm, TeacherRegistrationForm, StudentRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, template_name="panel/index.html")


def welcome(request):
    return render(request, template_name="panel/index.html")


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    # Redirect to a success page.
                    return redirect('panel-adminpage')
                else:
                    # Return an 'invalid login' error message.
                    form.add_error('password', 'Invalid username or password')
            except User.DoesNotExist:
                form.add_error('username', 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request,'panel/login.html',{'form':form})


def admin(request):
    return render(request, 'panel/admin.html')

def StdReg(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists')
                return render(request, "panel/StdReg.html", {'form':form})
            
            # Save the user first
            user = form.save()

            # Retrieve the other fields
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            address=form.cleaned_data['address']
            level=form.cleaned_data['level']
            optional_subject=form.cleaned_data['optional_subject']
            dob=form.cleaned_data['dob']
            gender=form.cleaned_data['gender']

            # Create a student object
            student = Student.objects.create(
                user=user,
                phone_number=phone_number,
                email=email,
                address=address,
                level=level,
                optional_subject=optional_subject,
                dob=dob,
                gender=gender
            )

            # Redirect to the home page
            return redirect('panel/admin.html')
        
    # If the request is a GET request, create an empty form instance and render it    
    form = StudentRegistrationForm()
    return render(request, "panel/StdReg.html", {'form':form})
    

def admReg(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']

            Admin.objects.create(user=user, phone_number=phone_number)
            return redirect('panel-admRegpage')  
    form = AdminRegistrationForm()
    return render(request, "panel/admReg.html", {'form':form})


def tchReg(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Admin.objects.create(user=user, phone_number=form.cleaned_data['phone_number'])
            return redirect('panel-tchRegpage')  
    form = TeacherRegistrationForm()
    return render(request, template_name="panel/tchReg.html")