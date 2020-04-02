from django.shortcuts import render, redirect
from .models import Articles

from django.contrib.auth.forms import UserCreationForm
from . import forms

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def articles(request):
    context = {
        'articles': Articles.objects.all()
    }
    return render(request, 'myapp/articles.html', context)

def pictures(request):
    return render(request, 'myapp/pictures.html')

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
