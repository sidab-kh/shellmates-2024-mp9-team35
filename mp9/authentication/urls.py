"""
URL configuration for authentication app.
This module defines the URL patterns for authentication-related endpoints using Django Rest Framework's JWT views.
URLs:
    - /token/: Endpoint to obtain a new JWT token pair (access and refresh tokens)
    - /token/refresh/: Endpoint to refresh an expired access token using a valid refresh token
    - /token/verify/: Endpoint to verify if a token is valid
    - /token/blacklist/: Endpoint to blacklist a refresh token
    - /users/register/: Endpoint for user registration
Views:
    - TokenObtainPairView: Handles JWT token pair generation
    - TokenRefreshView: Handles token refresh operations
    - TokenVerifyView: Handles token verification
    - TokenBlacklistView: Handles token blacklisting
    - user_registration_view: Custom view for user registration
"""
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import user_registration_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('users/register/', user_registration_view, name='user_registration')
]
