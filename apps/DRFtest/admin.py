from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class productadmin(admin.ModelAdmin):
    list_display=['name','price','register_date','image']