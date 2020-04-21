from django import forms
from .models import Comment, Articles

#class CommentForm(forms.ModelForm):
    #class Meta:
        #model = Comment
        #fields = ('author','comment')

class CommentForm(forms.Form):
    comment = forms.CharField(
        label='Comment',
        required=True,
        max_length=240    
    )

    def save(self, request, art_id):
        article_instance = models.Articles.objects.filter(id=art_id).get()
        comment_instance = models.Comment()
        comment_instance.content = content_instance
        comment_instance.comment = self.cleaned_data["comment"]
        comment_instance.author = request.user
        comment_instance.save()
        return comment_instance
