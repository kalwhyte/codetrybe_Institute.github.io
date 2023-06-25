from django.contrib import admin
from .models import Admin,Student,Teacher,Subject,OptionalSubject,SubjectScore,OptionalSubjectScore,StdClass

admin.site.register(Admin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(OptionalSubject)
admin.site.register(StdClass)
admin.site.register(SubjectScore)
admin.site.register(OptionalSubjectScore)

# Register your models here.
