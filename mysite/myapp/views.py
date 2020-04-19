from django.shortcuts import render, redirect
from .models import Articles, Comment, Pictures

from django.contrib.auth.forms import UserCreationForm
from . import forms

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def articles(request):
    articles_objects = Articles.objects.all()
    articles=[]
    for article in articles_objects:
        comment_objects=Comment.objects.filter(content=article)
        temp_article={}
        temp_article["title"] = article.title
        temp_article["content"]=article.content
        temp_article["datePosted"] = article.datePosted
        temp_article["author"]=article.author.username
        temp_article["comments"]=comment_objects
        articles+=[temp_article]
        

    context = {
        'articles': articles,
        #'comments': Comment.objects.all(),
    }
    return render(request, 'myapp/articles.html', context)

def detailed_view(request):
    context={
        'articles': Articles.objects.all(),
    }
    return render(request,'myapp/detailed_view.html', context)

def pictures(request):
    context = {
        'pictures': Pictures.objects.all(),
    }
    return render(request, 'myapp/pictures.html', context)

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
