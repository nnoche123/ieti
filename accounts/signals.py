from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Teacher

def student_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='student')
		instance.groups.add(group)
		Teacher.objects.create(
			user=instance,
			name=instance.username,
			)
		print('Profile created!')

post_save.connect(student_profile, sender=User)