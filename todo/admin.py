from django.contrib import admin
from .models import R_Task
# Register your models here.
class Taskadmin(admin.ModelAdmin):
    list_display=('task','is_completed','created_at','updated_at')
admin.site.register(R_Task,Taskadmin)