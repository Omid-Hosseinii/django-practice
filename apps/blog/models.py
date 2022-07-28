from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models
from kiwisolver import Constraint



###   sardabir    
class ChiefEditor(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام')
    family=models.CharField(max_length=50,verbose_name='نام خانوادگی')
    def __str__(self):
        return f"{self.name}\t{self.family}"
    class Meta:
        verbose_name ='سردبیر'
        verbose_name_plural='سردبیرها'      

### entesharat
class Publication(models.Model):
    title=models.CharField(max_length=100,verbose_name='نام انتشارات')
    chiefeditor=models.OneToOneField(ChiefEditor,on_delete=models.CASCADE,primary_key=True,verbose_name='سردبیر')
    def __str__(self):
        return f"{self.title}\t{self.chiefeditor}"
    
    class Meta:
        verbose_name ='نشریه'
        verbose_name_plural='انتشارات'  

### nevisande
class Author(models.Model):
    name=models.CharField(max_length=30,verbose_name='نام')
    family=models.CharField(max_length=30,verbose_name='نام خانوادگی')
    age=models.IntegerField(default=20,verbose_name='سن')
    slug=models.SlugField(max_length=100)
    is_active=models.BooleanField(default=True,verbose_name='فعال')
    register_date=models.DateTimeField(default=timezone.now,verbose_name='تاریخ ثبت')
    email=models.EmailField(max_length=30,verbose_name='ایمیل')
    url_field=models.URLField(default=None,verbose_name='آدرس سایت')
    image_name=models.CharField(max_length=200,null=True,default='p1.png',blank=True)
    
    
    def __str__(self):
        return f"{self.name}\t{self.family}\t{self.age}\t{self.email}\t{self.register_date}"
    class Meta:
        verbose_name ='نویسنده'
        verbose_name_plural='نویسنده ها' 
        constraints=[models.CheckConstraint(check=models.Q(age__gte=18),name='age__gte__18')]     
    
    
### maghale
class Article(models.Model):
    article_title=models.CharField(max_length=300,verbose_name='عنوان مقاله')
    slug=models.SlugField(max_length=100)
    article_text=models.TextField(verbose_name='متن اصلی')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ نوشته شده')
    published_at=models.DateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    update_at=models.DateTimeField(auto_now=True,verbose_name='تاریخ به روز رسانی') 
    is_active=models.BooleanField(default=False,verbose_name='فعال')
    ARTICLE_STATUSE=[
        ('Draft','پیش نویس'),
        ('publish','منتشر شده'),
        ('unknown','نامشخص')
    ]   
    status=models.CharField(max_length=40,choices=ARTICLE_STATUSE,default='Draft',verbose_name='وضعیت مقاله')
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,verbose_name='نویسنده')
    publication=models.ManyToManyField(Publication,verbose_name='سردبیر/انتشارات')
    class Meta:
        verbose_name ='مقاله'
        verbose_name_plural='مقالات' 
        db_table = 'T_Article'  
        ordering=['article_title','is_active']   