from rest_framework import serializers

from apps.user.models import Profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "fullname", "avatar", "faculty", "major", "stud_number", "course", "more"]
