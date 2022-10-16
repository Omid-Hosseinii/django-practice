from django.shortcuts import render
from datetime import time,datetime
from django.conf import settings
import os
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseNotFound
# Create your views here.

def media_admin(request):
    return { "media_url":settings.MEDIA_URL }

def index(request):
    username='مهمان'
    if request.user.is_authenticated:
        username = request.user.username
    request.session['user_name'] = username    
    return render(request,'main/index.html')


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

def testhtml(request):

    return render(request,'main/testhtml.html')


def media_images(request):
    imageList=os.listdir(settings.MEDIA_ROOT+'/images/laptops')
    context={
        
        "imageList":imageList   
    }
    return render(request,'main/photo.html',context)


def download_path(request):
    fs=FileSystemStorage()
    file_name="pdf/moama.pdf"
    if fs.exists(file_name):
        with fs.open(file_name) as pdf:
            response=HttpResponse(pdf,content_type="application/pdf")
            response['Content_Disposition']='attachment; filename=moama.pdf'
            return response
    else:
        return HttpResponseNotFound("Not Found ...!")
        
    



