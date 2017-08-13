from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','post']

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','post']