from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated

# List and create blogs
class BlogListCreateView(generics.ListCreateAPIView):
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
