from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Author
# Create your views here.


def blogList(request):
    template=loader.get_template('blog/blogpage1.html')
    return HttpResponse(template.render())

def author(request):
    authors=Author.objects.all()
    context={
        'authors':authors
    }
    return render(request, 'blog/authors.html',context)

def author_details(request,author_id):
    try:
        author=Author.objects.get(id=author_id)

    except Author.DoesNotExist:
        raise Http404('page not found .....!')
    context={
        'author':author,

    }
    return render(request,'blog/author_detail.html',context)