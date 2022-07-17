from django.shortcuts import render
from datetime import time,datetime
from django.conf import settings
import os
# Create your views here.



def index(request):
    context={
        "media_url":settings.MEDIA_URL
    }
    return render(request,'main/index.html',context)


def if_condition(request):
    context={
        "name":"omid",
        "age":26
    }
    return render(request,'main/ifcondition.html',context)


def for_condition(request):
    context={
        "name":"Agha omid",
        "age":"26 years old",
        "names":['omid','reza','mohammad','babak'],
        "range":range(1,11),
        "row":range(5),
        "col":range(10)
    }
    return render(request,'main/forcondition.html',context)

def autoescape(request):
    context={
        "str":'<h1 style="background-color:red;">Hello Django</h1>'
    }
    return render(request,'main/autoescape.html',context)

date=datetime.now
def date_time(request):
    context={
        "serverside_date":date
    }
    return render(request,'main/datetime.html',context)



time1=time(23,34,56)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def tag_Filters(request):
    context={
        "names":['omid','reza','mohammad','babak'],
        "str":'HeLLo Im Using django',
        "date":now,
        "time":time1,
        "current_time":current_time
    }
    return render(request,'main/tagfilter.html',context)


def media_images(request):
    imageList=os.listdir(settings.MEDIA_ROOT+'/images/laptops')
    context={
        "media_url":settings.MEDIA_URL,
        "imageList":imageList   
    }
    return render(request,'main/photo.html',context)







