from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('articles/<int:pk>/',
         views.ArticleView.as_view(), name="article"),
    path('authors/', views.AuthorsView.as_view(), name="authors"),
    path('authors/<int:pk>/', views.AuthorView.as_view(), name="author"),
    path('categories/', views.CategoriesView.as_view(), name="categories"),
    path('categories/<int:pk>/',
         views.CategoryView.as_view(), name="category"),
    path('articles/<int:article_id>/comment/',
         views.comment, name="comment")
]
