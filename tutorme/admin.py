from django.contrib import admin
from .models import AppUser, StudentProfile, TutorProfile, Course

admin.site.register(AppUser)
admin.site.register(StudentProfile)
admin.site.register(TutorProfile)
admin.site.register(Course)