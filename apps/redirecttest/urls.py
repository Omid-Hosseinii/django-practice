from django.urls import path
import apps.redirecttest.views as views
from django.views.generic.base import RedirectView


urlpatterns=[
    
    path('',views.index,name='redirectmain'),
    path('r1',views.fun1,name='r1'),
    path('r2',views.fun2,name='r2'),
    path('r22',views.fun3,name='r22'),
    path('r222',views.fun4,name='r222'),
    path('r2222',views.fun5,name='r2222'),
    path('r22222',views.fun6,name='r22222'),
    path('r222222',views.fun7,name='r222222'),
    path('R1',views.fun8,name='R1'),
    path('R2',views.fun9,name='R2'),
    path('R3',views.fun10,name='R3'),
    path('R4',views.fun11,name='R4'),
    path('R5/<str:fname>/',views.fun12,name='R5'),
    path('r13/',views.fun13,name='r13'),
    path('r14/',views.fun14,name='r14'),
    path('r15/',views.fun15,name='r15'),
    path('r16/<text>/',views.ClassView1.as_view(),name='r15'),
    path('r17/<text>/',RedirectView.as_view(url='https://darsman.com/Search/Searching/?s=%(text)s'),name='r17')
]