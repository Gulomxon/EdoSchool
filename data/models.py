from django.db import models

from EdoSchool.account.models import Teacher

class Subject(models.Model):
    title = models.CharField(max_length=100)
    

class Test(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subjrct = models.ForeignKey(Subject, on_delete=models.CASCADE)
    time = models.CharField(max_length=250)
    