from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='panel-home'),
    path('welcome/', views.welcome ,name='panel-welcome'),
    path('login/',views.login, name='panel-loginpage'),
    path('myadmin/',views.admin, name='panel-adminpage'),
    path('myadmin/inbox/',views.admin, name='panel-inboxpage'),
    path('myadmin/gallery/',views.admin, name='panel-gallerypage'),
    path('myadmin/charts/',views.admin, name='panel-chartspage'),
    path('myadmin/tables/',views.admin, name='panel-tablespage'),
    path('myadmin/forms/',views.admin, name='panel-formspage'),
    path('myadmin/maps/',views.admin, name='panel-mapspage'),
    path('myadmin/login/',views.admin, name='panel-loginpage'),
    path('myadmin/buttons/',views.admin, name='panel-buttons'),
    path('myadmin/grids/',views.admin, name='panel-grids'),
    path('myadmin/errorpage/',views.admin, name='panel-errorpage'),
    path('myadmin/icons/',views.admin, name='panel-iconspage'),
    path('myadmin/typography/',views.admin, name='panel-typographypage'),
    path('myadmin/faq/',views.admin, name='panel-faqpage'),
    path('register/',views.register, name='panel-registerpage'),
]
