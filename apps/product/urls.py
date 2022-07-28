from django.urls import path
import apps.product.views as views

urlpatterns = [
    path('',views.index,name='index')
]