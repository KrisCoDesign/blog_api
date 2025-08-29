from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

    
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    discription = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"  # Controls plural display name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='posts')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return self.user