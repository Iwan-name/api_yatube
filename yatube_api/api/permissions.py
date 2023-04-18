from rest_framework import status
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.method == SAFE_METHODS or obj.author == request.user


class IsComment(BasePermission):
    def has_object_permission(self, request, view, obj):
        if 'Authorization' not in request.headers:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if request.user != obj.author:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class IsCreateGroup(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == ['POST']:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
