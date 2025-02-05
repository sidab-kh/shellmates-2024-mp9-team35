from django.db import models
from blogs.models import Blog

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

class BlogCategory(models.Model):
    """
    A model representing the many-to-many relationship between Blog and Category models.

    Attributes:
        category (ForeignKey): Reference to the Category model
        blog (ForeignKey): Reference to the Blog model

    This model serves as a junction table to establish many-to-many relationships 
    between blogs and their categories, allowing each blog to belong to multiple 
    categories and each category to contain multiple blogs.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
