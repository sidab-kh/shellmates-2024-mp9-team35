from django.db import models
from blogs.models import Blog

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

class BlogCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
