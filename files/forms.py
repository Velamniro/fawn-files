from django import forms

from .models import Comment, Files


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddFileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('title', 'anons', 'url', 'full_txt', 'version', 'type')
