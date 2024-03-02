from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.user.api.v1.apis import ProfileViewSet, RegisterView, UserViewSet

app_name = "users"

router = DefaultRouter()
router.register("", UserViewSet)
router.register("profiles", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="user-register"),
]
