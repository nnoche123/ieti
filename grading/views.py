from users.forms import UserRegisterForm
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from users.models import *
from .models import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required



@login_required(login_url='loginPage')
def dashboard(request):
    student = Student.objects.get(name=name)
    student.subject.all()
    return render(request, 'grading/dashboard.html', {'student':student})

@login_required(login_url='loginPage')
def StudentGrades(request):
    Student.subject
    Teacher.subject
    return render(request, 'grading/Student.html', {'subject':subject})


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = UserRegisterForm(request.POST)

        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for: ' + user)

                return redirect('loginPage')

        
        return render(request, 'grading/register.html', {'form': form} )

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')

            else:
                    messages.info(request, 'Your Username or Password is incorrect.')
                    
        context = {}
        return render(request, 'grading/login.html', context)




def logoutUser(request):
    logout(request)
    return redirect('loginPage')

