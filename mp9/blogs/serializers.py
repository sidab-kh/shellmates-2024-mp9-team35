from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for Blog model.

    This serializer handles the serialization and deserialization of Blog objects,
    including fields for id, title, description, content and user.
    The user field is read-only and will be automatically set based on the request context.

    Attributes:
        Meta: Contains metadata for the serializer including model reference and field definitions.
            - model: Blog model
            - fields: List of fields to be serialized ('id', 'title', 'description', 'content', 'user')
            - extra_kwargs: Additional field configurations, setting user as read-only
    """
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'content', 'user']
        extra_kwargs = {
            'user': {'read_only': True}
        }