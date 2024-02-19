from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    
    def __str__(self) -> str:
        return self.user.username


class Teacher(models.Model):
    
    CHOOISE_CLASS = (
        ("CS", "CS"),
        ("ZBC", "ZBC"),
        ("XYZ", "XYZ")
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    classes = models.CharField(max_length=100, choices=CHOOISE_CLASS)
    students = models.ManyToManyField(Student, related_name='teachers', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.user.username

class Post(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.title

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student.user.username