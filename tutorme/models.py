from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)


class Course(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=10)
    catalog_number = models.CharField(max_length=10)
    course_id = models.CharField(max_length=10)
    is_enrolled = models.BooleanField(default=False)
    meeting_days = models.CharField(max_length=10)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)

