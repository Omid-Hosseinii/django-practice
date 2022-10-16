from django.shortcuts import render,redirect
from .forms import InputForm0, InputForm1, InputForm2,InputForm3,InputForm4
from django.forms import formset_factory
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def forms1(request):
    context={

    }
    return render(request,'formtest/forms1.html',context)

def forms2(request):
    form=InputForm0()
    context={
        'form':form
    }
    return render(request,'formtest/forms2.html',context)


def forms3(request):
    form=InputForm1
    context={
        'form':form
    }
    return render(request,'formtest/forms3.html',context)

def forms4(request):
    context={}
    if request.method == 'POST':
        form=InputForm2(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data["name"])

    else:
        form=InputForm2()            
    context["form"]=form
    return render(request,'formtest/forms4.html',context)




def forms5(request):
    form=InputForm3()
    forms=formset_factory(InputForm3,extra=3)
    forms=forms(initial=[{'name':'omid'}])
    context={
        'form':form,
        'forms':forms
    }
    return render(request,'formtest/forms5.html',context)


def forms6(request):
    context={}
    form=InputForm4(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        post=Post()
        post.name=data["name"]
        post.description=data["description"]
        post.save()
        # return redirect("/formtest/register")
        return HttpResponseRedirect(reverse('register'))
    
    context={
        'form':form
    }
    return render(request,'formtest/forms6.html',context)





def register(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,'formtest/register.html',context)