"""
modules containing the database structure of the codetrybe webapp
"""
from django.db import models
from django.contrib.auth.models import User

    
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
    phone_number = models.CharField(max_length=20,default="0802")
    address = models.CharField(max_length=50,default="Default address")

    def __str__(self):
        return self.user.username


class Subject(models.Model):
    """
    subjects offered by students
    """
    name = models.CharField(max_length=30)
    Teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True, blank=True,
                                      related_name="subject_taught")
    # class_offering =models.ForeignKey()
    def __str__(self):
        return self.name
    

class OptionalSubject(models.Model):
    """
    optional subjects offered by student
    """
    name = models.CharField(max_length=30)
    Teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True, blank=True,
                                      related_name="optional_subject_taught")
    def __str__(self):
        return self.name
    
# need to thing 

class StdClass(models.Model):
    """
    all classes in the school
    """
    name = models.CharField(max_length=40)
    subject = models.ManyToManyField(Subject,related_name="subject")
    optional_subject = models.ManyToManyField(OptionalSubject,
                                              related_name="optional_subject", null=True, blank=True,
                                              )
    class_teacher = models.OneToOneField(Teacher,on_delete=models.SET_NULL,
                                          null=True, blank=True)
    def __str__(self):
        return self.name
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,default="0802")
    address = models.CharField(max_length=50,default="Default address")
    std_class = models.ForeignKey(StdClass,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.user.username


class SubjectScore(models.Model):
    """
    a model for Subject Score
    """
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    Score = models.IntegerField()
    def __str__(self):
        return f"{self.student.user.username} {self.subject.name}"
    

class OptionalSubjectScore(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.student.user.username} {self.subject.name}"

# Create your models here.

