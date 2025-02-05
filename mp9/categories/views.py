from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Category, BlogCategory
from blogs.models import Blog
from .serializers import CategorySerializer
from rest_framework import status  # Add this import


# List and create categories
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# Retrieve, update, and delete category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# Assign category to blog
class AssignCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        category_ids = request.data.get('category_ids', [])
        blog = Blog.objects.get(id=blog_id)
        
        for category_id in category_ids:
            category = Category.objects.get(id=category_id)
            BlogCategory.objects.create(blog=blog, category=category)
        
        return Response({"message": "Categories assigned successfully!"}, status=status.HTTP_200_OK)
