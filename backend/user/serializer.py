from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FollowersSerializer(serializers.ModelSerializer):
    followed_by = UserSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'followed_by']
