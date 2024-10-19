from django.urls import path
from .views import CommentListCreate, CommentDetail

urlpatterns = [
    path('comments/', CommentListCreate.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]
