from django.forms import ModelForm
from .models import *
from users.models import *

class Update(ModelForm):
    class Meta:
        model = Student
        fields = ['grades']
