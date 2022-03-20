from django.db import models
from django import forms
from django.contrib.auth.models import User

class register(models.Model):
    attrs = {
        "type": "password"
    }
    Name = forms.CharField(label='Your name', max_length=100)
    Email = forms.CharField(label='Your Email', max_length=250)
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))

class comm(models.Model):
    attrs = {
        "type": "password"
    }
    CommentInp = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Write Your Comment','id':'CommentInp'}))
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)

class loginn(forms.Form):
    attrs = {
        "type": "password"
    }
    Name = forms.CharField(label='Your name', max_length=100)   
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))

    