from django.shortcuts import render
from django.db.models import F, Value

# Create your views here.
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
