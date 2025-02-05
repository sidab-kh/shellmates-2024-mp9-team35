from django.urls import path
from .views import LikeBlogView, UnlikeBlogView

urlpatterns = [
    path('<int:blog_id>/like/', LikeBlogView.as_view(), name='like-blog'),
    path('<int:blog_id>/unlike/', UnlikeBlogView.as_view(), name='unlike-blog'),
]
