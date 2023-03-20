from rest_framework import serializers
from django.contrib.auth import get_user_model

from post.models import Post

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['text','id','created_by','created' ]

class PostLijedSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'text','created_by']
