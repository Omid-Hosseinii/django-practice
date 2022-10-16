from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Author,articleimg
from .forms import articleimgForm
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
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

#--------------------------------------------------------------------------------
### send mail Functions

def sendMail(subject,message,to):
    Email_from=settings.EMAIL_HOST_USER
    send_mail(subject,message,Email_from,to)

def sendMail2(subject,message,html_content,to):
    Email_from=settings.EMAIL_HOST_USER
    message=EmailMultiAlternatives(subject,message,Email_from,to)
    message.attach_alternative(html_content,"text/html")
    message.send()
   
#--------------------------------------------------------------------------------
### for upload Images
def index(request):
    return render(request,'blog/index.html')


def uploadimg(request):
    if request.method == 'POST':
        form=articleimgForm(request.POST,request.FILES)
        if form.is_valid():
            imageupload=request.FILES['main_img']
            
            if imageupload.size<50000:
            
            
                img,exe=os.path.splitext(imageupload.name)
                current_time=datetime.utcnow().strftime("%Y%m%d%H%M%S")
                imagepath='images/article/'+img+current_time+exe
                    
                data=form.cleaned_data
                article=articleimg()
                article.title=data['title']
                article.text=data['text']
                article.is_active=data['is_active']
                article.main_img=imagepath
                article.save()
                
                
                fss=FileSystemStorage()
                fss.save(imagepath,imageupload)
                sendMail2('ذخیره مقاله','','<h1 style="background-color:green;">مقاله درج شد</h1>',['omid.iipa75@gmail.com'])
            else:
                context={
                    'form':form,
                    'message':'سایز تصویر نباید بیشتر از پنجاه کیلوبایت باشد'
                }    
            
            return redirect('indexblogimg')
    else:
        form=articleimgForm()
        context={
            'form':form
        }    
    return render(request,'blog/uploadimg.html',context)
