from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.user.api.v1.apis import ProfileViewSet, RegisterView, UserViewSet

app_name = "users"


urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
]


router = DefaultRouter()
router.register("", UserViewSet)
router.register("profiles", ProfileViewSet)


urlpatterns += router.urls
