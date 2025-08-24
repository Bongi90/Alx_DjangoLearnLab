from rest_framework import viewsets, permissions, filters, generics
from rest_framework.response import Response
from django.db.models import Q
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at", "title"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]

    def get_queryset(self):
        qs = Comment.objects.select_related("post", "author").all()
        post_id = self.request.query_params.get("post")
        if post_id:
            qs = qs.filter(post_id=post_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):

        serializer_class = PostSerializer
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
            user = self.request.user
            following_ids = user.following.values_list("id", flat=True)
            return Post.objects.filter(Q(author__in=following_ids) | Q(author=user)).order_by("-created_at")

        def list(self, request, *args, **kwargs):
            return super().list(request, *args, **kwargs)
