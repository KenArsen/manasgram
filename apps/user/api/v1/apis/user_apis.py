from rest_framework import permissions, status, views, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common import IsModeratorOrReadOnly, IsOwnerOrReadOnly
from apps.user.api.v1.serializers import (
    ProfileSerializer,
    RegisterSerializer,
    UserSerializer,
)
from apps.user.models import Profile, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                "id": user.id,
                "email": user.email,
                "username": user.username,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsModeratorOrReadOnly | IsOwnerOrReadOnly]

    @action(methods=["GET"], detail=False, url_path="profile")
    def get_user_profile(self, request):
        user_instance = request.user
        user = Profile.objects.filter(user=user_instance)
        serializer = self.get_serializer(user, many=True)

        return Response(serializer.data)
