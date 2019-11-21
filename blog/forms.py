from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 300px'}))

    class Meta:
        model = Post
        fields = ('title', 'text',)
