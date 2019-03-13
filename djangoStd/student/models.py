from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Major(models.Model):
    major_id = models.IntegerField(primary_key=True, verbose_name='전공ID')
    major_title = models.CharField(max_length=100, verbose_name='전공명')

    def __str__(self):
        return self.major_title

    def get_absolute_url(self):
        return reverse('student:All_list')
    
class Student(models.Model):
    studentID = models.IntegerField(primary_key=True,verbose_name='학생ID')
    name = models.CharField(max_length=20, verbose_name='이름')
    major = models.ForeignKey(Major, verbose_name='전공ID', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='전화번호', blank=True,null=True)
    address = models.CharField(max_length=100, verbose_name='주소', blank=True,null=True)
    hobby = models.CharField(max_length=50, verbose_name='취미', blank=True,null=True)
    skill = models.CharField(max_length=50, verbose_name='기술', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student:student_list')
    