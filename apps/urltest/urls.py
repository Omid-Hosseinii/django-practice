from django.urls import path,re_path
import apps.urltest.views as views


urlpatterns=[
    
    path('',views.index,name='urlmain'),
    path('u2/<str:name>/',views.viewfun2,name='u2'),
    path('u3/<str:name>/<int:age>/',views.viewfun3,name='u3'),
    re_path(r'u4/(?P<name>[a-z]{3})/(?P<age>[0-9]+)/$',views.viewfun4,name='u4'),
    re_path(r'u5/(?P<name>[a-z]{3})/(?:age-(?P<age>\d+)/)?$',views.viewfun5,name='u5'),
    re_path(r'^u7/',views.viewfun7,name='u7'),
    path('u8',views.viewfun8,name='u8')

]