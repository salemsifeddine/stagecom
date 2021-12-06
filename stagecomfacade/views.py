from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.db.models import Count
from django.contrib.auth.models import auth
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
from .forms import *
# from django.http import HttpResponse
# Create your views here.

def  home(request):
    context={"title":"Home"}
    return render(request, "pages/home.html",context)

def register(request):
    
    if request.method != "POST":
        form=RegisterForm()
    else:
        form=RegisterForm(data=request.POST)

        if form.is_valid():
            
           
    
            usernamereg=form.cleaned_data.get("username")
            emailreg=form.cleaned_data.get("email")
            passwordreg=form.cleaned_data.get("password1")

            form.save()
            new_user = authenticate(username=usernamereg,password=passwordreg)
            if new_user is not None:

                auth_login(request,new_user)
            
            
            return redirect('home')



    context={"title":"Register","courses":Course.objects.all(),"form":form}
    return render(request, "pages/register.html",context)



def login(request):
   
    if request.method != 'POST':
        form=LoginForm()

    else:
        form=LoginForm(data=request.POST)
       
        if form.is_valid():
            user = authenticate(
                    username=form.cleaned_data.get("username"),
                    password=form.cleaned_data.get("password"),
                )
            if user is not None:
                auth_login(request, user)
                return redirect("home")

    context={"title":"Login","form":form}
    return render(request, "pages/login.html",context)

def logout(response):
    auth.logout(response)
    return redirect("home")

def courses(request):

    context={"title":"Courses","courses":Course.objects.all()}
    return render(request, "pages/courses.html",context)

def internships(request):

    context={"title":"Internships" }
    return render(request, "pages/internships.html",context)

def internshipDet(request):

    context={"title":"Internship" }
    return render(request, "pages/internshipDet.html",context)