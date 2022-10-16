from cgitb import text
from dataclasses import fields
from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.core import validators
from .models import Post

class InputForm0(forms.Form):
    name=forms.CharField(max_length=10)
    family=forms.CharField(max_length=30)
    age=forms.IntegerField(label='Age1',label_suffix='=')
    is_active=forms.BooleanField(initial=True)
    avg=forms.DecimalField(max_digits=4,decimal_places=2)
    img=forms.ImageField(label='Image')
    FAVORIT_COLORS=[
        ("1","red"),
        ("2","white"),
        ("3","blue"),
        ("4","green")
    ]
    color=forms.ChoiceField(choices=FAVORIT_COLORS)
    colors=forms.MultipleChoiceField(choices=FAVORIT_COLORS,label='Colors')
    url=forms.URLField(label="website",initial="http://",help_text="www.example.com")
  
  
  
class InputForm1(forms.Form):
    name=forms.CharField(max_length=10)
    family=forms.CharField(max_length=30)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    text=forms.BooleanField(widget=forms.Textarea)
  
    FAVORIT_COLORS=[
        ("1","red"),
        ("2","white"),
        ("3","blue"),
        ("4","green")
    ]
    color=forms.ChoiceField(choices=FAVORIT_COLORS,widget=forms.RadioSelect)  
    colors=forms.MultipleChoiceField(choices=FAVORIT_COLORS,label='Colors',widget=forms.CheckboxSelectMultiple)
    Date=forms.CharField(widget=forms.NumberInput(attrs={'type':'date'}))
    YEAR=['2022','2023','2024','2025','2026','2027']
    Date2=forms.CharField(initial=datetime.datetime.now(),widget=forms.SelectDateWidget(years=YEAR))
    Date3=forms.CharField(initial=datetime.datetime.now(),widget=forms.SplitDateTimeWidget)
    Date4=forms.CharField(initial=datetime.datetime.now(),widget=forms.SplitHiddenDateTimeWidget)
    fileupload=forms.CharField(widget=forms.FileInput)
  

def checkvalidateName(value):
    value=str(value)
    if len(value)<3 or len(value)>8:
        raise forms.ValidationError('Name is invalid...!')

  
class InputForm2(forms.Form):
    name=forms.CharField(max_length=10,validators=[checkvalidateName])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(40,message="سن باید پایین 40 باشد"),validators.MinValueValidator(20,message='سن باید بالای 20 باشد')])
    family=forms.CharField(max_length=30)  
    
    
    
    def clean_name(self):
        name=self.cleaned_data["name"]
        return name
    
    def clean_family(self):
        family=self.cleaned_data["family"]
        if family[0]!='A':
            raise ValidationError("family isn't valid...!")
        return family
  
class InputForm3(forms.Form):
    name=forms.CharField(max_length=10)
    family=forms.CharField(max_length=30)  
  
  
class InputForm4(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"