from django.contrib import admin
from .models import Articles, Comment, Pictures

# Register your models here.
admin.site.register(Articles)
admin.site.register(Comment)
admin.site.register(Pictures)