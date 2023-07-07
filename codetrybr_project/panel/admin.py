from django.contrib import admin
from .models import Admin,Student,Teacher,Subject,SubjectScore,StdClass,Session

admin.site.register(Admin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(StdClass)
admin.site.register(SubjectScore)
admin.site.register(Session)


# Register your models here.
