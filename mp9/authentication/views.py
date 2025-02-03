from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer
from .models import CustomUser
from django.contrib.auth.models import User

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "user": serializer.data,
            "message": "User registered successfully."
        }, status=status.HTTP_201_CREATED, headers=headers)

    
user_registration_view = UserRegistrationView.as_view()

# Only for testing purposes
class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"detail": "Good it is working"}, status=status.HTTP_200_OK)

test_view = TestView.as_view()