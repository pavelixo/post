from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField(blank=False)
