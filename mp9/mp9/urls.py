"""
URL configuration for mp9 project.
The `urlpatterns` list routes URLs to views. For more information please see Django documentation:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
URL Patterns:
    - admin/ : Django admin site
    - api/auth/ : Authentication related endpoints
    - api/blogs/ : Blog management endpoints 
    - api/likes/ : Like management endpoints
    - api/categories/ : Category management endpoints
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Shellmates 2024-2025 mp9 API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('api/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    path('admin/', admin.site.urls),
    path('api/auth/', include("authentication.urls")),
    path('api/blogs/', include('blogs.urls')),
    path('api/likes/', include('likes.urls')),
    path('api/categories/', include('categories.urls')),
]
