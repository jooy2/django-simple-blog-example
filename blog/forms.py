from django import forms

from .models import *
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=SummernoteWidget())
    # text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 300px'}))

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'text': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
