from django.urls import path
import apps.main.views as views

urlpatterns=[
    
    path('',views.index),
    path('ifcondition/',views.if_condition),
    path('forcondition/',views.for_condition),
    path('autoescape/',views.autoescape),
    path('datetime/',views.date_time,name='date'),
    path('tag/',views.tag_Filters,name='tagfilters'),
    path('photoes/',views.media_images,name='photo')

]