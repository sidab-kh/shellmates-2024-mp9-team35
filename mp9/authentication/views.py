from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UserRegistrationView(generics.CreateAPIView):
    """
    A view for handling user registration using Django REST framework.
    This view extends CreateAPIView to provide user registration functionality.
    It validates the password against Django's password validation rules and
    creates a new user if all validations pass.
    Attributes:
        queryset: QuerySet of all CustomUser objects
        serializer_class: UserRegistrationSerializer for data validation and serialization
    Methods:
        create(request, *args, **kwargs): Handles the POST request for user registration
    Returns:
        Response with:
        - 201 CREATED: User registration successful
            {
                "user": serialized_user_data,
            }
        - 400 BAD REQUEST: Password validation failed
            {
                "errors": [error_messages]
            }
    Raises:
        ValidationError: If the password doesn't meet Django's validation requirements
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({"errors": e.messages}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "user": serializer.data,
            "message": "User registered successfully."
        }, status=status.HTTP_201_CREATED, headers=headers)

    
user_registration_view = UserRegistrationView.as_view()