from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed, created or edited.
    """

    queryset = Post.objects.all().order_by('-upvotes', '-created_at')
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        if post:
            post.upvotes += 1
            post.save()
            return Response({'status': 'post upvoted'})
        return Response({'status': 'error'})


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed, created or edited.
    """

    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
