from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Internships)
admin.site.register(WishInternship)
admin.site.register(InternshipsApplicant)
admin.site.register(Blog)
admin.site.register(ContactUs)
admin.site.register(applicationsInt)

####################################

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Content)
admin.site.register(Text)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Video)

admin.site.register(Newsletter)