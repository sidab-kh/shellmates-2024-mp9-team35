from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated

# List and create blogs
class BlogListCreateView(generics.ListCreateAPIView):
    """
    A view class for listing and creating blog posts using Django REST framework.
    This view supports:
    - GET: List all blog posts
    - POST: Create a new blog post
    The view requires authentication for all operations.
    Attributes:
        queryset: QuerySet of all Blog objects
        serializer_class: BlogSerializer for data serialization/deserialization
        permission_classes: List containing IsAuthenticated permission
    Methods:
        perform_create(serializer): Automatically sets the authenticated user as the blog post author
    Returns:
        GET: List of blog posts
        POST: Created blog post data
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user from request
        serializer.save(user=self.request.user)

# Retrieve, update, and delete blog
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
