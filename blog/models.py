from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    slug = models.SlugField(default="", blank=True, null=False)
    image = models.ImageField(null=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    summary = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return f"{ self.title } - { self.author }"
    
    def get_absolute_url(self):
        return reverse("single-post-page", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)