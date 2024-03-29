from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Assignment,Student,Submission,Post
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
import os

def login_view(request):
    if request.method == "GET":
        username = request.GET.get('username')
        password = request.GET.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                if hasattr(request.user, 'student_profile'):
                    return redirect('feed')  # Redirect students to feed
                else:
                    messages.error(request, 'You are not authorized to access this page.')
                    return render(request, 'login.html')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Username or password missing.')
            return render(request, 'login.html')
    return render(request, 'login.html')

def home(request):
    return render(request, "home.html", {})  
def testing(request):
    student = get_object_or_404(Student, user=request.user)
    assignments = Assignment.objects.filter(teacher__students=student)

    submissions = Submission.objects.filter(student=student)

    
    if request.method == 'POST':
        
        assignment_picture = request.FILES['file']

        print(assignment_picture)

        if assignment_picture:
        
            assignment_id = request.POST.get('assignment_id')

            print(assignment_id)

            assignment = get_object_or_404(Assignment, id=assignment_id)
            student_ = get_object_or_404(Student, user=request.user)

            already_submitted = Submission.objects.filter(
                assignment=assignment,
                student=student
            ).exists()

            if already_submitted:
                return redirect('/assignment')

            submission = Submission.objects.create(
                file=assignment_picture,
                assignment=assignment,
                student=student_
            )

            return redirect('/assignment')
        else:
            messages.error(request, 'No files uploaded.')

    return render(request, 'example.html', {'assignments': assignments, "user": request.user, "submissions": submissions})
  
@login_required
def feed(request):
    
    student = request.user.student_profile
    
    
    teacher = student.teachers.first()  
    
    teacher_posts = Post.objects.filter(teacher=teacher)
    
    return render(request, "feed.html", {'teacher_posts': teacher_posts})

from django.shortcuts import get_object_or_404

@login_required
def assignment(request):
    student = get_object_or_404(Student, user=request.user)
    assignments = Assignment.objects.filter(teacher__students=student)

    submissions = Submission.objects.filter(student=student)

    
    if request.method == 'POST':
        
        assignment_picture = request.FILES['file']

        print(assignment_picture)

        if assignment_picture:
        
            assignment_id = request.POST.get('assignment_id')

            print(assignment_id)

            assignment = get_object_or_404(Assignment, id=assignment_id)
            student_ = get_object_or_404(Student, user=request.user)

            already_submitted = Submission.objects.filter(
                assignment=assignment,
                student=student
            ).exists()

            if already_submitted:
                return redirect('/assignment')

            submission = Submission.objects.create(
                file=assignment_picture,
                assignment=assignment,
                student=student_
            )

            return redirect('/assignment')
        else:
            messages.error(request, 'No files uploaded.')

    return render(request, 'assignment.html', {'assignments': assignments, "user": request.user, "submissions": submissions})

@login_required
def profile(request):
    user = request.user  
    
    return render(request, 'profile.html', {'user': user})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Submission

def upload_assignment(request):
    
     return render(request, 'assignment.html')  

def show_logged_out(request):
    return render(request, 'logged_out.html')

def delete_session(request):
    if request.user.is_authenticated:
        logout(request)  # Log out the user
    return render(request, 'logged_out.html')  