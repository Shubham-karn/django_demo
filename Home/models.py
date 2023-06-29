from django.db import models


class Blog(models.Model):
    username = models.CharField(max_length=30, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.username

