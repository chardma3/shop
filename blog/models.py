from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    article = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
