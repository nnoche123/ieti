from django.contrib import admin

# Register your models here.

from .models import *



class SubjecttInLine(admin.TabularInline):
    model = Subject

class StudentAdmin(admin.ModelAdmin):
    # inlines = [
    #     SubjectInLine,
    # ]
    pass

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentSubject)

