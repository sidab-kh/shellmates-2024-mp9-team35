from rest_framework import status  # Import status here
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like
from blogs.models import Blog
from rest_framework.permissions import IsAuthenticated

class LikeBlogView(APIView):
    """
    APIView for handling blog post likes.
    This view allows authenticated users to like blog posts. If the user hasn't liked
    the post before, a new Like object is created. If they have already liked it,
    a message indicating this is returned.
    Attributes:
        permission_classes: List containing IsAuthenticated to ensure only logged in users can like
    Methods:
        post(request, blog_id): Handles POST requests to like a blog post
    Args:
        blog_id (int): The ID of the blog post to like
    Returns:
        Response: JSON response with success/error message and appropriate status code
            - 201: Like was successfully created
            - 400: User has already liked this blog post
    Raises:
        Blog.DoesNotExist: If no blog post exists with the given blog_id
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        like, created = Like.objects.get_or_create(blog=blog, user=request.user)
        
        if created:
            return Response({"message": "Liked successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "You already liked this blog."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikeBlogView(APIView):
    """
    API view for unliking a blog post.
    This view allows authenticated users to remove their like from a specific blog post.
    Attributes:
        permission_classes (list): List containing IsAuthenticated permission class.
    Methods:
        post(request, blog_id): Handles POST request to unlike a blog.
    Args:
        request: The HTTP request object.
        blog_id: The ID of the blog to unlike.
    Returns:
        Response: A JSON response with:
            - 204 NO_CONTENT if successful with message "Unliked successfully!"
            - 400 BAD_REQUEST if blog wasn't liked with message "You haven't liked this blog."
    Requires:
        - User must be authenticated
        - Blog with given blog_id must exist
        - User must have previously liked the blog
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        try:
            like = Like.objects.get(blog_id=blog_id, user=request.user)
            like.delete()
            return Response({"message": "Unliked successfully!"}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"message": "You haven't liked this blog."}, status=status.HTTP_400_BAD_REQUEST)
