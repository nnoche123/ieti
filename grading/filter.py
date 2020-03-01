import django_filters

from users.models import *

class StudentFilter(django_filters.FilterSet):
        class Meta:
            model = Student
            fields = '__all__'
            exclude = ['name', 'grades','teacher','subject']