from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from .serializers import PostSerializer
from .models import Post
from auth_api.models import User

class PostList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
