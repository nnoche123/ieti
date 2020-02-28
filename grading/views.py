from users.forms import UserRegisterForm
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from users.models import *
from .models import *
from django.contrib import messages

from.decorators import unauthenticated_user ,allowed_users

from django.contrib.auth.decorators import login_required

from .forms import Update


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def Teacher(request):
    student = Student.objects.all()
    return render(request, 'grading/Teacher.html', {'student':student})

@login_required(login_url='loginPage')
def StudentGrades(request):
    student = Student.objects.all()

    return render(request, 'grading/Student.html', {'student':student})


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
@unauthenticated_user
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
                return redirect('teacher')

            else:
                    messages.info(request, 'Your Username or Password is incorrect.')
                    
        context = {}
        return render(request, 'grading/login.html', context)




def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def UpdateForms(request, pk):
    
    student = Student.objects.get(id=pk)
    form = Update(instance=student)

    if request.method == 'POST':
	    form = Update(request.POST, instance=student)
	    if form.is_valid():
		    form.save()
		    return redirect('teacher')

    context = {'form':form}
    return render(request, 'grading/update_form.html', context)

