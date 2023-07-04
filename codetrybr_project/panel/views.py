from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Admin, Teacher, Student, Subject
from .forms import AdminRegistrationForm, TeacherRegistrationForm, StudentRegistrationForm, ClassRegistrationForm, SubjectRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, template_name="panel/index.html")

@login_required
def welcome(request):
    return render(request, template_name="panel/index.html")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    authenticated_user = authenticate(username=username, password=password)
                    login(request, authenticated_user)
                      # Redirect to a success page.
                   
                    return render(request,'panel/admin.html')
                else:
                    # Return an 'invalid login' error message.
                    form.add_error('password', 'Invalid username or password')
            except User.DoesNotExist:
                form.add_error('username', 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request,'panel/login.html',{'form':form})


@login_required
def admin(request):
    return render(request, 'panel/admin.html')


@login_required
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
    

@login_required
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


@login_required
def tchReg(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Teacher.objects.create(user=user, phone_number=form.cleaned_data['phone_number'])
            return render(request, 'panel/admin.html')  
    form = TeacherRegistrationForm()
    return render(request, "panel/tchReg.html", {'form':form})


@login_required
def clsReg(request):
    if request.method == 'POST':
        form = ClassRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'panel/admin.html')
    form = ClassRegistrationForm()
    return render(request, "panel/clsReg.html", {'form':form})


@login_required
def subReg(request):
    if request.method == 'POST':
        form = SubjectRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'panel/admin.html')
    form = SubjectRegistrationForm()
    return render(request, "panel/clsReg.html", {'form':form})
    


def Logout_view(request):
    logout(request)
    return render(request, 'panel/index.html')