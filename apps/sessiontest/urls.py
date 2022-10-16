from django.urls import path
from apps.sessiontest.views import *


urlpatterns =[
    path('',index,name='sessionindex'),
    path('setsession/',set_session,name='setsession'),
    path('getsession/',get_session,name='getsession'),
    path('delsession/',del_session,name='delsession')
]