from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):

    status_types = [
        ("PB", "Piblished"),
        ("DR", "Draft"),
    ]

    title = models.CharField(max_length=30, unique=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    create_date = models.DateTimeField(default=timezone.now())
    change_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50)
    status = models.CharField(max_length=2, choices=status_types, default='DR')

    class Meta:
        ordering = ['-create_date']
        indexes = [
            models.Index(fields=['-create_date'])
        ]

    def __str__(self):
        return f"{self.title} - {self.author}"
