from .models import Post, Comment
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):

    comments = CommentSerializer(
        source='comment_set', many=True, required=False
    )

    class Meta:
        model = Post
        fields = '__all__'
