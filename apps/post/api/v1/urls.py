from django.urls import path

from apps.post.api.v1.apis import (
    PostCreateAPI,
    PostDeleteAPI,
    PostDetailAPI,
    PostListAPI,
    PostUpdateAPI,
)

app_name = "posts"

urlpatterns = [
    path("", PostListAPI.as_view(), name="post-list"),
    path("create/", PostCreateAPI.as_view(), name="post-create"),
    path("<int:pk>/", PostDetailAPI.as_view(), name="post-detail"),
    path("<int:pk>/update/", PostUpdateAPI.as_view(), name="post-update"),
    path("<int:pk>/delete/", PostDeleteAPI.as_view(), name="post-delete"),
]
