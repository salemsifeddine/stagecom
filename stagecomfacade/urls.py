from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('login/',views.login, name="login"),
    path("logout/", views.logout,name="logout"),
    path('courses/',views.courses, name="courses"),
    path('internships/',views.internships, name="internships"),
    path('internshipDet/<int:pk>',views.InternshipDet.as_view(), name="internshipDet"),
    path('internshipApi/',views.saveInternship, name="internshipApi"),
    path('blog/',views.blog, name="blog"),
    path('blogDet/<int:pk>',views.BlogDet.as_view(), name="blogDet"),
    path('contact',views.contact, name="contact")
]