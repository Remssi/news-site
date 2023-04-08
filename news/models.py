from django.db import models
from django.utils import timezone


class NewsAuthor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NewsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    heading = models.CharField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey(NewsAuthor, on_delete=models.CASCADE)
    category = models.ForeignKey(NewsCategory, on_delete=models.PROTECT)
    published = models.DateTimeField()
    edited = models.DateTimeField()

    def __str__(self):
        return self.heading

    def was_published_today(self):
        return self.published.date() == timezone.now().date()

    def has_been_edited(self):
        return self.edited > self.published


class Comment(models.Model):
    text = models.TextField()
    newsArticle = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    created = models.DateTimeField()

    def __str__(self):
        return self.text
