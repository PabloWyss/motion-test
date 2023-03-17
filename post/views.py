from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from post.models import Post
from post.permissions import IsSameUser
from post.serializers import PostSerializer


# Create your views here.

class ListCreatePostView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-created')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created']
    ordering = ['created']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class RetrieveUpdateDeletePostView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsSameUser]

class ListLikedPostView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Post.objects.filter(liked_by=self.request.user)
class UpdateLikedPostView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        liked_post_by_user = request.user.posts_liked.all()
        post = self.get_object()
        serializer = self.get_serializer(post)
        if post in liked_post_by_user:
            request.user.posts_liked.remove(post)
            return Response(serializer.data)
        else:
            request.user.posts_liked.add(post)
            return Response(serializer.data)

