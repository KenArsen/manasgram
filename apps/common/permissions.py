from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True

        return obj.user == request.user


class IsModeratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.status == "Модератор" or request.method in permissions.SAFE_METHODS
