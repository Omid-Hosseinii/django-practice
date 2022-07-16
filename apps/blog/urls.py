from django.urls import path
import apps.blog.views as views

urlpatterns=[
    
    path('list',views.blogList)

]



