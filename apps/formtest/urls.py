from django.urls import path
import apps.formtest.views as views

urlpatterns=[
    

    path('forms/',views.forms1,name='form1'),
    path('forms2/',views.forms2,name='form2'),
    path('forms3/',views.forms3,name='form3'),
    path('forms4/',views.forms4,name='form4'),
    path('forms5/',views.forms5,name='form5'),
    path('forms6/',views.forms6,name='form6'),
    path('register/',views.register,name='register'),

]