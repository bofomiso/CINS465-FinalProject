import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-datePosted']
        
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Articles, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'pictures')

class Pictures(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=100)
    datePosted = models.DateTimeField(auto_now_add=True)
    dateTaken = models.DateField()
    picture = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-datePosted']

    def __str__(self):
        return self.description

class PicComment(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Pictures, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

