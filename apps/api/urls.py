from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from ..common.custom_token import CustomTokenObtainPairView

app_name = "api"

urlpatterns = [
    path("users/", include("apps.user.api.v1.user_url", namespace="users")),
    path("posts/", include("apps.post.api.v1.urls", namespace="posts")),
]

# token
urlpatterns += [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
