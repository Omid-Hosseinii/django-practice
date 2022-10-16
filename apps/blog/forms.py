from django import forms
from .models import articleimg


class articleimgForm(forms.ModelForm):
    class Meta:
        model=articleimg
        fields=["title","text","is_active","main_img"]