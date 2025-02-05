from django.db import models
from django.conf import settings
from blogs.models import Blog

class Like(models.Model):
    """A Like represents a user's like on a blog post.

    This model establishes a many-to-many relationship between users and blog posts through likes.
    Each like instance connects exactly one user to one blog post.

    Attributes:
        blog (ForeignKey): Reference to the Blog model this like belongs to. Cascading delete.
        user (ForeignKey): Reference to the User model who created this like. Cascading delete.
    """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
