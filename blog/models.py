from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('post-by-category', kwargs={'category': self.slug})

    def __str__(self):
        return self.title

    def post_count(self):
        return self.posts.all().count()


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('post-by-tag', kwargs={'tag': self.slug})

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    image = models.ImageField(upload_to="images")
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    tag = models.ManyToManyField(Tag, related_name="tags", blank=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

