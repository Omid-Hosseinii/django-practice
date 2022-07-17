from django.urls import path
import apps.main.views as views

urlpatterns=[
    
    path('',views.index,name='mainpage'),
    path('ifcondition/',views.if_condition,name='if'),
    path('forcondition/',views.for_condition,name='for'),
    path('autoescape/',views.autoescape,name='autoescape'),
    path('datetime/',views.date_time,name='date'),
    path('tag/',views.tag_Filters,name='tagfilters'),
    path('photoes/',views.media_images,name='photo')

]