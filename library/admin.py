 

# Register your models here.
from django.contrib import admin
from .models import Contact, Student,Seat

admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Seat)
