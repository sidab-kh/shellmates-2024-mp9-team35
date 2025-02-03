from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import test_view, user_registration_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('users/register/', user_registration_view, name='user_registration'),
    # Only for testing purposes
    path('test/', test_view, name='api_test')
]
