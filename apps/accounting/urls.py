from django.urls import path
import apps.accounting.views as views

urlpatterns=[
    
    path('login/',views.login)


]

