from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Assignment,Student,Submission
from django.shortcuts import get_object_or_404
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
                return redirect('feed')  
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
    return render(request, "feed.html", {})  

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
    user = request.user  # Get the current logged-in user
    # Pass the user object to the template
    return render(request, 'profile.html', {'user': user})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Submission

def upload_assignment(request):
    
    return render(request, 'assignment.html')  # Render the assignment upload page template

def delete_session(request):
    if request.user.is_authenticated:
        request.session.flush()
        return redirect('login_user')  
    else:
        return redirect('login_user') 

