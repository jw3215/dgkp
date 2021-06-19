from django.forms import ModelForm, models
from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
