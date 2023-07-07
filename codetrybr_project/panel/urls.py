from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home, name='panel-home'),
    path('about/',views.about_page, name='panel-about'),
    path('welcome/', views.welcome ,name='panel-welcome'),
    path('login/',views.login_view, name='panel-loginpage'),
    path('myadmin/',views.admin, name='panel-adminpage'),
    path('StdReg/',views.StdReg, name='panel-StdRegpage'),
    path('admReg/',views.admReg, name='panel-admRegpage'),
    path('tchReg/',views.tchReg, name='panel-tchRegpage'),
    path('clsReg/',views.clsReg, name='panel-clsRegpage'),
    path('subReg/',views.subReg, name='panel-subRegpage'),
    path('teach/',views.teach, name='panel-teachpage'),
    path('student/',views.student, name='panel-studentpage'),
    path('session/',views.sessionReg, name='panel-session'),
    path('logout/',views.Logout_view, name='panel-logout')
]