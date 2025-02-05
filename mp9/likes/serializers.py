from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Like model.

    This serializer is used to convert Like model instances into JSON representations
    and vice versa. It includes the following fields: id, blog, and user.

    Attributes:
        Meta: Inner class defining metadata for the serializer
            model: The Like model that this serializer is based on
            fields: List of fields to include in the serialization
    """
    class Meta:
        model = Like
        fields = ['id', 'blog', 'user']
