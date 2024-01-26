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
            return render(request, 'index.html') 
    return render(request, 'index.html')

def home(request):
    return render(request, "home.html", {})  

@login_required
def feed(request):
    return render(request, "feed.html", {})  

@login_required
def assignment(request):
    student = Student.objects.get(user=request.user)
    assignments = Assignment.objects.filter(teacher__students=student)
    print(request.method)
    if request.method == 'POST':
        print("Hello1")
        print(request.FILES)  # Print out files in the request
        assignment_pictures = request.FILES.getlist('file')
        print("Hello2")
        print(request.POST)   # Print out POST data
        if assignment_pictures:
            print("Hello3")
            for assignment_picture in assignment_pictures:
                assignment_id = request.POST.get('assignment_id')
                student_id = request.POST.get('student_id')
                # Save the submission record in the database
                print("Hello4")
                print("Hello5")
                submission = Submission.objects.create(
                    file=assignment_picture,
                    assignment_id=assignment_id,
                    student_id=student_id
                )
                print("Hello5")
                submission.save()
            
            messages.success(request, 'Assignment pictures uploaded successfully.')
            return redirect('feed')  # Redirect to the assignment upload page or any other page
        else:
            messages.error(request, 'No files uploaded.')
    
    return render(request, 'assignment.html', {'assignments': assignments, 'user': request.user})
@login_required
def profile(request):
    return render(request, "profile.html", {})  

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Submission

def upload_assignment(request):
    print("JEhlleo")
    
    return render(request, 'assignment.html')  # Render the assignment upload page template

def delete_session(request):
    if request.user.is_authenticated:
        request.session.flush()
        return redirect('login_user')  
    else:
        return redirect('login_user') 

