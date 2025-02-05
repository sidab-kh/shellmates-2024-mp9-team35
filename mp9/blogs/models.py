from django.db import models
from django.conf import settings  # Import user model

class Blog(models.Model):
    """A model representing a blog entry.

    This class defines the structure of a blog post in the application, containing
    title, description, content in JSON format, and associated user information.

    Attributes:
        title (CharField): The title of the blog post, limited to 255 characters.
        description (TextField): An optional description of the blog post.
        content (JSONField): The main content of the blog post stored in JSON format.
        user (ForeignKey): Reference to the user who created the blog post.

    Relationships:
        - Each blog is associated with exactly one user (many-to-one relationship)
        - When a user is deleted, all their associated blogs are also deleted (CASCADE)
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    content = models.JSONField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
