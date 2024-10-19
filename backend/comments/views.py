from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from django.http import JsonResponse
from .youtube_api import get_video_comments

# List all comments or create a new comment
class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Retrieve, update, or delete a specific comment
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def fetch_comments(request, video_id):
    comments = get_video_comments(video_id)
    return JsonResponse({'comments': comments})
