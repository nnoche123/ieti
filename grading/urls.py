from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('student/', views.StudentGrades, name='StudentGrades')
]