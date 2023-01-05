from rest_framework import serializers
from .models import Post
from auth_api.models import User

class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'formBody', 'imageURL', 'created',)
