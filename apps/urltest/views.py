from django.shortcuts import render
from datetime import time,datetime
from django.conf import settings
import os

# Create your views here.

def index(request):
    return render(request,'urltest/index.html')


def viewfun2(request,name):
    context={
        'name':name,
        'age':27
    }
    return render(request,'urltest/page1.html',context)


def viewfun3(request,name,age):
    context={
        'name':name,
        'age':age
    }
    return render(request,'urltest/page1.html',context)


def viewfun4(request,name,age):
    context={
        'name':name,
        'age':age
    }
    return render(request,'urltest/page1.html',context)


def viewfun5(request,name,age):
    context={
        'name':name,
        'age':age
    }
    return render(request,'urltest/page1.html',context)


def viewfun6(request,x,name,age):
    context={
        'name':name,
        'age':age,
        'x':x
    }
    return render(request,'urltest/page1.html',context)


def viewfun7(request):
    name=request.GET.get('name')
    age=request.GET.get('age')
    context={
        'name':name,
        'age':age,
    }
    return render(request,'urltest/page1.html',context)


from django.urls import reverse
from urllib.parse import urlencode
from django.utils.http import url_has_allowed_host_and_scheme

def viewfun8(request):
    #if not url_has_allowed_host_and_scheme('https://www.google.com',allowed_hosts={'sadahjha.com'},require_https=True):
    if not url_has_allowed_host_and_scheme(url='urltest/u2',allowed_hosts=request.get_host()):   
        return render(request,'urltest/error.html')
   
    base_url=reverse('u7')
    print(base_url)
    query_string=urlencode({'name':'aghaOmid','age':27})
    print(query_string)
    url=f'{base_url}?{query_string}'
    print(url)
    age=request.GET.get('age')
    name=request.GET.get('name')
    context={
        'name':name,
        'age':age
    }
    return render(request,'urltest/page1.html',context)