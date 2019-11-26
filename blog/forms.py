from django import forms

from .models import *
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': '',
                                                          'placeholder': '제목을 입력해주세요'}))
    text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'text': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                           'placeholder': '작성자'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm comment-textarea',
                                                        'placeholder': '여기에 댓글을 입력해주세요.'}))

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
