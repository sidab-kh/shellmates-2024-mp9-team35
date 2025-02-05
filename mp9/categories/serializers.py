from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    """
    A Django REST Framework ModelSerializer for the Category model.

    This serializer handles the serialization and deserialization of Category objects,
    converting them to and from JSON representations.

    Attributes:
        Meta: Inner class defining the model and fields to be serialized
            - model: Category model
            - fields: List of fields to include ('id', 'category_name')
    """
    class Meta:
        model = Category
        fields = ['id', 'category_name']
