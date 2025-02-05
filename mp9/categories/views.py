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
    """
    A view that handles both listing all categories and creating new categories.

    This view provides GET and POST endpoints for Category objects. It requires
    authentication for all operations.

    Attributes:
        queryset: QuerySet of all Category objects
        serializer_class: The serializer class used for Category objects
        permission_classes: List containing IsAuthenticated permission class

    Methods:
        get: Returns a list of all categories
        post: Creates a new category

    Returns:
        GET: List of serialized Category objects
        POST: Created Category object data
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# Retrieve, update, and delete category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view class for handling detailed operations on Category objects.

    This view supports GET (retrieve), PUT (update), PATCH (partial update), 
    and DELETE operations on individual Category instances.

    Attributes:
        queryset: QuerySet of all Category objects
        serializer_class: Serializer class for Category model
        permission_classes: List containing IsAuthenticated permission class

    Requires:
        - User must be authenticated to access this view
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# Assign category to blog
class AssignCategoryView(APIView):
    """
    View for assigning categories to a blog.
    This view requires authentication and handles POST requests to associate multiple categories
    with a specific blog post.
    Attributes:
        permission_classes (list): List containing IsAuthenticated permission class
    Methods:
        post(request, blog_id): Assigns multiple categories to a specific blog
    Args:
        request (Request): The HTTP request object containing category_ids in request.data
        blog_id (int): The ID of the blog to assign categories to
    Returns:
        Response: JSON response with success message and HTTP 200 status code
    Raises:
        Blog.DoesNotExist: If blog with given blog_id is not found
        Category.DoesNotExist: If any category with given category_id is not found
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        category_ids = request.data.get('category_ids', [])
        blog = Blog.objects.get(id=blog_id)
        
        for category_id in category_ids:
            category = Category.objects.get(id=category_id)
            BlogCategory.objects.create(blog=blog, category=category)
        
        return Response({"message": "Categories assigned successfully!"}, status=status.HTTP_200_OK)
