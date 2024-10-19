from django.urls import path
from .views import CommentListCreate, CommentDetail
from .views import fetch_comments

urlpatterns = [
    path('comments/', CommentListCreate.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('comments/<video_id>/', fetch_comments, name='fetch_comments_with_sentiment'),
]
