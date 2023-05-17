from signal import pthread_kill

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from blogs.models import Post, Comment
from users.models import User


class PostApiListCreateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    like = serializers.IntegerField(required=False)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'tags', 'author', 'image', 'video', 'category', 'like']


class AddCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.IntegerField(required=False)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'post', 'author']

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data["category"] = PostApiListCreateSerializers(instance.category).data
    #     return data
