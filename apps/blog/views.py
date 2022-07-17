from django.shortcuts import render
from django.http import HttpResponse
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