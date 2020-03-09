from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class StudentForm(ModelForm):
	class Meta:
		model = Teacher
		fields = '__all__'
		exclude = ['user']

class OrderForm(ModelForm):
	class Meta:
		model = StudentSubject
		fields = ['FSMTgrades','FSFgrades','FSgrades',
				'SSMTgrades','SSFgrades','SFgrades']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

