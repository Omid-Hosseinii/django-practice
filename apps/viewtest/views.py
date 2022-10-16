from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.urls import reverse
# Create your views here.


def index(request):
    context={
        
    }
    return render(request,'viewtest/index.html',context)


class viewClass(View):
    
    def get(self, request):
        context={
            'name':'OmidHosseini'
        }
        return render(request,'viewtest/page1.html',context)



class PostCreate(CreateView):
    model=Post
    fields='__all__'
    # success_url='/viewtest/view2/'
    def get_success_url(self):
        return reverse('view2')


class PostList(ListView):
    model=Post
    paginate_by=15



class PostDetail(DetailView):
    model=Post



class PostUpdate(UpdateView):
    model=Post
    fields='__all__'
    # success_url='/viewtest/view2/'
    def get_success_url(self):
        return reverse('view2')


class PostDelete(DeleteView):
    model=Post
    # success_url='/viewtest/view2/'
    def get_success_url(self):
        return reverse('view2')
    
    
    

class PostList2(ListView):
    model=Post 
    template_name='viewtest/postlist.html'
    context_object_name='posts'
    queryset=Post.objects.order_by('is_active')   
    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context={
    #         'name1':'OmidHosseini'
    #     }
    #     return context