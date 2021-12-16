from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.db.models.base import Model
from django.forms import ModelForm, fields, widgets
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *
username_validator = UnicodeUsernameValidator()





class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'placeholder': 'username',"name":"username"}))
    password = forms.CharField(max_length=63,  widget=forms.PasswordInput(attrs={'placeholder': 'Password',"name":"password"}))
    
    class Meta:
        model=User
        fields = ["username","password"]


class RegisterForm(UserCreationForm):

   username = forms.CharField(
       widget=forms.TextInput(attrs={'placeholder': ' ',"name":"username"})
   )
   email = forms.CharField(
       widget=forms.EmailInput(attrs={'placeholder': ' ',"name":"email"})
   )
   password1 = forms.CharField(
       widget=forms.PasswordInput(attrs={'placeholder': ' ',"name":"password1"})
   )
   password2 = forms.CharField(
       widget=forms.PasswordInput(attrs={'placeholder': ' ',"name":"password2"})
   )

   class Meta:
        model=User
        fields=["username","email","password1","password2"]
   # def __init__(self, *args, **kwargs):
   #      super(RegisterForm, self).__init__(*args, **kwargs)
   #      self.fields['studentCheck'].required = False
   #      self.fields['companyCheck'].required = False

class Newsletter(forms.Form):

   emailnewsletter= forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Type your email for updates',"name":"newsletter"}))
   
   class Meta:
      model=User
      fields=["emailnewsletter"]


class ApplicantInternship(forms.ModelForm):
      username = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'id': 'usernameUser','placeholder': ' ',"name":"username"}))
      email = forms.CharField(
       widget=forms.EmailInput(attrs={'placeholder': ' ',"name":"email","id":"EmailUser"})
      )
      circulumvitae = forms.FileField( widget=forms.FileInput(attrs={"class":"inputfile","style":"font-size: 14px;padding-top:5px"}))
      motivationLetter =forms.CharField(widget=forms.Textarea(attrs={"cols":"0","rows":"0","style":"padding: 5px; max-width:521px;max-height: 70px","name":"email","id":"textareainput"}))
      class Meta:
         model=InternshipsApplicant
         fields = ["username", "email","circulumvitae","motivationLetter"]
      



class ContactUsForm(forms.ModelForm):
      first_name = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'id': 'usernameUser','placeholder': ' ',"name":"username"}))
      last_name = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'id': 'usernameUser','placeholder': ' ',"name":"username"}))
      email = forms.CharField(
       widget=forms.EmailInput(attrs={'placeholder': ' ',"name":"email","id":"EmailUser"})
      )
      subject =forms.CharField(widget=forms.Textarea(attrs={"cols":"0","rows":"0","style":"padding: 5px; max-width:521px;max-height: 70px","name":"email","id":"textareainput"}))
      class Meta:
         model=ContactUs
         fields = ["first_name","last_name","email","subject"]


class InternshipForm(forms.Form):
    title = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    level = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'placeholder': 'Level'}))
    location = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    tags = forms.CharField(max_length=63,widget=forms.TextInput(attrs={"placeholder": 'Tags: tag1,tag2..'}))
    datefield=forms.DateField(widget=forms.DateInput(attrs={"placeholder": 'date',"type":"date"}))
    imageFile = forms.FileField( widget=forms.FileInput(attrs={"style":"font-size: 14px;padding-top:5px"}))
    requirements =forms.CharField(widget=forms.Textarea(attrs={"cols":"0","rows":"0","style":"padding: 5px;min-height:59.9px; max-height: 60px;min-width:449.9px;max-width:450px"}))
    description =forms.CharField(widget=forms.Textarea(attrs={"cols":"0","rows":"0","style":"padding: 5px;min-height:59.9px; max-height: 60px;min-width:449.9px;max-width:450px"}))
    class Meta:
        model=Internships
        fields="__all__"
