from django import forms

from .models import *
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import AuthenticationForm


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': '',
                                                          'placeholder': '제목을 입력해주세요'}))
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


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
