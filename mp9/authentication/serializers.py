from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    This serializer is used to handle user registration by validating and creating new user instances.
    It uses the CustomUser model and includes email, username, and password fields.\n
    Attributes:
        Meta: Nested class defining metadata for the serializer
            - model: CustomUser model
            - fields: List of fields to include in serialization
            - extra_kwargs: Additional field options (password is write-only)
    \nMethods:\n
        create(validated_data): Creates and returns a new CustomUser instance with validated data
    """
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user