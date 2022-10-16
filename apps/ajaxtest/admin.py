from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display=['title','caption','is_active']
    

@admin.register(Like)
class likeAdmin(admin.ModelAdmin):
    list_display=['post']
    
@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display=['name','email','message']