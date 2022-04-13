from django import forms
from django.forms import ModelForm
from .models import Comment

# Create your forms here
class CommentForm(ModelForm):
    Text = forms.CharField(widget=forms.Textarea(attrs={'id':'CommentInp', 'placeholder':'Write your comment'}))
    class Meta:
        model = Comment
        fields = ("Text",)