from django.db import models

# Create your models here.


class Post(models.Model):
    name=models.CharField(max_length=200,verbose_name='عنوان')
    description=models.TextField(max_length=3000,verbose_name='پیام')
    is_active=models.BooleanField(default=False,verbose_name='وضعیت')
    
    def __str__(self):
        return self.name+""+self.description+""+str(self.is_active)