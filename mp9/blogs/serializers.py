from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'content', 'user']
        extra_kwargs = {
            'user': {'read_only': True}
        }