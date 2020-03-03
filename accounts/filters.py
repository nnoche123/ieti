import django_filters
from django_filters import DateFilter, CharFilter

from .models import *
# from django.contrib.postgres.fields import ImageField


class OrderFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	# end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	# note = CharFilter(field_name='note', lookup_expr='icontains')
	name = CharFilter(field_name='name', lookup_expr='icontains')


	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['profile_pic', 'user']
		# exclude = ['profile_pic']
		# filter_overrides = {
        #      models.CharField: {
        #          'filter_class': django_filters.ImageField,
        #          'extra': lambda f: {
        #              'lookup_expr': 'icontains',
        #          },
        #      },
		# }