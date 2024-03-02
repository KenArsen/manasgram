from rest_framework import generics

from apps.post.api.v1.serializers import PostSerializer
from apps.post.repositories import PostRepository
from apps.post.services import PostService


class PostListAPI(generics.ListAPIView):
    service = PostService(PostRepository)
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.service.get_all_posts()


class PostCreateAPI(generics.CreateAPIView):
    service = PostService(PostRepository)
    serializer_class = PostSerializer


class PostDetailAPI(generics.RetrieveAPIView):
    service = PostService(PostRepository)
    serializer_class = PostSerializer

    def get_object(self):
        return self.service.get_post(pk=self.kwargs["pk"])


class PostUpdateAPI(generics.UpdateAPIView):
    service = PostService(PostRepository)
    serializer_class = PostSerializer


class PostDeleteAPI(generics.DestroyAPIView):
    service = PostService(PostRepository)
    serializer_class = PostSerializer
