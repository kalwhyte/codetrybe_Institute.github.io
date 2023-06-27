from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='panel-home'),
    path('welcome/', views.welcome ,name='panel-welcome'),
    path('login/',views.login, name='panel-loginpage'),
    path('myadmin/',views.admin, name='panel-adminpage'),
    path('register/',views.register, name='panel-registerpage'),
]
