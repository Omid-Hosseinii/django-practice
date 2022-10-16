from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpRequest
# Create your views here.

def index(request):
    return render(request,'ajaxtest/index.html')


def post(request):
    posts=Post.objects.all()
    like=Like.objects.all()
    context={
        'posts':posts,
        'likes':like
    }
    return render(request,'ajaxtest/post.html',context)


def like(request):
    if request.method == 'GET':
        post_id=request.GET['post_id']
        liked_post=Post.objects.get(id=post_id)
        likepost=Like(post=liked_post)
        likepost.save()
        likecount=len(Like.objects.filter(post_id=post_id))
        # print('*'*100)
        # print(len(likecount))
        # print('*'*100)
        return HttpResponse([likecount])
        
    return HttpResponse("Unsuccess")




def is_ajax(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return True
    else:
        return False

from django.http import JsonResponse
from .forms import contactForm

def contact(request):
    form=contactForm()
    if request.method == 'POST' and is_ajax(request):
        form=contactForm(request.POST)
        if form.is_valid():
            form.save()
            data=form.cleaned_data
            name=data['name']
            return JsonResponse({'name':name},status=200)
        else:
            errors=form.errors.as_json()
            return JsonResponse(errors,status=400)
    
    return render(request,'ajaxtest/contact.html',{'form':form})    
                    
    