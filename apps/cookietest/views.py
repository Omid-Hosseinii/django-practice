from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'cookies/index.html')


def set_cookie(request):
    response=render(request,'cookies/page1.html')
    response.set_cookie(key='name',value='omid',max_age=30000)
    response.set_cookie(key='family',value='hosseini',max_age=30000)
    response.set_cookie(key='age',value=27)
    return response



def get_cookie(request):
    context={}
    if request.COOKIES.get('name'):
        name = request.COOKIES['name']
        family = request.COOKIES['family']
        age = request.COOKIES['age']
        context={
            'name':name,
            'family':family,
            'age':age
        }
    return render(request,'cookies/page2.html',context)