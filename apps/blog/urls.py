from django.urls import path
import apps.blog.views as views

urlpatterns=[
    
    path('list',views.blogList,name='blogs'),
    path('author',views.author,name='authors'),
    path('author/<int:author_id>',views.author_details,name='authors_detail')

]



