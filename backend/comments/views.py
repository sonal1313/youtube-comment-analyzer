from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer

# List all comments or create a new comment
class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Retrieve, update, or delete a specific comment
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

