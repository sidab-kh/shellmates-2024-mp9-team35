from rest_framework import status  # Import status here
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like
from blogs.models import Blog
from rest_framework.permissions import IsAuthenticated

class LikeBlogView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        like, created = Like.objects.get_or_create(blog=blog, user=request.user)
        
        if created:
            return Response({"message": "Liked successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "You already liked this blog."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikeBlogView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        try:
            like = Like.objects.get(blog_id=blog_id, user=request.user)
            like.delete()
            return Response({"message": "Unliked successfully!"}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"message": "You haven't liked this blog."}, status=status.HTTP_400_BAD_REQUEST)
