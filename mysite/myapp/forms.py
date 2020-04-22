from django import forms
from .models import Comment, Articles

#class CommentForm(forms.ModelForm):
    #class Meta:
        #model = Comment
        #fields = ('author','comment')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author' , 'comment')