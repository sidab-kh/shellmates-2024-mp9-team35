from django.urls import path
"""
URL patterns for the likes app.
This module defines the URL patterns for handling blog post likes and unlikes.
The patterns include:
- like-blog: URL pattern for liking a blog post, accessed via <blog_id>/like/
- unlike-blog: URL pattern for unliking a blog post, accessed via <blog_id>/unlike/
Both paths expect an integer blog_id parameter in the URL.
Example:
    /blogs/1/like/ - Likes blog post with ID 1
    /blogs/1/unlike/ - Unlikes blog post with ID 1
"""
from .views import LikeBlogView, UnlikeBlogView

urlpatterns = [
    path('<int:blog_id>/like/', LikeBlogView.as_view(), name='like-blog'),
    path('<int:blog_id>/unlike/', UnlikeBlogView.as_view(), name='unlike-blog'),
]
