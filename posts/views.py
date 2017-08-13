from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListAPIView,UpdateAPIView,DestroyAPIView

from posts.models import Post
from posts.serializers import PostSerializer,PostDetailSerializer

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostListAPIView(ListAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()

class PostUpdateAPIView(UpdateAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()

class PostDestroyAPIView(DestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()