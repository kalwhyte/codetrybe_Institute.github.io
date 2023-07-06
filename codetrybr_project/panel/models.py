"""
modules containing the database structure of the codetrybe webapp
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,default="0802")
    address = models.CharField(max_length=50,default="Default address")

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    """
    a model for Teachers table
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,default="+234-")
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50,default="Default address")

    def __str__(self):
        return self.user.username


class Subject(models.Model):
    """
    subjects offered by students
    """
    name = models.CharField(max_length=30)
    Teacher = models.ManyToManyField(Teacher,related_name="subject_taught")
    score = models.IntegerField(null=True, blank=True)
    # class_offering =models.ForeignKey()
    def __str__(self):
        return self.name

# need to thing 

class StdClass(models.Model):
    """
    all classes in the school
    """
    CLASS_CHOICES = [
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SSS1', 'SSS1'),
        ('SSS2', 'SSS2'),
        ('SSS3', 'SSS3'),
    ]

    name = models.CharField(max_length=40)
    subject = models.ManyToManyField(Subject,related_name="classes")
    class_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=20, default="0802")
#     address = models.CharField(max_length=50, default="Default address")
#     subjects = models.ManyToManyField(Subject, related_name="students", blank=True, limit_choices_to={'name__lte': 8})
#     dob = models.DateField()
#     std_class = models.ForeignKey(StdClass, on_delete=models.CASCADE, default=None)
#     email = models.EmailField(max_length=50, default="codetrybe@codetrybe.com")
#     gender = models.CharField(max_length=10, default='NULL')
#     # USERNAME_FIELD = 'user'

#     def __str__(self):
#         return self.user.username



class Student(models.Model):
    """
    a model for Teachers table
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,default="+234-")
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50,default="Default address")
    subjects = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True)
    dob = models.DateField()
    std_class = models.ForeignKey(StdClass, on_delete=models.CASCADE, default=None)
    gender = models.CharField(max_length=10, default='NULL')

    def __str__(self):
        return self.user.username

class SubjectScore(models.Model):
    """
    a model for Subject Score
    """
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student.user.username} {self.subject.name}"
    
