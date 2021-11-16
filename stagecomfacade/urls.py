from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('login/',views.login, name="login"),
    path('courses/',views.courses, name="courses"),
     path('internships/',views.internships, name="internships"),
   
]