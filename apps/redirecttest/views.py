from django.shortcuts import render,redirect
from apps.viewtest.models import Post
import random
from django.template.loader import render_to_string
from django.http import (
    
    HttpResponseRedirect,HttpResponsePermanentRedirect,
    HttpResponseNotFound,HttpResponseBadRequest,
    HttpResponseForbidden,HttpResponseServerError
)
# Create your views here.


def index(request):
    return render(request, 'redirecttest/index.html')

def fun1(request):
    return render(request, 'redirecttest/page1.html')



def fun2(request):
    print(HttpResponseRedirect.status_code)
    return HttpResponseRedirect('/redirecttest/r1')

def fun3(request):
    return HttpResponsePermanentRedirect('/redirecttest/r1')


def fun4(request):
    post=Post.objects.filter(pk=5)
    if post:
        context={
            'post': post
        }
        return render(request,"redirecttest/page1.html",context)
    else:
        # return HttpResponseNotFound('<h1>یافت نشد</h1>')
        context={
            'post':'پست مورد نظر حذف شده است'
        }
        content=render_to_string(
            'redirecttest/error.html',
            context,
            request
        )
        return HttpResponseNotFound(content)
    
    
    
    
def fun5(request):
    return HttpResponseBadRequest('this is bad request')


def fun6(request):
    return HttpResponseForbidden('this is forbidden')


def fun7(request):
    return HttpResponseServerError('this is server error') 

#------------------------------------------------------------------------------------------------

def fun8(request):
    posts=Post.objects.all()
    return redirect(posts)  


def fun9(request):
    return redirect('/redirecttest/r1') 



def fun10(request):
    urlList=['r1','r22','r2222']
    return redirect('/redirecttest/'+random.choice(urlList)) 




def fun11(request):
    name='omid'
    return redirect('R5',fname=name) 


def fun12(request,fname):
    context={
        'fname':fname
    }
    return render(request,"redirecttest/page2.html",context) 

from django.urls import reverse
from urllib.parse import urlencode
def fun13(request):
    base_url=reverse('r14')
    querystring=urlencode({'name':'omid','age':27})
    url=f'{base_url}?{querystring}'
    return redirect(url)

def fun14(request):
    name=request.GET.get('name')
    age=request.GET.get('age')
    context={
        'name':name,
        'age':age
    }
    return render(request,'redirecttest/page3.html',context)



def fun15(request):
    response=redirect('r1')
    response.status_code=307
    return response



from django.views.generic.base import RedirectView
class ClassView1(RedirectView):
    # url='https://www.google.com/?q=%(text)s'
    url='https://www.google.com/search?q=%(text)s'