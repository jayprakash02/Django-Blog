from django import forms

from .models import Comment , NewsLetter

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email',)