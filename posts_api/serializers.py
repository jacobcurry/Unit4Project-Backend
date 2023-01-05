from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'formBody', 'imageURL', 'created',)
