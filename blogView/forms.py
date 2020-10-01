from django import forms

from .models import Comment , NewsLetter , Blog

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email',)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        feilds = '__all__'