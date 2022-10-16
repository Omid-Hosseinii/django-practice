from django.db import models

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=200,verbose_name='عنوان')
    caption=models.TextField(max_length=200,verbose_name='کپشن پست')
    is_active=models.BooleanField(default=False,verbose_name='وضعیت فعال/غیر فعال')
    
    class Meta:
        db_table = 't_posts'
        verbose_name ='پست'
        verbose_name_plural ='پستها'
    
    def __str__(self):
        return self.title
    
    
    
class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name='پست')    
    
    class Meta:
        db_table = 't_like'
        verbose_name ='لایک'
        verbose_name_plural ='لایک ها'    
        
        
class Contact(models.Model):
    name=models.CharField(max_length=30, verbose_name='نام')
    email= models.EmailField(max_length=30, verbose_name='ایمیل')
    message=models.TextField(verbose_name='پیام') 
    
    class Meta:
        db_table='t_contact'
        verbose_name='تماس با ما'
        verbose_name_plural ='ارتباطات' 
        
           
                   