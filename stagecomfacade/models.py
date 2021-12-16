
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models.fields import CharField
from django.http import request
from .fields import OrderField

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
# Create your models here.


class Internships(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(blank=False, upload_to="Internships_images")
    level=models.CharField(max_length=100)
    company=models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    location=models.CharField(max_length=255)
    date=models.DateField()
    date_added=models.DateTimeField(auto_now_add=True)
    tags=models.CharField(max_length=255)
    requirements=models.TextField(max_length=255,blank=True)
    description=models.TextField(blank=True)
    is_closed=models.BooleanField(default=False)

    def __str__(self):
        return self.title


class WishInternship(models.Model):
    internship = models.ForeignKey(Internships, blank=False, on_delete=models.CASCADE)
    user= models.ForeignKey(User,blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.internship.title

class InternshipsApplicant(models.Model):
    username=models.CharField(max_length=255)
    email= models.EmailField(max_length=254)
    internship = models.ForeignKey(Internships, blank=False, on_delete=models.CASCADE)
    user= models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    circulumvitae = models.FileField()
    motivationLetter = models.TextField(blank=False)

    def __str__(str):
        return f"internship Applicant"


class Blog(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to="blog_images",blank=True)
    category=models.CharField(max_length=60)
    date_added=models.DateTimeField(auto_now_add=True, blank=True)
    description1=models.TextField()
    description2=models.TextField()
    description3=models.TextField()
    description4=models.TextField()
    description5=models.TextField()
    description6=models.TextField()
    quote=models.TextField()
    authorQuote=models.CharField(max_length=60)

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    email=models.EmailField(max_length=255)
    subject=models.TextField()

    def __str__(self):
        return f"{self.first_name} contact"

    
class Company(models.Model):
    company=models.ForeignKey(User,blank=False,on_delete=models.CASCADE)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to="company_image",blank=True)
    
    def __str__(self):
        return f"{self.company}"

class Student(models.Model):
    student=models.ForeignKey(User,blank=False,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="student_image",blank=True,null=True)

    def __str__(self):
        return f"{self.student}"

















# information about the subject
class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
# ordering course title
    class Meta:
        ordering = ['title']
# to show the title
    def __str__(self):
        return self.title
# information about the course
class Course(models.Model):
    # Owner -> instructor / creator of the course
    owner = models.ForeignKey(User,
                    related_name='courses_created',
                    on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses',
                        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User,
                                      related_name='courses_joined',
                                      blank=True)
# ordering courses that are created
    class Meta:
        ordering = ['-created']
# to show the course title
    def __str__(self):
        return self.title
# admin can see the courses and about
class Module(models.Model):
    course = models.ForeignKey(Course,
                        related_name='modules',
                        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order'] #default ordering

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

# content of courses
class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to={'model__in':('text',
                                                                    'video',
                                                                    'image',
                                                                    'file')},
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
            ordering = ['order']
# factory pattern for all modules
class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
         abstract =True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string('courses/content/{}.html'.format(
                            self._meta.model_name), {'item': self})

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()


class Newsletter(models.Model):

    email=models.EmailField(max_length=150)