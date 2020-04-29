from django import forms
from .models import Comment, Articles, Pictures, PicComment

#class CommentForm(forms.ModelForm):
    #class Meta:
        #model = Comment
        #fields = ('author','comment')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment' ,)

class PicCommentForm(forms.ModelForm):
    class Meta:
        model = PicComment
        fields = ('comment' ,)