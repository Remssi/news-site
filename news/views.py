from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import NewsArticle, Comment, NewsAuthor, NewsCategory


class IndexView(generic.ListView):
    template_name = "news/index.html"
    context_object_name = 'latest_articles_list'

    def get_queryset(self):
        return NewsArticle.objects.order_by('-published')


class ArticleView(generic.DetailView):
    template_name = "news/article.html"
    model = NewsArticle
    context_object_name = "article"


class AuthorsView(generic.ListView):
    template_name = "news/authors.html"
    context_object_name = "authors_list"

    def get_queryset(self):
        return NewsAuthor.objects.order_by('-name')


class AuthorView(generic.DetailView):
    template_name = "news/author.html"
    model = NewsAuthor
    context_object_name = "author"


class CategoriesView(generic.ListView):
    template_name = "news/categories.html"
    context_object_name = "categories_list"

    def get_queryset(self):
        return NewsCategory.objects.order_by('-name')


class CategoryView(generic.DetailView):
    template_name = "news/category.html"
    model = NewsCategory
    context_object_name = "category"


def comment(request, article_id):
    article = get_object_or_404(NewsArticle, pk=article_id)

    commentText = request.POST['comment-text']
    if commentText == "":
        context = {
            'article': article,
            'comment_error': "Comment cannot be empty."
        }
        return render(request, 'news/article.html', context)

    newComment = Comment(
        newsArticle=article,
        text=commentText,
        created=timezone.now())
    newComment.save()
    return HttpResponseRedirect(reverse('news:article', args=(article_id,)))
