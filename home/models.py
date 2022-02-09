from django.db import models
from django import forms
class register(forms.Form):
    attrs = {
        "type": "password"
    }
    Name = forms.CharField(label='Your name', max_length=100)
    Email = forms.CharField(label='Your Email', max_length=250)
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))
