from django.urls import path
import apps.viewtest.views as views
from apps.viewtest.views import *



urlpatterns = [
    path('',views.index,name='indexviews'),
    path('view0/',viewClass.as_view(),name='view0'),
    path('view1/',PostCreate.as_view(),name='view1'),
    path('view2/',PostList.as_view(),name='view2'),
    path('returnvalue/<int:pk>',PostDetail.as_view(),name='view3'),
    path('update/<int:pk>',PostUpdate.as_view(),name='update'),
    path('delete/<int:pk>',PostDelete.as_view(),name='delete'),
    path('list/',PostList2.as_view(),name='postlist'),

]