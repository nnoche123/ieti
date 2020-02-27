from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

from grading.models import *


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    name = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

class Student(models.Model):
    YEAR_LEVEL = [('GR11','Grade 11'), ('G12','Grade 12')]
    SECTION = [('A', 'A'), ('B', 'B'), ('C', 'C')]
    SEX = [('MALE','MALE'),('FEMALE','FEMALE')]
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Student')
    strand = models.ForeignKey(Strand, on_delete=models.CASCADE, related_name='Strand')
    year = models.CharField(max_length=10, choices=YEAR_LEVEL)
    sex = models.CharField(max_length=10, choices=SEX, default ='al')
    section = models.CharField(max_length=1, choices=SECTION)
    grades = models.IntegerField(range(70, 95))
    teacher = models.ManyToManyField(Teacher)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.SET_NULL)
    

    
    def __str__(self):
        return self.name.username

class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
