from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='panel-home'),
    path('welcome/', views.welcome ,name='panel-welcome'),
    path('login/',views.login_view, name='panel-loginpage'),
    path('myadmin/',views.admin, name='panel-adminpage'),
    path('StdReg/',views.StdReg, name='panel-StdRegpage'),
    path('admReg/',views.admReg, name='panel-admRegpage'),
    path('tchReg/',views.tchReg, name='panel-tchRegpage'),
]
