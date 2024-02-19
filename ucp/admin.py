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
    list_display = ['content', 'created_at']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(teacher__user=request.user)
        return qs
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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            # Limit the choices for the teacher field to the current user's teacher profile
            kwargs["queryset"] = Teacher.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'submitted_at']


