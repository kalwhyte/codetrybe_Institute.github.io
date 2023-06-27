from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.admin import User
from .models import Admin
from .forms import AdminRegistrationForm
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
            pass
    else:
        form = AuthenticationForm()

    return render(request,'panel/login.html',{'form':form})


def admin(request):
    
    return render(request, template_name="panel/admin.html")

def register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Admin.objects.create(user=user, phone_number=form.cleaned_data['phone_number'])
            return redirect('panel-adminpage')  
    else:
        form = AdminRegistrationForm()
    return render(request,"panel/register.html", {'form':form})