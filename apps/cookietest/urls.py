from django.urls import path
from apps.cookietest.views import *


urlpatterns = [
    path('',index,name='cookieindex'),
    path('setcookie',set_cookie,name='setcookie'),
    path('getcookie',get_cookie,name='getcookie'),
]
