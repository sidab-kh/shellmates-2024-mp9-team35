from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView, AssignCategoryView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:blog_id>/assign/', AssignCategoryView.as_view(), name='assign-category'),
]
