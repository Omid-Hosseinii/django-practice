from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'sessions/index.html')



def set_session(request):
    request.session['email']='omid75@gmail.com'
    request.session['password']='12345678'
    return render(request, 'sessions/page1.html')
    
    
    
def get_session(request):
    context={}
    if 'email' in request.session:
        email=request.session['email']    
        password=request.session['password']    
        context={
            'email': email,
            'password': password
        }
    return render(request, 'sessions/page2.html',context)
    
    
    
def del_session(request):
    flag=False
    if 'email' in request.session:
        del request.session['email']    
        del request.session['password']
        flag=True
    return render(request, 'sessions/page3.html',{'flag':flag})        
    
    
    
    
    
    
    