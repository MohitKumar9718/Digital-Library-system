# Register your models here.
from django.contrib import admin
from .models import Contact, Student,Seat

# library/admin.py


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_no', 'village_name', 'fee', 'fee_status', 'joining_date')
    list_filter = ('fee_status', 'village_name')
    search_fields = ('name', 'mobile_no', 'village_name')

admin.site.register(Contact)
admin.site.register(Seat)
