from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.db.models import Count
# from django.http import HttpResponse
# Create your views here.

def  home(request):
    return render(request, "pages/home.html",{})

def register(request):

    context={"courses":Course.objects.all()}
    return render(request, "pages/register.html",context)

def login(request):
    context={}
    return render(request, "pages/login.html",context)

def courses(request):

    context={"courses":Course.objects.all()}
    return render(request, "pages/courses.html",context)

def mobile(request):

    context={ }
    return render(request, "pages/mobile.html",context)