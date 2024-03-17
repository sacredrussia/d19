from django.contrib import admin
from .models import Category, Post, Responses, News

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Responses)
admin.site.register(News)
