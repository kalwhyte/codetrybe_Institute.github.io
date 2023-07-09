from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home, name='panel-home'),
    path('about/',views.about_page, name='panel-about'),
    path('welcome/', views.welcome ,name='panel-welcome'),
    path('login/',views.login_view, name='panel-loginpage'),
    path('myadmin/',views.admin, name='panel-adminpage'),
    path('teach/',views.teacher, name='panel-teachpage'),
    path('student/',views.student, name='panel-studentpage'),
    path('StdReg/',views.StdReg, name='panel-StdRegpage'),
    path('admReg/',views.admReg, name='panel-admRegpage'),
    path('tchReg/',views.tchReg, name='panel-tchRegpage'),
    path('clsReg/',views.clsReg, name='panel-clsRegpage'),
    path('subReg/',views.subReg, name='panel-subRegpage'),
    path('std_all',views.all_student,name='panel-allstd'),
    path('adm_all',views.all_admin,name='panel-alladm'),
    path('tch_all',views.all_teachers,name='panel-alltch'),
    path('cls_all',views.all_class,name='panel-allcls'),
    path('sub_all',views.all_subject,name='panel-allsub'),
    path('std_up',views.std_update,name='panel-stdup'),
    path('session/',views.sessionReg, name='panel-session'),
    path('logout/',views.Logout_view, name='panel-logout')
]