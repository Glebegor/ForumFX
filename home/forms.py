from .models import commentsTabl

class CommentForm(forms.commentsTab):
    class Meta:
        model = commentsTabl
        fields = ('Text')