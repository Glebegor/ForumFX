from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}), max_length="70")
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}), max_length="180")
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Write Password'}), max_length="80")
    password2 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}), max_length="80")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

