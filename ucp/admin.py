from django.contrib import admin
from .models import Teacher, Student, Post, Comment, Like, Assignment, Submission

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'classes', 'AssignedStudents']
    
    def AssignedStudents(self, obj):
        return "\n".join([p.user.username for p in obj.students.all()])



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'teachers_']

    def teachers_(self, obj):
        return "\n".join([p.user.username for p in obj.teachers.all()])

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'content', 'created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'content', 'created_at']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'title', 'description']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        return qs.filter(teacher=request.user.teacher_profile)
    
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'submitted_at']

# You can register other models in a similar fashion
