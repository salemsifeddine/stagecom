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
from django.views.generic.edit import FormMixin
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
import  time
from datetime import date
from .search import *
# from django.http import HttpResponse
# Create your views here.

def  home(request):
    context={"title":"Home"}
    return render(request, "pages/home.html",context)

def register(request):
    logged=False
    
    if request.method != "POST":
        form=RegisterForm()
    else:
        form=RegisterForm(data=request.POST)

        if form.is_valid():
            
           
    
            usernamereg=form.cleaned_data.get("username")
            emailreg=form.cleaned_data.get("email")
            passwordreg=form.cleaned_data.get("password1")
            typeuser=request.POST.getlist('typeuser')[0]
            

            form.save()
            new_user = authenticate(username=usernamereg,password=passwordreg)
            if new_user is not None:
                auth_login(request,new_user)
                logged=True
               
            if logged:
                if typeuser == "Company":
                    comp, created = Company.objects.get_or_create(company=new_user, description="")
                    print("company created succesfully")
                    return redirect('companyinfos')
                elif typeuser == "Student":
                    stu, created = Student.objects.get_or_create(student=new_user)
                    print("Student created succesfully")  
                    return redirect('home')     


                
            
            
            



    context={"title":"Register","courses":Courses.objects.all(),"form":form}
    return render(request, "pages/register.html",context)

def companyinfos(request):


    return render(request,"pages/companyinfos.html",{})

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
    company=False
    student=False
    
    try:
        Company.objects.get(company=request.user)
        company = True

        
    except:
        student =True
    if request.method != "POST":
            form =InternshipForm()
            
    else:
        form=InternshipForm(request.POST, request.FILES)
        if form.is_valid():
            title= form.cleaned_data.get('title')
            level=form.cleaned_data.get('level')
            location=form.cleaned_data.get('location')
            tags=form.cleaned_data.get('tags')
            datefield=form.cleaned_data.get('datefield')
            imageFile=form.cleaned_data.get('imageFile')
            requirements=form.cleaned_data.get('requirements')
            description=form.cleaned_data.get('description')

            datagiven=Internships(title=title,level=level,company=request.user,location=location,date=datefield,
                tags=tags,image=imageFile,requirements=requirements,description=description)
            datagiven.save()

            return redirect("home")
            
    context={"title":"Courses","courses":Courses.objects.all(),"company":company,"student":student}
    return render(request, "pages/courses.html",context)

def internships(request):
    company=False
    student=False
    
    try:
        Company.objects.get(company=request.user)
        company = True

        
    except:
        student =True

    
    internships=Internships.objects.all()
    savedInternships=[]
    saveArray=[]
    arrayinternships=[]
    for  intnum,intship in enumerate(internships):
        
        
          
        if WishInternship.objects.filter(user=request.user,internship=intship):
            myobject= {"saved":"exist","intship":intship}
        else:
            myobject= {"saved":False,"intship":intship}

        print(myobject)
        if intship.date < date.today():
            isclosedintsh = intship.is_closed = True
            
        else:
            arrayinternships.append(myobject)
            

    if request.method != "POST":
            form =InternshipForm()
            
    else:
        form=InternshipForm(request.POST, request.FILES)
        if form.is_valid():
            title= form.cleaned_data.get('title')
            level=form.cleaned_data.get('level')
            location=form.cleaned_data.get('location')
            tags=form.cleaned_data.get('tags')
            datefield=form.cleaned_data.get('datefield')
            imageFile=form.cleaned_data.get('imageFile')
            requirements=form.cleaned_data.get('requirements')
            description=form.cleaned_data.get('description')

            datagiven=Internships(title=title,level=level,company=request.user,location=location,date=datefield,
                tags=tags,image=imageFile,requirements=requirements,description=description)
            datagiven.save()

            return redirect("home")

    
    
    

    context={"title":"Internships" ,"internships":arrayinternships, "wishInternships":savedInternships,
    "company":company,"student":student}

    try:
        context["form"]=form
    except :
        print("there is no form")
    return render(request, "pages/internships.html",context)

# class InternshipDet(generic.DetailView):
    
    
#     def get_context_data(self,**kwargs):
#         internships=Internships.objects.all()
#         try:
#             savedInternships= WishInternship.objects.filter(user=self.request.user)
#             arrayinternships=[]
#             dataInternship = super().get_context_data(**kwargs)
#             internship = super().get_context_data(**kwargs)
            
#             dataInternship["internshipSaved"]= WishInternship.objects.all().filter(internship=self.object.pk)
#             # total["products"]=internships.objects.all()
            
#             for  intnum,intship in enumerate(internships):
            
#                 try:
#                     str(intship) == str(savedInternships[intnum])
#                     flagSavedInternship = "exist"
                    
#                 except:
#                     flagSavedInternship = False
                

#                 dataInternship["saved"]= flagSavedInternship

#                 if self.request.user.is_authenticated:
#                     dataInternship["username"]= self.request.user.username
#                     dataInternship["email"] = self.request.user.email
#         except:
#             print("user unauth")

       
#         if self.request.method != "POST":
#             form=applicantInternship()
#             dataInternship["form"]=form
#         else:
#             form=applicantInternship(data=self.request.POST)
#             dataInternship["form"]=form
#             if form.is_valid():
                
#                 formcommited= form.save(commit=False)
#                 formcommited.internship = Internships.objects.all().filter(internship=self.object.pk)
#                 formcommited.user = self.request.user

#                 formcommited.save()
#                 return redirect('home')
#         # if self.request.user.is_authenticated:
#         return dataInternship

# @method_decorator(csrf_exempt, name='dispatch')
class InternshipDet(FormMixin,generic.DetailView):
    model=Internships
    form_class=ApplicantInternship
    template_name="pages/internshipDet.html"
    success_url = '/'
  

    def get_context_data(self,**kwargs):
        internships=Internships.objects.all()
        internship = super().get_context_data(**kwargs)
        dataInternship = super().get_context_data(**kwargs)
        dataInternship["object"]=Internships.objects.get(id=self.object.pk)

        
        if self.request.user.is_authenticated:
            savedInternships= WishInternship.objects.filter(user=self.request.user)
            arrayinternships=[]
            
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

                
                dataInternship["username"]= self.request.user.username
                dataInternship["email"] = self.request.user.email
        else:
            print("user unauth")

        return dataInternship

    def post(self, request, *args, **kwargs):
 
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            # form.internship = Internships.objects.get(id=self.object.pk)
            print("form valid")
            return self.form_valid(form)
        else:
            print("form invalid")
            return self.form_invalid(form)
   

    def form_valid(self, form):
       
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        circulumvitae = form.cleaned_data["circulumvitae"]
        motivationLetter = form.cleaned_data["motivationLetter"]
        print(username,email,circulumvitae,motivationLetter)
        try:
            applicant, created= InternshipsApplicant.objects.get_or_create(username=username, email=email,
            internship=Internships.objects.get(id=self.object.pk),user=self.request.user,
            circulumvitae=circulumvitae,motivationLetter=motivationLetter)
        except:
            applicant, created= InternshipsApplicant.objects.get_or_create(username=username, email=email,
            internship=Internships.objects.get(id=self.object.pk),user=None,
            circulumvitae=circulumvitae,motivationLetter=motivationLetter)

        
        
        # dateadded=datetime.datetime.today()
        # edition=Internships.objects.get(title=self.object.title).edition
        
            
        return super(InternshipDet, self).form_valid(form)   


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


@csrf_exempt
def ajaxrequest(request):
   
    major=request.GET.get("major")
    place=request.GET.get("place")
    tag=request.GET.get("tag")

    data={}
    if request.is_ajax():
        print(getprodFiltered(major,place,tag,request))
            
        
        
        data=getprodFiltered(major,place,tag,request)
        
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)