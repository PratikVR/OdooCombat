from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Employee_db(models.Model):
    username = models.CharField(primary_key = True, max_length = 50)
    firstname = models.CharField(max_length = 100)
    emp_dept = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 256)
    password = models.CharField(max_length = 100)


class HR_db(models.Model):
    username = models.CharField(primary_key = True, max_length = 50)
    firstname = models.CharField(max_length = 100)
    HR_dept = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 256)
    password = models.CharField(max_length = 100)


class Administrator_db(models.Model):
    username = models.CharField(primary_key = True, max_length = 50)
    firstname = models.CharField(max_length = 100)
    Admin_dept = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 256)
    password = models.CharField(max_length = 100)


class grievance_db(models.Model):
    G_id = models.AutoField(primary_key = True, max_length = 15)
    user_id = models.CharField(max_length = 50)
    G_title = models.CharField(max_length = 100)
    G_desc = models.TextField()
    user_dept = models.CharField(max_length = 100)
    severity = models.IntegerField()
    files = models.FileField(upload_to = "G_media/", default=None)
    register_time = models.TimeField(auto_now_add = True)
    event_date = models.TimeField()
    completion_time = models.TimeField(auto_now_add = True)
    statue = models.CharField(max_length = 50)


def set_password(raw_password):
    return make_password(raw_password)