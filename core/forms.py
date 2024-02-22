from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CollegeForm(forms.ModelForm):
    
    class Meta:
        model = College
        fields = ['name','api_key','desc','logo','root_url','hints']
