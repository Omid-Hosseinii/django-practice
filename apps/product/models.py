from django.db import models

# Create your models here.


class Product(models.Model):
    productname= models.CharField(max_length=50)
    productprice= models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.productname}\t{self.productprice}"