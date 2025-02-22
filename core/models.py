from django.db import models
from django.conf import settings

# Create your models here.

from django.contrib.auth.models import AbstractUser
from core.manager import UserManager
Usertype =(
    ('student', 'student'),
    ('mentor', 'mentor'),
    
)
class User(AbstractUser):
    # username = None
    username = models.CharField(unique=True, max_length=16)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    usertype = models.CharField(choices= Usertype,default = "student" ,max_length=60)

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ['username']c
    objects = UserManager()


class Attendance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.CharField(max_length=200)
    leave = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.employee} - {self.entry}"
    


class Course(models.Model):
    title = models.CharField(max_length = 200)

    def __str__(self): 
        return self.title

class Mentor(models.Model): 
    user = models.OneToOneField(User,on_delete= models.CASCADE)

    def __str__(self): 
        return self.user.username
    
PACKAGE =(
    ('tranning+internship', 'tranning+internship'),
    ('tranning', 'tranning'),
    

)
Time_slot =(
    ('10:00 a.m', '12:00 p.m'),
    ('1:00 a.m', '3:00 p.m'),
    ('3:00 a.m', '5:00 p.m'),
    
)
class Students(models.Model): 
    name = models.CharField(max_length = 200)
    package = models.CharField(choices = PACKAGE, max_length = 200)
    course = models.ForeignKey(Course,on_delete = models.CASCADE)
    payable_fee = models.CharField(max_length = 200)
    collage = models.CharField(max_length = 200)
    time_slot = models.CharField(choices = Time_slot,max_length = 200)
    assigned_mentor = models.ForeignKey(Mentor,on_delete= models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add = True)
    referred_by = models.CharField(max_length = 200)

    def __str__(self): 
        return f"{self.name}-{self.pk}"






    

    # models.py
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password_changed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
