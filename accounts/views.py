from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm, StudentForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			if request.user.groups.all()[0].name == 'student':
				return redirect('grades')
			else:
				return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['teacher'])
# def home(request):
	# orders = Subject.objects.all()
	# students = Teacher.objects.all()

	# total_students = students.count()

	# total_orders = orders.count()
	# delivered = orders.filter(status='Delivered').count()
	# pending = orders.filter(status='Pending').count()

	# context = {'orders':orders, 'students':students,
	# 'total_orders':total_orders,'delivered':delivered,
	# 'pending':pending }

	# return render(request, 'accounts/dashboard.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def userPage(request):
	return render(request, 'accounts/about.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def accountSettings(request):
	teacher = request.user.teacher
	form = StudentForm(instance=teacher)

	if request.method == 'POST':
		form = StudentForm(request.POST, request.FILES,instance=teacher)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'accounts/account_settings.html', context)






@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def products(request):
	products = request.user.student_set.all()

	return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
def grades(request):
	student = Student.objects.get(name = request.user.username)

	students = Student.objects.get(user= request.user.id)
	
	grades = student.studentsubject_set.all()

	myFilter = OrderFilter(request.GET, queryset=grades)
	grades = myFilter.qs

	context = {'grades':grades, 'myFilter':myFilter, 'students':students, 'student':student }
	print(grades)

	return render(request, 'accounts/student.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def home(request):
	teacher = Teacher.objects.get(name=request.user.username)
	print(teacher)
	subjects = teacher.studentsubject_set.all()
	students = Student.objects.all()

	myFilter = OrderFilter(request.GET, queryset=students)
	students = myFilter.qs 

	context = {'teacher':teacher, 'subjects':subjects, 'students':students,
	'myFilter':myFilter}


	return render(request, 'accounts/teacher.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Teacher, Subjects, fields=('name','strand','year_level'), extra=10)
	teacher = Teacher.objects.get(id=pk)
	formset = OrderFormSet(queryset=Subject.objects.none(),instance=teacher)
	form = OrderForm(initial={'teacher':teacher})
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=teacher)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def updateOrder(request, pk):
	grades = StudentSubject.objects.get(id=pk)
	form = OrderForm(instance=grades)
	print('ORDER:', grades)
	if request.method == 'POST':

		form = OrderForm(request.POST, instance=grades)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def deleteOrder(request, pk):
	subject = Subject.objects.get(id=pk)
	if request.method == "POST":
		subject.delete()
		return redirect('/')

	context = {'item':subject}
	return render(request, 'accounts/delete.html', context)