from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title','categories','content','thumbnail']