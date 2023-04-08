from django.contrib import admin

from .models import NewsArticle, NewsAuthor, NewsCategory, Comment

admin.site.register(NewsArticle)
admin.site.register(NewsAuthor)
admin.site.register(NewsCategory)
admin.site.register(Comment)
