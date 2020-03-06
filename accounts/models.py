from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Teacher')
    name = models.CharField(max_length=200, null=True)
    subject = models.ManyToManyField(Subject)
 
    def __str__(self):
        return self.name
    

class Student(models.Model):
    STRAND = [('STEM', 'STEM'), ('HUMMS', 'HUMMS'), ('GAS', 'GAS')]
    YEAR_LEVEL = [('GR11','Grade 11'), ('G12','Grade 12')]
    SECTION = [('A', 'A'), ('B', 'B'), ('C', 'C')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    name = models.CharField(max_length=200, null=True)
    strand = models.CharField(max_length=10, choices=STRAND)
    year_level = models.CharField(max_length=10, choices=YEAR_LEVEL)
    section = models.CharField(max_length=1, choices=SECTION)
    subject = models.ManyToManyField(Subject, through='StudentSubject',
											  through_fields=('student', 'subject'))
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    def __str__(self):
        return self.name

    
class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grades = models.PositiveSmallIntegerField(blank=True, null=True)  
    FSMTgrades = models.PositiveSmallIntegerField(blank=True, null=True)
    FSFgrades = models.PositiveSmallIntegerField(blank=True, null=True)
    FSgrades = models.PositiveSmallIntegerField(blank=True, null=True)
    SSMTgrades = models.PositiveSmallIntegerField(blank=True, null=True)
    SSFgrades = models.PositiveSmallIntegerField(blank=True, null=True)
    SFgrades = models.PositiveSmallIntegerField(blank=True, null=True)
 

    def __str__(self):
        return self.subject.name