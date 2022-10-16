from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30,verbose_name='نام')
    family=models.CharField(max_length=30,verbose_name='نام خانوادگی')
    age=models.IntegerField(default=20,verbose_name='سن')
    email=models.EmailField(max_length=30,verbose_name='ایمیل')
    
    def __str__(self):
        return self.name+" "+self.family
    

def image_path(instance,filename):
    ext=filename.split('.')[-1]
    name=filename.split('.')[0]
    date=datetime.utcnow().strftime("%Y%m%d%H%M%S")  
    return f'images/product/{name}-{date}.{ext}'  
    
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.PositiveIntegerField(default=0)
    register_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to=image_path,default='images/product/noimage.jpg')    
    
    def __str__(self):
        return self.name+' '+str(self.price)
    



class ProductFeature(models.Model):
    feature_name=models.CharField(max_length=200)
    feature_value=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True,related_name='features')
    user_register=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    

        