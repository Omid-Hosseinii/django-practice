from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=30)
    family=models.CharField(max_length=30)
    age=models.IntegerField(default=20)
    slug=models.SlugField(max_length=100)
    is_active=models.BooleanField(default=True)
    register_date=models.DateTimeField(default=timezone.now)
    email=models.EmailField(max_length=30)
    url_field=models.URLField(default=None)
    
    
    def __str__(self):
        return f"{self.name}\t{self.family}\t{self.age}\t{self.email}\t{self.register_date}"
    