from django.db import models
from authentication.models import User


class Blog(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.username}"

