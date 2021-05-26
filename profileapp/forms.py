from profileapp.models import Profile
from django.forms import ModelForm


class Form(ModelForm):
    class Meta:
        model = Profile
        fields = ("image", "nickname", "massage")
        # fields = ["image", "nickname", "massage"]
