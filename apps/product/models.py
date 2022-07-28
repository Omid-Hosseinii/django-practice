from django.db import models

# Create your models here.


class Product(models.Model):
    type= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    description= models.TextField(max_length=500,null=True, blank=True)
    picaddress= models.CharField(max_length=200,null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.name}\t{self.price}\t{self.description}\t{self.type}"
