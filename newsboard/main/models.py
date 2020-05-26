from django.db import models
from django.utils.timezone import now

# Create your models here.


class Post(models.Model):
    title = models.TextField(max_length=200)
    link = models.URLField()
    created_at = models.DateTimeField(default=now)
    upvotes = models.IntegerField(default=0)
    author = models.TextField(max_length=42)

    def __str__(self):
        return '%s by %s' % (self.title, self.author)


class Comment(models.Model):
    post = models.ForeignKey(Post, models.CASCADE)
    content = models.TextField(max_length=3000)
    author = models.TextField(max_length=42)
    created_at = models.DateTimeField(default=now)
