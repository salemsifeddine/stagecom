from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models.fields import CharField
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
    date=models.DateTimeField(blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    tags=models.CharField(max_length=255)
    requirements=models.TextField(max_length=255,blank=True)
    description=models.TextField(blank=True)



























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