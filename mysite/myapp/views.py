from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, Comment, Pictures, PicComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm, PicCommentForm
from django.views import generic


# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

class ArticlesList(generic.ListView):
    queryset = Articles.objects.filter().order_by('-datePosted')
    template_name = 'myapp/articles.html'

class ArticleDetail(generic.DetailView):
    model = Articles
    template_name ='myapp/article_details.html'

class PicturesList(generic.ListView):
    queryset = Pictures.objects.filter().order_by('-datePosted')
    template_name = 'myapp/pictures.html'

class PicturesDetail(generic.DetailView):
    model = Articles
    template_name ='myapp/picture_details.html'

# def pictures(request):
#     context = {
#         'pictures': Pictures.objects.all(),
#     }
#     return render(request, 'myapp/pictures.html', context)

def resume(request):
    return render(request, 'myapp/resume.html')

def chat(request):
    return render(request, 'myapp/chat.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('Home')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

def ArticleDetail(request,slug):
    template_name = 'myapp/article_details.html'
    article = get_object_or_404(Articles, slug=slug)
    comments = Comment.objects.filter(content=article)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.author = request.user
            new_comment.content = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    return render(request, template_name, {'article': article, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form}) 

def PicturesDetail(request,slug):
    template_name = 'myapp/picture_details.html'
    picture = get_object_or_404(Pictures, slug=slug)
    comments = PicComment.objects.filter(content=picture)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = PicCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.author = request.user
            new_comment.content = picture
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = PicCommentForm()
    
    return render(request, template_name, {'picture': picture, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})    