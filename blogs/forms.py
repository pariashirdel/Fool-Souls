from django import forms
from blogs.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','picture','body']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='',widget=forms.Textarea(attrs={
        'rows': '3',
        'placeholder': 'Say Something...'
        }))

    class Meta:
        model = Comment
        fields = ['comment']