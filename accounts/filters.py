import django_filters
from django_filters import CharFilter

from .models import *
# from django.contrib.postgres.fields import ImageField


class SubjectFilter(django_filters.FilterSet):
	# student = CharFilter(field_name='student', lookup_expr='icontains')

	class Meta:
		model = StudentSubject
		fields = ['student','subject']
		# exclude = ['grades', 'teacher']