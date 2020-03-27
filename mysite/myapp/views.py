from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')


def articles(request):
    return render(request, 'myapp/articles.html')

def pictures(request):
    return render(request, 'myapp/pictures.html')

def resume(request):
    return render(request, 'myapp/resume.html')

def chat(request):
    return render(request, 'myapp/chat.html')