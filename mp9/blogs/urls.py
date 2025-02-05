from django.urls import path
"""
URL configuration for the blogs application.
Contains URL patterns for blog-related views:
- Root path ('') maps to BlogListCreateView for listing and creating blogs
- Path with integer parameter ('<int:pk>/') maps to BlogDetailView for individual blog operations
URL Patterns:
    - blog-list-create: Lists all blogs and handles blog creation
    - blog-detail: Handles individual blog retrieval, update and deletion operations
Dependencies:
    - django.urls.path: For URL pattern definition
    - views.BlogListCreateView: View for listing and creating blogs
    - views.BlogDetailView: View for individual blog operations
"""
from .views import BlogListCreateView, BlogDetailView

urlpatterns = [
    path('', BlogListCreateView.as_view(), name='blog-list-create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]
