from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Employee_db(AbstractBaseUser):
    username = models.CharField(primary_key = True, max_length = 50)
    firstname = models.CharField(max_length = 100)
    emp_dept = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 256)
    password = models.CharField(max_length = 100)


class HR_db(AbstractBaseUser):
    username = models.CharField(primary_key = True, max_length = 50)
    firstname = models.CharField(max_length = 100)
    HR_dept = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 256)
    password = models.CharField(max_length = 100)


class Administrator_db(AbstractBaseUser):
    username = models.CharField(primary_key = True, max_length = 50)
    firstname = models.CharField(max_length = 100)
    Admin_dept = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 256)
    password = models.CharField(max_length = 100)


class grievance_db(models.Model):
    G_id = models.CharField(primary_key = True, max_length = 50)
    user_id = models.CharField(max_length = 50)
    G_title = models.CharField(max_length = 100)
    G_desc = models.TextField()
    user_dept = models.CharField(max_length = 100)
    severity = models.IntegerField(max_length = 3)
    files = models.FileField(upload_to = "G_media/")
    register_time = models.TimeField(auto_now_add = True)
    completion_time = models.TimeField(auto_now_add = True)
    statue = models.CharField(max_length = 50)
