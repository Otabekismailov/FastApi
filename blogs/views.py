from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from blogs.models import Post, Comment
from blogs.serializers import PostApiListCreateSerializers, AddCommentSerializer
from rest_framework.views import APIView


class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApiListCreateSerializers

    def perform_create(self, serializers):
        serializers.save(author=self.request.user)


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostApiListCreateSerializers
    lookup_field = 'slug'


class LikeApiView(APIView):
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        user = request.user.id
        if user in post.liked.all():
            post.liked.remove(user)
            return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)
        else:
            post.liked.add(user)
            return Response({'detail': 'Post liked.'}, status=status.HTTP_200_OK)


class AddCommentAPI(CreateAPIView):
    lookup_field = 'slug'
    queryset = Comment.objects.all()
    serializer_class = AddCommentSerializer
    permission_class = [IsAuthenticated]

    def perform_create(self, serializers):
        slug = self.kwargs.get('slug')
        post = get_object_or_404(Post, slug=slug)
        serializers.save(post=post, author=self.request.user)
