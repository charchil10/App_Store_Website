from django import forms
from .models import Post, Reviews

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['appsName' , 'appsDescription', 'version' , 'App_price']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['author', 'text','ratings',]
