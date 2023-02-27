from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)