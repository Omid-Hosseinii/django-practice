from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def blogList(request):
    template=loader.get_template('blog/blogpage1.html')
    return HttpResponse(template.render())

