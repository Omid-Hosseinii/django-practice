from django.urls import path
from apps.ajaxtest.views import *  


urlpatterns = [
    path('',index,name='indexajax'),
    path('post',post,name='postajax'),
    path('like',like,name='postlikeajax'),
    path('contact',contact,name='contactajax'),
]