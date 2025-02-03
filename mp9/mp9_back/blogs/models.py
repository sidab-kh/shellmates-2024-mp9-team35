from django.db import models
from django.conf import settings  # Import user model

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    content = models.JSONField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
