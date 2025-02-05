from django.urls import path
"""
URL Configuration for Categories App
This module defines the URL patterns for the Categories application, mapping specific URL paths
to their corresponding views.
URL Patterns:
    - '' : Maps to CategoryListCreateView for listing and creating categories
    - '<int:pk>/' : Maps to CategoryDetailView for retrieving, updating, and deleting categories
    - '<int:blog_id>/assign/' : Maps to AssignCategoryView for assigning categories to blogs
Each path is associated with a class-based view and includes a unique name identifier for
reverse URL lookups.
"""
from .views import CategoryListCreateView, CategoryDetailView, AssignCategoryView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:blog_id>/assign/', AssignCategoryView.as_view(), name='assign-category'),
]
