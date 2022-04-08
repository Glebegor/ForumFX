from django.forms import ModelForm
from .models import Comment

# Create your forms here
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("Text",)