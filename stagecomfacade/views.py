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
from django.views import generic
import json
from django.http import JsonResponse
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
    
    internships=Internships.objects.all()
    savedInternships= WishInternship.objects.filter(user=request.user)
    saveArray=[]
    arrayinternships=[]
    for  intnum,intship in enumerate(internships):
        
        try:
            str(intship) == str(savedInternships[intnum])
            flagSavedInternship = "exist"
            
        except:
            flagSavedInternship = False
           

        myobject= {"saved":flagSavedInternship,"intship":intship}

        arrayinternships.append(myobject)


    
    

    context={"title":"Internships" ,"internships":arrayinternships, "wishInternships":savedInternships}
    return render(request, "pages/internships.html",context)

class InternshipDet(generic.DetailView):
    
    model=Internships
    template_name="pages/internshipDet.html"
    def get_context_data(self,**kwargs):
        internships=Internships.objects.all()
        try:
            savedInternships= WishInternship.objects.filter(user=self.request.user)
            arrayinternships=[]
            dataInternship = super().get_context_data(**kwargs)
            internship = super().get_context_data(**kwargs)
            
            dataInternship["internshipSaved"]= WishInternship.objects.all().filter(internship=self.object.pk)
            # total["products"]=internships.objects.all()
            
            for  intnum,intship in enumerate(internships):
            
                try:
                    str(intship) == str(savedInternships[intnum])
                    flagSavedInternship = "exist"
                    
                except:
                    flagSavedInternship = False
                

                dataInternship["saved"]= flagSavedInternship

                if self.request.user.is_authenticated:
                    dataInternship["username"]= self.request.user.username
                    dataInternship["email"] = self.request.user.email
        except:
            print("user unauth")

       
        if self.request.method != "POST":
            form=applicantInternship()
            dataInternship["form"]=form
        else:
            form=applicantInternship(data=self.request.POST)
            dataInternship["form"]=form
            if form.is_valid():
                
                formcommited= form.save(commit=False)
                formcommited.internship = Internships.objects.all().filter(internship=self.object.pk)
                formcommited.user = self.request.user

                formcommited.save()
                return redirect('home')
        # if self.request.user.is_authenticated:
        return dataInternship




def saveInternship(request):
    data= json.loads(request.body.decode('utf-8'))
    idproduct= data["internshipId"]
    action= data["action"]

    internship_saved= Internships.objects.all().filter(id=idproduct)
   
        
   
    if action == "addInternship":
        addInternship , created = WishInternship.objects.get_or_create(user=request.user, internship=internship_saved.first())
        addInternship.save()
        action="addInternship"
   
    elif action == "removeInternship":
        removeInternship= WishInternship.objects.get(user=request.user, internship=internship_saved.first()).delete() 
        
        action="removeInternship"
  
    
    data_json={"action":action, "id":internship_saved.first().title}
    return JsonResponse( data_json, safe=False)




def blog(request):
    context={
        "blogs":Blog.objects.all()
    }

    return render(request, "pages/blog.html",context)


class BlogDet(generic.DetailView):
    model=Blog
    template_name="pages/blogDet.html"


def contact(request):


    if request.method != "POST":
        form = ContactUsForm()
    else:
        form= ContactUsForm(data=request.POST)
        if form.is_valid():
     
            form.save()
            return redirect("home")

    context={"form":form}
    return render(request, "pages/contact.html",context)