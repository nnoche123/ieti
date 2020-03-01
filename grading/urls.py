from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('teacher/', views.Teacher, name='teacher'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('student/', views.StudentGrades, name='StudentGrades'),
    path('UpdateForms/<str:pk>', views.UpdateForms, name='UpdateForms'),

]