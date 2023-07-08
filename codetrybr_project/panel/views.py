from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Admin, Teacher, Student, Subject,StdClass
from .forms import AdminRegistrationForm, TeacherRegistrationForm, StudentRegistrationForm, ClassRegistrationForm, SubjectRegistrationForm,SessionCreationForm
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

                    # if user is admin
                    try:
                        admin_instance = Admin.objects.get(user=user)
                        return render(request, 'panel/admin.html', {"admin_instance": admin_instance})
                    except Admin.DoesNotExist:
                        pass

                    try:
                        teacher_instance = Teacher.objects.get(user=user)
                        return render(request, 'panel/teach.html', {"teacher_instance": teacher_instance})
                    except Teacher.DoesNotExist:
                        pass

                    try:
                        student_instance = Student.objects.get(user=user)
                        return render(request, 'panel/student.html', {"student_instance": student_instance})
                    except Student.DoesNotExist:
                        pass
                    return render(request,"panel/admin.html")
                    

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
            
            try:
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']
                if password!= confirm_password:
                    messages.error(request,"unmatching password")
                    return render(request, "panel/StdReg.html", {'form':form})
                username = form.cleaned_data['username']
                try:
                    data = User.objects.get(username=username)
                    messages.error(request, "Username already exists")
                    return render(request, "panel/StdReg.html", {'form': form})
                except User.DoesNotExist:
                    pass
                user = form.save(commit=False)
                phone_number=form.cleaned_data['phone_number']
                email=form.cleaned_data['email']
                address=form.cleaned_data['address']
                dob=form.cleaned_data['dob']
                gender=form.cleaned_data['gender']
                user.save()
                student =  Student.objects.create(
                    user=user,
                    phone_number=phone_number,
                    email=email,
                    address=address,
                    dob=dob,
                    gender=gender
                )
            except ValueError:
    # Silencing the ValueError
                pass
            except Exception as e:
            # Handle other exceptions
                 raise e
                # Redirect to the home page
            messages.success(request,"student successfully created")
            return render(request, "panel/admin.html") 
    # If the request is a GET request, create an empty form instance and render it    
    form = StudentRegistrationForm()
    return render(request, "panel/StdReg.html", {'form': form, 'messages': messages.get_messages(request)})
    

@login_required
def admReg(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.instance.role = "admin"
            user = form.save()
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            address=form.cleaned_data['address']

            Admin.objects.create(user=user, phone_number=phone_number,email=email,address=address)
            return redirect('panel-admRegpage')  
    form = AdminRegistrationForm()
    return render(request, "panel/admReg.html", {'form':form})


@login_required
def tchReg(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.instance.role = "teacher"
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
def sessionReg(request):
    if request.method == 'POST':
        form = SessionCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'panel/admin.html')
    form = SessionCreationForm()
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
    

@login_required
def teach(request):
    return render(request, 'panel/teach.html')


def about_page(request):
    return render(request, template_name="panel/about.html")


@login_required
def student(request):
    # user = User.objects.get(username)
    # student_instance = Student.objects.get(user=user)
    return render(request, 'panel/student.html')


def Logout_view(request):
    logout(request)
    return render(request, 'panel/index.html')


@login_required
def all_student(request):
    student_list = Student.objects.all()
    return render(request, 'panel/all_student.html', {'student_list': student_list})

@login_required
def all_teachers(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'panel/all_teachers.html', {'teacher_list': teacher_list})


@login_required
def all_admin(request):
    admin_list = Admin.objects.all()
    return render(request,'panel/all_admin.html', {'admin_list': admin_list})


@login_required
def all_class(request):
    class_list = StdClass.objects.all()
    return render(request, 'panel/all_class.html', {'class_list': class_list})

@login_required
def all_subject(request):
    subject_list = Subject.objects.all()
    return render(request, 'panel/all_subject.html', {'subject_list': subject_list})