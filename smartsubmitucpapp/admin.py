from django.contrib import admin
from .models import UserProfile, Post, Assignment, AssignmentSubmission
# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)