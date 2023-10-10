from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('login-redirect')  
    return render(request, 'landing/landing_UI.html')

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

def login_redirect(request):
    if is_teacher(request.user):
        return redirect('quiz/dashboard')
    elif is_student(request.user):
        return redirect('student/sdashboard')
    else:
        return redirect('')

def about(request):
    return render(request, 'landing/about.html')

