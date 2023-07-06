from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home, name='panel-home'),
    path('welcome/', views.welcome ,name='panel-welcome'),
    path('login/',views.login_view, name='panel-loginpage'),
    path('myadmin/',views.admin, name='panel-adminpage'),
    path('StdReg/',views.StdReg, name='panel-StdRegpage'),
    path('admReg/',views.admReg, name='panel-admRegpage'),
    path('tchReg/',views.tchReg, name='panel-tchRegpage'),
    path('clsReg/',views.clsReg, name='panel-clsRegpage'),
    path('subReg/',views.subReg, name='panel-subRegpage'),
    path('logout/',views.Logout_view, name='panel-logout')
]
